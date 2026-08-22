def celsius_to_fahrenheit(c):
    z = round((c * 9/5) + 32, 1)
#print(z)
#NameError: name 'z' is not defined
#The variable z is a local variable and cannot be accessed in global.

def give_name(Name):
    name = Name
    return name
print(give_name("Sally"))
#This works because this function returns the value of the local variable "name"

