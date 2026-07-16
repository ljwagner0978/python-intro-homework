#This code takes the user's date and provides the date in a sentence structure.

# Navigation commands I used:
# cd lswag/python_homework/python-intro-homework
# ls
# cd week-2/assignment-2

import datetime as dt

while True:
    x = input("What is today's date? (MM/DD/YYYY format) ")
    try:
        user_date = dt.date.strptime(x, "%m/%d/%Y")
        print(f'You said today is {user_date.strftime("%B")} {user_date.strftime("%d")}, {user_date.strftime("%Y")}.')
        break
    except ValueError:
        print("Oops!  That was not a valid date.  Try again...")

