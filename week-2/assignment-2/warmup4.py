#Original code
#This code takes the user's inputted value and divides by 3

#x = input("Provide me with a number and I shall return 3 times less the value provided: ")
#y = x / 3
#This mathematical operation will not work because x is a STRING value. For the operation to occcur, x needs to be a FLOAT or INT type
#print (y)

#1. What the Error Message Said:

#Traceback (most recent call last):

#  y = x / 3
#        ~~^~~
#TypeError: unsupported operand type(s) for /: 'str' and 'int'

#2. What Caused The Error Message: The y variable was NOT converted to a FLOAT/INT value for mathematical operations to occur. This caused the error.

#3. What Fixes the Error: Converting the y variable to FLOAT type and adding value exception to handle misinputs

 x = (input("Provide me with a number and I shall return 3 times less the value provided: "))
 y = float(x) / 3
 print(y)
 
