def celsius_to_fahrenheit(c):
    z = round((c * 9/5) + 32, 1)
    return(z)
#print(z)
#NameError: name 'z' is not defined   
conversion = celsius_to_fahrenheit(32)
print(conversion)

