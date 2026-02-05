import pandas as pd

def transform_sales_data(df):
    # Example transformation: add a 'total_price' column
    df["total_price"] = df["quantity"] * df["price"]
    return df

if __name__ == "__main__":
    # Read the extracted data
    df = pd.read_csv("data/processed/extracted_temp.csv")
    
    # Transform data
    df_transformed = transform_sales_data(df)
    
    # Save transformed data to temporary file for load.py
    df_transformed.to_csv("data/processed/transformed_temp.csv", index=False)
    print("Transformed data saved to data/processed/transformed_temp.csv")
    
    # Optional: preview
    print(df_transformed.head())
