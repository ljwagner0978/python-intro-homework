import os
path = os.getcwd()
print(path)
if os.path.exists("C:/Users/lswag/python_class/python_homework/python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")  
path = os.path.join(os.getcwd(), "data", "expenses.csv")
print(path)