# exec_summary.py

# 📦 --- Third-Party Libraries ---
import pandas as pd

# 🧩 --- Executive Summary Loader ---
def get_exec_summary(df):
    """
    Extracts the executive summary body from a config Excel sheet with a single-column header 'value'.

    Expected Excel sheet:
    | value                        |
    |-----------------------------|
    | This month we completed...  |

    Returns:
    {
        "title": "Executive Summary",
        "body": "...summary text..."
    }
    """
    if df.empty or "value" not in df.columns:
        return {
            "title": "Executive Summary",
            "body": ""
        }

    values = df["value"].dropna().astype(str).str.strip().tolist()

    return {
        "title": "Executive Summary",
        "body": values[0] if values else ""
    }