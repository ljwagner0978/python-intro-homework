numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

print("=== Number Cruncher ===")
print("1. Find minimum")
print("2. Find maximum")
print("3. Search for a number")
print("4. Sort the list")
print("5. Quit")
user_input = input("Choose an option (1-5): ")

while user_input.isdigit() == False or int(user_input) <= 0 or int(user_input) >= 6:
        print("Invalid input, try again please.")
        print("=== Number Cruncher ===")
        print("1. Find minimum")
        print("2. Find maximum")
        print("3. Search for a number")
        print("4. Sort the list")
        print("5. Quit")
        user_input = input("Choose an option (1-5): ")

while int(user_input) >= 1 and int(user_input) <= 5:
        if int(user_input) == 1:
            min_number = numbers[0]
            for number in numbers:
                if(min_number > number):
                    min_number = number
            print(min_number)
            print("=== Number Cruncher ===")
            print("1. Find minimum")
            print("2. Find maximum")
            print("3. Search for a number")
            print("4. Sort the list")
            print("5. Quit")
            user_input = input("Choose an option (1-5): ")
        elif int(user_input) == 2:
            top_number = numbers[0]
            for number in numbers:
                if(top_number < number):
                    top_number = number
            print(top_number)
            print("=== Number Cruncher ===")
            print("1. Find minimum")
            print("2. Find maximum")
            print("3. Search for a number")
            print("4. Sort the list")
            print("5. Quit")
            user_input = input("Choose an option (1-5): ")
        elif int(user_input) == 3:
            number_input = input("Please provide a number: ")
            while True:
                if number_input.isdigit() == False:
                   print("Invalid number inputted. Please try again")
                   number_input = input("Please provide a number: ")
                for i in range(len(numbers)):
                    if numbers[i] == int(number_input):
                       print(f"Found at index: {i}")
                       break
                    elif i == (len(numbers)-1):
                       print("Not found")
                       break
                break
            print("=== Number Cruncher ===")
            print("1. Find minimum")
            print("2. Find maximum")
            print("3. Search for a number")
            print("4. Sort the list")
            print("5. Quit")
            user_input = input("Choose an option (1-5): ")
        elif int(user_input) == 4:
            swapped = True
            j = 0
            while swapped != False:
                
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    swapped = True
                else:
                    swapped = False
                j+= 1
            print(numbers)
            print("=== Number Cruncher ===")
            print("1. Find minimum")
            print("2. Find maximum")
            print("3. Search for a number")
            print("4. Sort the list")
            print("5. Quit")
            user_input = input("Choose an option (1-5): ")
        elif int(user_input) == 5:
            print("Goodbye.")
