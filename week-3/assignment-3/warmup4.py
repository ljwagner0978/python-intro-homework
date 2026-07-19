#This code takes a user's inputted number value and evaluates if it is positive/negative and even/odd.

num = int(input("Enter a number: "))

if num == 0:
    print("0 is zero.")
elif num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")

if (num % 2 == 0) or num == 0: 
   print(f"{num} is even.")
elif (num % 2 != 0):
   print(f"{num} is odd.")

