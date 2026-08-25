numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    print(f'{float(numerator)} ÷ {float(denominator)} = {round(float(numerator)/float(denominator), 1)}')
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")