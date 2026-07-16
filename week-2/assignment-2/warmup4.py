#Original code
#This code takes the user's inputted value and divides by 3

#x = (input("Provide me with a number and I shall return 3 times less the value provided: "))
#y = x / 3
#print (y)

#Error Message as a result below

#Traceback (most recent call last):
#  File "C:\Users\lswag\python_class\python_homework\python-intro-homework\week-2\assignment-2\warmup4.py", line 2, in <module>
#  y = x / 3
#        ~~^~~
#TypeError: unsupported operand type(s) for /: 'str' and 'int'

#What caused the error message was that the input was not converted to a float/int value for mathematical operations to occur

#How to fix -- converting the y variable to float type and adding value exception to handle misinputs

while True:
 x = (input("Provide me with a number and I shall return 3 times less the value provided: "))
 try:
  y = float(x) / 3
  print(y)
  break
 except ValueError:
    print("Oops!  That was not a valid number.  Try again...")
