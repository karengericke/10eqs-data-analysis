import pandas as pd
import requests
import os

def load_data(csv_path):
    """Loads the product data from a CSV file."""
    try:
        df = pd.read_csv(csv_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def fetch_external_data(api_url):
    """Fetches external data from a given API endpoint."""
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch external data. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching external data: {e}")
        return None

def clean_data(df):
    """Performs basic data cleaning (handling missing values)"""
    if df is None:
        return None
    
    df.dropna(inplace=True)
    print("Data cleaned successfully.")
    return df

def generate_insight(df, external_data):
    """Generates insights by comparing internal and external pricing data."""
    if df is None or external_data is None:
        print("Missing data. Cannot generate insight.")
        return None
    
    df['external_price'] = df['our_price'] * 1.1  # Example: External price is 10% higher
    df['price_difference'] = df['external_price'] - df['our_price']
    
    return df[['product_name', 'our_price', 'external_price', 'price_difference']]

def save_report(df, output_path="report.md"):
    """Saves the generated insights into a Markdown report."""
    if df is None:
        return
    
    with open(output_path, "w") as f:
        f.write("# Data Analysis Report\n\n")
        f.write("## Pricing Insights\n\n")
        f.write(df.to_markdown(index=False))
        f.write("\n\n## Recommendations\n\n")
        f.write("Consider adjusting pricing based on market trends.")
    print("Report saved.")
