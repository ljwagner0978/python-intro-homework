#This code takes the user's inputted fahrenheit temperature value and converts it to celsius

 fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
 
celsius = round(((fahrenheit - 32) * 5 / 9), 1)
  print(f"{fahrenheit}°F is {celsius}°C.")
