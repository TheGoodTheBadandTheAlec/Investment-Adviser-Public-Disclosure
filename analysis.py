import pandas as pd

# Provide the path to your CSV file
file_path = r'C:\Users\alecj\python\Investment Adviser Public Disclosure\extract_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Fill missing values in the 'Total_Assets' column with 0
df['Total_Assets'].fillna(0, inplace=True)

# Convert the 'Total_Assets' column to numeric (in case it contains non-numeric values)
df['Total_Assets'] = pd.to_numeric(df['Total_Assets'], errors='coerce')

# Sum the 'Total_Assets' column
total_assets_sum = df['Total_Assets'].sum()

print(f"Sum of Total Assets: {total_assets_sum}")
