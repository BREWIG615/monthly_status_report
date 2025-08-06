# title_block.py

def get_title_block(df, selected_month_display=None):
    """
    Load title block metadata from Excel config sheet.

    Args:
        df (pd.DataFrame): Sheet with 'key' and 'value' columns.
        selected_month_display (str): Optional month name to override in the date field.

    Returns:
        dict: Keys and values for the title block section.
    """
    if df.empty or not {"key", "value"}.issubset(df.columns):
        return {
            "header": "Default Header",
            "subheader": "Default Subheader",
            "date": selected_month_display or "Undated"
        }

    # Convert to dictionary and lowercase keys
    title_data = dict(zip(df["key"].str.strip().str.lower(), df["value"].astype(str).str.strip()))

    # Capitalize 'date' if overridden by CLI
    if selected_month_display:
        title_data["date"] = f"{selected_month_display} 2025"

    return {
        "header": title_data.get("header", "Default Header"),
        "subheader": title_data.get("subheader", "Default Subheader"),
        "date": title_data.get("date", selected_month_display or "Undated")
    }