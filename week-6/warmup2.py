def celsius_to_fahrenheit(c):
    z = round((c * 9/5) + 32, 1)
    return(f"{c}°C = {z}°F")
def fahrenheit_to_celsius(f):
    z = round((f - 32) * 5/9, 1)
    return(f"{f}°F = {z}°C")
    
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(72))