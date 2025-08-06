
# 📊 Monthly Status Report Generator

This project converts a structured Excel file into a professional PDF report using Python, Jinja2 templates, and LaTeX. It’s modular, configurable, and supports month-based filtering to make it easy for project teams, managers, or contractors to generate monthly summaries from raw data.

---

## 🚀 Getting Started

These steps will guide you through downloading the repo, setting up your Python environment, and running your first PDF report.

### 1. Clone the Repository

```bash
git clone https://github.com/brewig615/monthly_status_report.git
cd monthly_status_report
```

### 2. Set Up Your Python Environment

Make sure Python 3 is installed (preferably Python 3.10+).

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

The project uses a `requirements.txt` file to list all needed Python packages.

```bash
pip install -r requirements.txt
```

---

## 🗃️ Excel Input File Setup

By default, the script expects the Excel workbook to be named:

```bash
dummy.xlsx
```

You can change the filename in `main.py` by editing this line:

```python
excel_path = "dummy.xlsx"
```

Replace it with the name of your actual Excel file (e.g. `"msr.xlsx"`). Make sure the file is placed in the **project root directory**.

### 🧾 Sheet Expectations

| Sheet Name              | Description                                  |
|-------------------------|----------------------------------------------|
| summary                 | Project-wide task summary                    |
| config_title_block      | Contains title, subheader, date (key/value) |
| config_contact_info     | Contains contact name, org, email, etc.     |
| config_exec_summary     | One-column sheet with mission statement text |
| config_staffing_info    | Staff list with `name`, `role`, `start_date` |
| john, bob, mike, etc.   | One sheet per person, with daily task logs  |

Date fields must be in `YYYY-MM-DD` format (e.g. `2023-07-01`) and should not include time components.

---

## 🖼️ Change the Logo

By default, the PDF report header uses a logo file called:

```
tc_logo.png
```

This is referenced in `templates/fancy_header.tex.j2`:

```latex
\includegraphics[height=2cm]{tc_logo.png}
```

### To change the logo:

1. Replace `tc_logo.png` in the **project root** with your own file.
2. If you rename the logo, update the `\includegraphics` line in `fancy_header.tex.j2`.

Accepted formats: `.png`, `.jpg`, `.pdf`.

---

## 🏃 Running the Report

To generate a report for a specific month, use the `--month` flag:

```bash
python3 main.py --month july
```

This will filter all individual logs to entries starting with `YYYY07`.

The output PDF file will be written to:

```
output.pdf
```

You can also enable logging for debugging purposes:

```bash
python3 main.py --month july --logging
```

This prints parsed data to the console for troubleshooting.

---

## 🛠️ File & Folder Structure

Here's what your project directory should look like:

```
monthly_status_report/
├── main.py
├── dummy.xlsx
├── README.md
├── requirements.txt
├── .gitignore
├── .dockerignore
├── tc_logo.png
├── title_block.py
├── contact_info.py
├── exec_summary.py
├── staffing_info.py
├── person_logs.py
├── templates/
│   ├── template.tex
│   ├── fancy_header.tex.j2
│   ├── exec_summary.tex.j2
│   └── person_logs.tex.j2
├── output.pdf               <-- generated after running script
└── venv/                    <-- virtual environment (ignored)
```

---

## ⚙️ .gitignore and .dockerignore

Both ignore unnecessary build and environment files. You should not include compiled LaTeX logs, `.pdf`, virtual environments, or editor metadata.

```bash
__pycache__/
*.log
*.aux
*.out
*.pdf
*.zip
.env
.vscode/
.idea/
*.db
venv/
```

---

## 📄 Example Command Summary

| Action                         | Command                                 |
|-------------------------------|-----------------------------------------|
| Set up virtualenv             | `python3 -m venv venv && source venv/bin/activate` |
| Install dependencies          | `pip install -r requirements.txt`       |
| Run for July report           | `python3 main.py --month july`          |
| Enable debug logging          | `python3 main.py --month july --logging`|

---

## 🧪 Troubleshooting Tips

- **Missing fields?** Check your Excel sheet names and column headers match the expected structure.
- **Excel parsing error?** Ensure `openpyxl` is installed and you're using `.xlsx`, not `.xls`.
- **Date problems?** Use `YYYY-MM-DD` format in all `start_date` and `task` date fields.
- **PDF not created?** Look for `output.log` or `*.aux` files for LaTeX compilation errors.

---

## 🔗 License

This project is provided under the MIT License.

---

## 🙌 Acknowledgements

Built with ❤️ to streamline monthly reporting and simplify LaTeX/PDF generation from spreadsheets.
