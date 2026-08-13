x = input("Enter a positive integer: ")
while x.isdigit() == False or int(x) < 1:
   print("That's not a positive integer. Try again.")
   x = input("Enter a positive integer: ")
print(f"Got it: {x}")
