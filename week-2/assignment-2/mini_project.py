#This code takes the user's inputted fahrenheit temperature value and converts it to celsius

while True:
 fahrenheit = (input("Enter a temperature in Farenheit: "))
 try:
  celsius = round(((float(fahrenheit) - 32) * 5 / 9), 1)
  print(f"{round(float(fahrenheit),1)}°F is {celsius}°C.")
  break
 except ValueError:
    print("Oops!  That was not a valid number.  Try again...")
