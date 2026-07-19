#This code takes a user's inputted number value and evaluates if it is positive/negative and even/odd.

num = int(input("Enter a number: "))

if num == 0:
    print("0 is zero.")
    print("0 is even.")
elif num < 0 and (num % 2 == 0):
    print(f"{num} is negative.")
    print(f"{num} is even.")
elif num > 0 and (num % 2 == 0):
    print(f"{num} is positive.")
    print(f"{num} is even.")
elif num < 0 and (num % 2 != 0):
    print(f"{num} is negative.")
    print(f"{num} is odd.")
elif num > 0 and (num % 2 != 0):
    print(f"{num} is positive.")
    print(f"{num} is odd.")
else:
    print(f"{num} is not a valid number")


  
