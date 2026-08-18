import os
import csv
from datetime import datetime

try:
    if(os.path.exists("./data/expenses.csv")):
        with open("./data/expenses.csv", 'r') as file:
            reader = csv.DictReader(file)
            itemlist = []
            total = 0
            user_input = input("What type of report would you like to choose? (Food, Transport, Utilities, or Entertainment): ")
            while user_input not in ["Food", "Transport", "Utilities", "Entertainment"]:
                print("Invalid input, try again please.")
                user_input = input("What type of report would you like to view? (Food, Transport, Utilities, or Entertainment): ")
            for row in reader:
                itemlist.append({"date": row["date"],"category": row["category"],"description": row["description"],"amount": float(row["amount"])})
                if(row["category"] == user_input): total += float(row["amount"])
            new_itemlist = [item for item in itemlist if item['category'] == user_input]
            report_name = user_input.lower() + "_report.txt"
            with open(report_name, 'w') as file:
                file.write(f'{user_input} Expense Report — generated {datetime.now().strftime("%B %d, %Y")}\n')
                for item in new_itemlist:
                    file.write(f'\n{item["date"]}: ${item["amount"]:,.2f}')
                file.write(f'\nTotal: ${round(total, 2):,.2f}')
                print("Report successfully generated.")       
except Exception as e:
    print(f"An error occurred: {e}")