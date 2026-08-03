while True:
 try:
  x = int(input("Enter a positive integer: "))
  while x < 0:
   print("That's not a positive integer. Try again.")
   x = int(input("Enter a positive integer: "))
  print(f"Got it: {x}")
  break
 except ValueError:
    print("That's not a positive integer. Try again.")