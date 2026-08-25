while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        print(f'You entered: {number}')
        break
    except ValueError:
        print("That's not a valid number. Try again.")