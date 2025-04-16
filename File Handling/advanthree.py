import csv

input_file = 'sales.csv'
output_file = 'high_sales.csv'
high_sales = []

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        try:
            # Remove ₹ symbol, commas, and strip any spaces
            amount_str = row['Amount'].replace('₹', '').replace(',', '').strip()
            amount = float(amount_str)  # Convert to float

            # Only add the row if the amount is greater than ₹10,000
            if amount > 10000:
                high_sales.append(row)
        except ValueError:
            print(f"Skipping row with invalid amount: {row}")

# Print results to check
print("Sales above ₹10,000:\n")
for sale in high_sales:
    print(sale)

# If there are any valid sales, write them to a new file
if high_sales:
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=high_sales[0].keys())
        writer.writeheader()
        writer.writerows(high_sales)
    print(f"\nFiltered high sales written to '{output_file}'")
else:
    print("\nNo sales above ₹10,000 found.")




