import csv
import os

def go_thru(reader):
    data_list = []
    skipped_rows_list = []
    rows_attempted = 0
    rows_parsed = 0
    rows_skipped = 0
    for i, row in enumerate(reader):
        rows_attempted += 1
        if None in row:
            skipped_rows_list.append(f'Row {i+1}: extra column detected — skipped')
            rows_skipped += 1
        else:
            try:
                data_list.append({"name": row["name"],"category": row["category"], "amount": float(row["amount"])})
                rows_parsed += 1
            except (ValueError, KeyError) as e:
                skipped_rows_list.append(f'Row {i+1}: {type(e).__name__} — {e}')
                rows_skipped += 1
    print("=== CSV Report ===")
    print(f"Rows attempted:  {rows_attempted}")
    print(f"Rows parsed:     {rows_parsed}")
    print(f"Rows skipped:    {rows_skipped}\n\n")
    print("Skipped rows:")
    for row in skipped_rows_list:
        print(f'  {row}')
    print("\n\nClean data:")
    for row in data_list:
        print(f'  {row["name"]} | {row["category"]} | ${row["amount"]:,.2f}')


if os.path.exists("../data/messy_data.csv"):
    try:
        with open("../data/messy_data.csv", 'r') as file:
            reader = csv.DictReader(file)
            go_thru(reader)                   
    except FileNotFoundError:
            print(f"Error: 'messy_data.csv' was not found. Please check the file path and try again.")