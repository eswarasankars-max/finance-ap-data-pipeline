import pandas as pd

# Read invoice data
df = pd.read_csv("../data/invoices.csv")

print("Original Records:", len(df))

# Remove duplicate invoice IDs
df = df.drop_duplicates(subset=["invoice_id"])

print("Records After Removing Duplicates:", len(df))

# Convert dates to datetime format
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
df["due_date"] = pd.to_datetime(df["due_date"])

# Save cleaned data
df.to_csv("../data/cleaned_invoices.csv", index=False)

print("Cleaned data saved successfully.")