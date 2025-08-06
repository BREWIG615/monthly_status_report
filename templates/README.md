# MSR Report Generator

A Python + LaTeX + Jinja2-based automated PDF generator for task tracking and reporting.  
This system reads an Excel workbook and generates a polished multi-section report using dynamic Jinja2-LaTeX templates.

## 📦 Project Structure

MSR RedHorse/
├── main.py # Entry point for report generation
├── Dockerfile # Optional containerized setup
├── msr_june.xlsx # Input Excel workbook (rename as needed)
├── README.md # You're reading this!
├── templates/ # All LaTeX Jinja2 templates
│ ├── template.tex
│ ├── title_block.tex.j2
│ ├── contact_info.tex.j2
│ ├── exec_summary.tex.j2
│ ├── task_summary.tex.j2
│ ├── staffing_table.tex.j2
│ ├── person_logs.tex.j2
│ ├── fancy_header.tex.j2
│ └── preamble_packages.tex.j2
├── title_block.py
├── contact_info.py
├── exec_summary.py
├── task_summary.py
├── staffing_info.py
├── person_logs.py
└── output.pdf # Output is generated after build

## 🚀 How to Run

1. **Install requirements:**

```bash
pip install pandas jinja2 openpyxl
sudo apt install texlive-full  # For LaTeX tools like pdflatex

2. Run with default (all records):
python3 main.py

3. Run with a month filter (e.g., only June entries):
python3 main.py --month june

4.Enable debug logging output:
python3 main.py --logging

✏️ Customizing the Report

Each section is modular and controlled via:

    Jinja2 .tex.j2 templates in templates/

    Corresponding Python config files (e.g. title_block.py, exec_summary.py)

To change the title, summary, or contact information:

    Edit the appropriate .py file.

To change layout or LaTeX styling:

    Edit the matching .tex.j2 file under templates/.

📄 Excel Format Expectations

    Sheet 1: Task summary
    Required columns: project, date, task

    Other Sheets: One sheet per person, containing completed tasks
    Required columns: project, date, task, (optional issue)

Date format must be YYYYMMDD.
🐳 Docker (Optional)

Build a container to run the report without needing LaTeX installed locally: