#Traceback (most recent call last):

#  y = x / 3
#        ~~^~~
#TypeError: unsupported operand type(s) for /: 'str' and 'int'

#1. What the Error Message Said: The TypeError message is saying that the operation cannot be complete because the x variable is a string, as such, division (as indicated by "/") cannot occur between a string value and an int value.

#2. What Caused It: Because in this script, the x variable was NOT converted to a FLOAT/INT type for mathematical operations to occur.

#3. What Fixes the Error: Converting the x variable to FLOAT/INT type for this script to run correctly.

 x = (input("Provide me with a number and I shall return 3 times less the value provided: "))
 y = float(x) / 3
 print(y)
 
