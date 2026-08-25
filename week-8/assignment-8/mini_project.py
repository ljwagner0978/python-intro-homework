import csv

def go_thru(reader):
    data_list = []
    skipped_rows_list = []
    rows_attempted = 0
    rows_parsed = 0
    rows_skipped = 0
    for i, row in enumerate(reader):
        try:
            rows_attempted += 1
            if None in row:
                skipped_rows_list.append(f'Row {i+1}: extra column detected — skipped')
                rows_skipped += 1
            else:
                data_list.append({"name": row["name"],"category": row["category"], "amount": float(row["amount"])})
                rows_parsed += 1
        except ValueError as e:
            skipped_rows_list.append(f'Row {i+1}: ValueError - {e}')
            rows_skipped += 1
        except KeyError as e:
            skipped_rows_list.append(f'Row {i+1}: KeyError - {e}')
            rows_skipped += 1
    print("=== CSV Report ===")
    print(f"Rows attempted:  {rows_attempted}")
    print(f"Rows parsed:     {rows_parsed}")
    print(f"Rows skipped:    {rows_skipped}")
    print()
    print()
    print("Skipped rows:")
    for row in skipped_rows_list:
        print((' ' * 2) + f'{row}')
    print()
    print()
    print("Clean data:")
    for row in data_list:
        print((' ' * 2) + f'{row["name"]} | {row["category"]} | ${row["amount"]:,.2f}')

try:
    with open("../data/messy_data.csv", 'r') as file:
        reader = csv.DictReader(file)
        go_thru(reader)                   
except FileNotFoundError:
    print(f"Error: 'messy_data.csv' was not found. Please check the file path and try again.")