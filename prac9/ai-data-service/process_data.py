import pandas as pd

df = pd.read_csv("transaction.csv")

print("Original Data:")
print(df)

# Replace missing values with median
median_amount = df["Amount"].median()
df["Amount"] = df["Amount"].fillna(median_amount)

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

# Group data by User_ID
summary = df.groupby("User_ID").agg(
    Total_Spent=("Amount", "sum"),
    Total_Transactions=("Transaction_ID", "count")
).reset_index()

# Save report
summary.to_csv("summary_report.csv", index=False)

print("\nSummary Report:")
print(summary)

print("\nCSV created successfully!")