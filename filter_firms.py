import csv

input_file_path = r'C:\Users\alecj\python\Investment Adviser Public Disclosure\extract_data.csv'
output_file_path = r'C:\Users\alecj\python\Investment Adviser Public Disclosure\filter_firms.csv'

#adjust min and max aum based on requirements 

#min AUM
lower_threshold_total_assets = 10000000

#max AUM
upper_threshold_total_assets = 100000000000000000

# Open the input CSV file
with open(input_file_path, 'r', newline='', encoding='utf-8') as infile:
    # Use csv.reader to handle the CSV structure
    reader = csv.reader(infile)

    # Read the header
    header = next(reader)

    # Filter rows based on Total_Assets within the specified range
    filtered_rows = [row for row in reader if row and row[9] and lower_threshold_total_assets < int(row[9]) < upper_threshold_total_assets]

# Sort the filtered rows based on Total_Assets in descending order
sorted_rows = sorted(filtered_rows, key=lambda x: int(x[9]), reverse=False)

# Write the sorted rows to a new CSV file
with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
    # Use csv.writer to handle the CSV structure
    writer = csv.writer(outfile)

    # Write the header to the output file
    writer.writerow(header)

    # Write the sorted rows to the output file
    writer.writerows(sorted_rows)

print(f"Rows with Total_Assets between {lower_threshold_total_assets} and {upper_threshold_total_assets} filtered and sorted successfully. Output file saved at:", output_file_path)
