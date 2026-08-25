user_input = input("Enter a number: ")
while True:
    try:
        if user_input.isdigit() or abs(float(user_input)) > 0:
            print(f'You entered: {float(user_input)}')
            break
    except ValueError:
        print("That's not a valid number. Try again.")
        user_input = input("Enter a number: ")