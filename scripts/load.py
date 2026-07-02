import pandas as pd
import sqlite3

# Read cleaned data
df = pd.read_csv("../data/cleaned_invoices.csv")

# Connect to SQLite database
conn = sqlite3.connect("../finance.db")

# Load data into a table
df.to_sql("invoices", conn, if_exists="replace", index=False)

print("Data loaded successfully into SQLite database.")

# Close connection
conn.close()