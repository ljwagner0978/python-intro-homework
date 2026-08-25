numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    result = (float(numerator)/float(denominator))
    print(f'{float(numerator)} ÷ {float(denominator)} = {result:.1f}')
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")