#This code takes a user's inputted number value and evaluates if it is positive/negative and even/odd.

num = int(input("Enter a number: "))

if num == 0:
    print("0 is zero.")
elif abs(num) != num:
    print(f"{num} is negative.")
else:
    print(f"{num} is positive.")

if num == 0:
    print("0 is even.")
elif ((num / 2) % 1 != 0):
    print(f"{num} is odd.")
else:
    print(f"{num} is even.")


  