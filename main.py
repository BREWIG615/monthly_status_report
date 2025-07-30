# 🧰 --- Standard Library ---
import os
import subprocess
import argparse
from datetime import datetime

# 📦 --- Third-Party Libraries ---
import pandas as pd
from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError

# 🧩 --- Custom Section Data ---
from title_block import title_block
from contact_info import contact_info
from exec_summary import exec_summary
from task_summary import task_summary_title
from staffing_info import staffing_info
from person_logs import person_logs_config

# ✨ --- Escape LaTeX special characters ---
def escape_latex(value):
    if pd.isnull(value): return ""
    if not isinstance(value, str): value = str(value)
    return (
        value.replace('\\', r'\textbackslash{}').replace('&', r'\&').replace('%', r'\%').replace('$', r'\$').replace('#', r'\#').replace('_', r'\_').replace('{', r'\{').replace('}', r'\}').replace('~', r'\textasciitilde{}').replace('^', r'\textasciicircum{}').replace('\n', ' ').strip())

def main():
    # 🧾 --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="Generate PDF from Excel and LaTeX template.")
    parser.add_argument("--logging", action="store_true", help="Enable debug logging output")
    parser.add_argument("--month", type=str, help="Limit results to a specific month, e.g., --month june")
    args = parser.parse_args()

    # 🗓️ --- Optional month filtering setup ---
    month_map = {
        'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06',
        'july': '07', 'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'
    }

    filter_prefix = None
    if args.month:
        selected_month = args.month.lower()
        if selected_month in month_map:
            current_year = datetime.now().year
            filter_prefix = f"{current_year}{month_map[selected_month]}"
        else:
            raise ValueError(f"Invalid month: {args.month}. Use full month names like 'june'.")

    # 🖨️ --- Set up Jinja2 environment ---
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=False)

    # 🔧 Register LaTeX escaping filter
    env.filters['latex'] = escape_latex

    # 📂 --- Load Excel workbook ---
    excel_path = "msr.xlsx"
    all_sheets = pd.read_excel(excel_path, sheet_name=None, engine="openpyxl")

    # 🧽 --- Normalize sheet columns ---
    def normalize_df(df):
        df.columns = [col.lower().strip() for col in df.columns]
        return df

    all_sheets = {name: normalize_df(df) for name, df in all_sheets.items()}

    # 🔀 --- Split summary and task logs ---
    summary_sheet_name = list(all_sheets.keys())[0]
    summary_records = all_sheets[summary_sheet_name].to_dict(orient="records")

    all_logs = {}
    for sheet, df in all_sheets.items():
        if sheet == summary_sheet_name:
            continue
        if "date" in df.columns and filter_prefix:
            df = df[df["date"].astype(str).str.startswith(filter_prefix)]
        all_logs[sheet] = df.to_dict(orient="records")

    # 🐞 --- Debug Output ---
    if args.logging:
        print("=== Summary Records ===")
        for record in summary_records: print(record)
        print("\n=== All Logs ===")
        for person, records in all_logs.items():
            print(f"\n-- {person} --")
            for row in records: print(row)

    # 📜 --- Render LaTeX Template ---
    try:
        template = env.get_template("template.tex")
        rendered_tex = template.render(
            summary=summary_records,
            all_logs=all_logs,
            title_block=title_block,
            contact_info=contact_info,
            exec_summary=exec_summary,
            task_summary_title=task_summary_title,
            staffing_info=staffing_info,
            person_logs_config=person_logs_config
        )
    except TemplateSyntaxError as e:
        print(f"Jinja2 template error: {e.message} at line {e.lineno}")
        raise

    # 📝 --- Write .tex to disk ---
    tex_path = "output.tex"
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(rendered_tex)

    # 🖨️ --- Compile LaTeX to PDF ---
    try:
        if args.logging:
            subprocess.run(["pdflatex", tex_path], check=True)
        else:
            subprocess.run(["pdflatex", tex_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("\n❌ LaTeX Compilation Error — Last 30 lines of output.log:")
        with open("output.log", "r", encoding="utf-8") as log:
            lines = log.readlines()
            print("".join(lines[-30:]))
        raise

    # 🧹 --- Clean up auxiliary files ---
    for ext in ["aux", "log", "out"]:
        try: os.remove(f"output.{ext}")
        except FileNotFoundError: pass

# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    main()
