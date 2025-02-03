import pandas as pd
import requests
import os

# Load and process CSV data
def load_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Integrate external pricing data (Example: Dummy API call)
def fetch_external_data():
    try:
        response = requests.get("https://dummyjson.com/products")  # Placeholder API
        if response.status_code == 200:
            data = response.json()
            if "products" in data and isinstance(data["products"], list):
                return [{"title": item.get("title", "Unknown"), "price": item.get("price", 0)} for item in data["products"]]
            else:
                print("Invalid data format in external API response.")
                return None
        else:
            print("Failed to fetch external data.")
            return None
    except Exception as e:
        print(f"Error fetching external data: {e}")
        return None

# Generate insights
def generate_insight(df, external_data):
    if df is None or external_data is None:
        print("Missing data. Cannot generate insight.")
        return None
    
    df['external_price'] = df['our_price'] * 1.1  # Example: External price is 10% higher
    df['price_difference'] = df['external_price'] - df['our_price']
    
    return df[['product_name', 'our_price', 'external_price', 'price_difference']]

# Save report
def save_report(df, output_path="report.md"):
    if df is None:
        return
    
    with open(output_path, "w") as f:
        f.write("# Data Analysis Report\n\n")
        f.write("## Pricing Insights\n\n")
        f.write(df.to_string(index=False))
        f.write("\n\n## Recommendations\n\n")
        f.write("Consider adjusting pricing based on market trends.")
    print("Report saved.")

if __name__ == "__main__":
    csv_file = os.path.join(os.path.dirname(__file__), "data/products.csv")
    df = load_data(csv_file)
    external_data = fetch_external_data()
    insights = generate_insight(df, external_data)
    save_report(insights)