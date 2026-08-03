numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

print("=== Number Cruncher ===")
print("1. Find minimum")
print("2. Find maximum")
print("3. Search for a number")
print("4. Sort the list")
print("5. Quit")
user_input = int(input("Choose an option (1-5): "))

while user_input < 5:
    if user_input == 1:
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
        user_input = int(input("Choose an option (1-5): "))
    elif user_input == 2:
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
        user_input = int(input("Choose an option (1-5): "))
    elif user_input == 3:
        number_input = int(input("Please provide a number: "))
        for i in range(len(numbers)):
            if numbers[i] == number_input:
                print(i)
                break
            elif i == (len(numbers)-1):
                print("Not found")
        print("=== Number Cruncher ===")
        print("1. Find minimum")
        print("2. Find maximum")
        print("3. Search for a number")
        print("4. Sort the list")
        print("5. Quit")
        user_input = int(input("Choose an option (1-5): "))
    elif user_input == 4:
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print(numbers)
        print("=== Number Cruncher ===")
        print("1. Find minimum")
        print("2. Find maximum")
        print("3. Search for a number")
        print("4. Sort the list")
        print("5. Quit")
        user_input = int(input("Choose an option (1-5): "))

print("Goodbye.")

            
