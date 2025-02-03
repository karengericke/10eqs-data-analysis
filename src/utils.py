import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs basic cleaning on the dataframe:
      - Strips whitespace from column headers.
      - Drops empty rows (if any).
      - Fixes data types if necessary.
    Returns the cleaned dataframe.
    """
    # 1. Strip column name whitespace
    df.columns = [col.strip() for col in df.columns]
    
    # 2. Drop completely empty rows
    df.dropna(how='all', inplace=True)
    
    # 3. Convert numeric columns if needed (example: 'our_price' to float)
    if 'our_price' in df.columns:
        df['our_price'] = pd.to_numeric(df['our_price'], errors='coerce')
    
    # Return the cleaned DataFrame
    return df


def check_missing_values(df: pd.DataFrame) -> dict:
    """
    Checks for missing values across all columns in the DataFrame.
    Returns a dictionary with {column_name: number_of_missing_values}.
    """
    missing_info = {}
    for col in df.columns:
        missing_count = df[col].isna().sum()
        if missing_count > 0:
            missing_info[col] = missing_count
    return missing_info


def summarize_data(df: pd.DataFrame) -> str:
    """
    Generates a quick summary of the data including row and column counts.
    Returns the summary as a formatted string.
    """
    row_count, col_count = df.shape
    summary = (
        f"Data Summary:\n"
        f"  - Rows: {row_count}\n"
        f"  - Columns: {col_count}\n"
        "  - Columns List: " + ", ".join(df.columns) + "\n"
    )
    return summary


def validate_response_data(data) -> bool:
    """
    Basic validation for external API data.
    Check if the response data meets the expected structure (list of dicts).
    Returns True if valid, False otherwise.
    """
    if not isinstance(data, list):
        return False
    # Just an example check for expected keys in the first item
    if data and not isinstance(data[0], dict):
        return False
    return True
