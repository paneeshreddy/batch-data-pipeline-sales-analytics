import pandas as pd
import os
import sys

# -------------------
# Paths
# -------------------
RAW_FILE = "data/raw/sales.csv"
PROCESSED_DIR = "data/processed/"
FINAL_FILE = os.path.join(PROCESSED_DIR, "sales_transformed.csv")
EXTRACTED_TEMP = os.path.join(PROCESSED_DIR, "extracted_temp.csv")
TRANSFORMED_TEMP = os.path.join(PROCESSED_DIR, "transformed_temp.csv")

# Analytics report paths
REVENUE_COUNTRY_FILE = os.path.join(PROCESSED_DIR, "revenue_by_country.csv")
QUANTITY_COUNTRY_FILE = os.path.join(PROCESSED_DIR, "quantity_by_country.csv")
TOP_PRODUCTS_FILE = os.path.join(PROCESSED_DIR, "top_products.csv")
DAILY_REVENUE_FILE = os.path.join(PROCESSED_DIR, "daily_revenue.csv")

# -------------------
# Extract
# -------------------
def extract_sales_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Raw file {file_path} not found.")
        sys.exit(1)
    df = pd.read_csv(file_path)
    print("Step 1: Extract complete")
    return df

# -------------------
# Transform + Analytics
# -------------------
def transform_and_analyze(df):
    # Remove missing quantity or price
    df = df.dropna(subset=["quantity", "price"])

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_date"])

    # Add total_price column
    df["total_price"] = df["quantity"] * df["price"]

    # --- Analytics Summaries ---
    revenue_country = df.groupby("country")["total_price"].sum().reset_index()
    revenue_country.rename(columns={"total_price": "total_revenue"}, inplace=True)
    revenue_country.to_csv(REVENUE_COUNTRY_FILE, index=False)

    quantity_country = df.groupby("country")["quantity"].sum().reset_index()
    quantity_country.to_csv(QUANTITY_COUNTRY_FILE, index=False)

    top_products = df.groupby("product_id")["total_price"].sum().reset_index()
    top_products = top_products.sort_values(by="total_price", ascending=False).head(5)
    top_products.to_csv(TOP_PRODUCTS_FILE, index=False)

    daily_revenue = df.groupby("order_date")["total_price"].sum().reset_index()
    daily_revenue.to_csv(DAILY_REVENUE_FILE, index=False)

    # Print summaries for quick view
    print("\n--- Total Revenue by Country ---\n", revenue_country)
    print("\n--- Total Quantity by Country ---\n", quantity_country)
    print("\n--- Top 5 Products by Revenue ---\n", top_products)
    print("\n--- Daily Revenue Trends ---\n", daily_revenue)

    print("Step 2: Transform + Analytics complete")
    return df

# -------------------
# Load
# -------------------
def load_sales_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Step 3: Load complete → Data saved to {output_file}")

# -------------------
# Main pipeline
# -------------------
if __name__ == "__main__":
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Extract
    df_extracted = extract_sales_data(RAW_FILE)
    df_extracted.to_csv(EXTRACTED_TEMP, index=False)

    # Transform + Analytics
    df_transformed = transform_and_analyze(df_extracted)
    df_transformed.to_csv(TRANSFORMED_TEMP, index=False)

    # Load
    load_sales_data(df_transformed, FINAL_FILE)

    # Cleanup temporary files
    if os.path.exists(EXTRACTED_TEMP):
        os.remove(EXTRACTED_TEMP)
    if os.path.exists(TRANSFORMED_TEMP):
        os.remove(TRANSFORMED_TEMP)

    print("\nETL pipeline finished successfully! Analytics reports saved in data/processed/")
