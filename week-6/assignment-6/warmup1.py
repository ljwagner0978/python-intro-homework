def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
name = input("What is your name?: ")
greet(name)
greet(name, "Good morning")
greet(name, "Hello")
