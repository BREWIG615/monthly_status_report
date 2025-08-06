# contact_info.py

# 📦 --- Third-Party Libraries ---
import pandas as pd

# 🧩 --- Contact Info Loader ---
def get_contact_info(df):
    if df.empty:
        return {}

    if not {'key', 'value'}.issubset(df.columns):
        raise ValueError("Expected columns: 'key' and 'value'")

    # Drop rows with missing key/value and strip whitespace
    df = df.dropna(subset=['key', 'value'])
    df['key'] = df['key'].astype(str).str.strip()
    df['value'] = df['value'].astype(str).str.strip()

    return dict(zip(df['key'], df['value']))

# 🧩 --- Top-level reference (used in main.py like a config constant) ---
contact_info = {}