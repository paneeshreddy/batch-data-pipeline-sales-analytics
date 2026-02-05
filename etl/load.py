import pandas as pd

# Read the transformed data
df = pd.read_csv("data/processed/transformed_temp.csv")

# Save the final processed data
df.to_csv("data/processed/sales_transformed.csv", index=False)
print("Data successfully saved to data/processed/sales_transformed.csv")
