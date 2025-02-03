import pandas as pd
import requests

# Import helper functions from utils
from utils import (
    clean_dataframe,
    check_missing_values,
    summarize_data,
    validate_response_data
)

def load_data(csv_path: str) -> pd.DataFrame:
    """
    Loads and cleans product data from a CSV file.
    """
    try:
        df = pd.read_csv(csv_path)
        # Clean the dataframe using our helper function
        df = clean_dataframe(df)
        print("Data loaded and cleaned successfully.")
        # Check for missing values
        missing = check_missing_values(df)
        if missing:
            print("Warning: Missing values found in columns:", missing)
        # Print a quick summary of the data
        print(summarize_data(df))

        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def fetch_external_data() -> list:
    """
    Fetches external pricing data (dummy example) 
    from a public API (https://dummyjson.com).
    """
    try:
        response = requests.get("https://dummyjson.com/products")
        if response.status_code == 200:
            api_data = response.json()

            # Check if the 'products' key is present and valid
            if 'products' in api_data:
                products = api_data['products']
                if validate_response_data(products):
                    # Convert data to a list of dictionaries with relevant fields
                    return [
                        {
                            "title": item.get("title", "Unknown"),
                            "price": item.get("price", 0)
                        }
                        for item in products
                    ]
            print("Invalid data format in external API response.")
            return None
        else:
            print(f"Failed to fetch external data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching external data: {e}")
        return None

def generate_insight(df: pd.DataFrame, external_data: list) -> pd.DataFrame:
    """
    Generates an insight by comparing our price to external price data.
    """
    if df is None or external_data is None:
        print("Missing data. Cannot generate insight.")
        return None
    df["external_price"] = df["our_price"] * 1.1
    df["price_difference"] = df["external_price"] - df["our_price"]
    # Return columns of interest
    return df[["product_name", "our_price", "external_price", "price_difference"]]

def save_report(df: pd.DataFrame, output_path="report.md"):
    """
    Saves the pricing analysis report to a Markdown file.
    """
    if df is None:
        return

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Data Analysis Report\n\n")
        f.write("## Pricing Insights\n\n")
        f.write(df.to_string(index=False))
        f.write("\n\n## Recommendations\n\n")
        f.write("Consider adjusting pricing based on market trends.\n")
    print(f"Report saved to {output_path}.")

if __name__ == "__main__":
    # CSV path
    csv_file = "C:/Users/Kmger/OneDrive/Bureau/karenina/10eqs-data-analysis/data/products.csv"
    # 1. Load CSV Data
    df = load_data(csv_file)
    # 2. Fetch External Data
    external_data = fetch_external_data()
    # 3. Generate Insight
    insights = generate_insight(df, external_data)
    # 4. Save Report
    save_report(insights)
