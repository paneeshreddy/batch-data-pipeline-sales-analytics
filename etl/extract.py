import pandas as pd

def extract_sales_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = extract_sales_data("data/raw/sales.csv")
    print(df.head())

    # Save the extracted data for transform.py
    df.to_csv("data/processed/extracted_temp.csv", index=False)
    print("Extracted data saved to data/processed/extracted_temp.csv")
