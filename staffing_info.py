# staffing_info.py

# 📦 --- Third-Party Libraries ---
import pandas as pd

# 🧩 --- Staffing Info Loader ---
def get_staffing_info(df):
    """
    Extracts staffing information from a config Excel sheet.

    Expected columns (case-insensitive):
    - name
    - role
    - start_date

    Returns:
    - List of dictionaries: [{ name, role, start_date }, ...]
    """
    if df.empty:
        return []

    required_cols = {'name', 'role', 'start_date'}
    df.columns = [col.lower().strip() for col in df.columns]

    if not required_cols.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required_cols - set(df.columns)}")

    df = df.dropna(subset=['name', 'role'])

    # ✅ Strip time if any, keep date string as-is
    df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce').dt.date.astype(str)

    return df.to_dict(orient="records")