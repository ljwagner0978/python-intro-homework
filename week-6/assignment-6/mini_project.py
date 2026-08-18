 def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    user_input = input("Choose an option (1-5): ")
    return(user_input)
    
def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if(min_number > number):
            min_number = number
    return(min_number)

def find_max(numbers):
    top_number = numbers[0]
    for number in numbers:
        if(top_number < number):
            top_number = number
    return(top_number)

def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return(i)
        elif i == (len(numbers)-1):
            return(-1)
        
def bubble_sort(numbers):
    numbers1 = numbers.copy()
    swapped = True
    swaps = 0
    j = 0
    while swapped:
        if j == (len(numbers1)-1):
            if swaps == 0:
                swapped = False
            j = 0
            swaps = 0
        if numbers1[j] > numbers1[j+1]:
            numbers1[j], numbers1[j+1] = numbers1[j+1], numbers1[j]
            swaps += 1
        j+=1
    return(numbers1)
    
def main():
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
    user_input = show_menu()
    while not user_input.isdigit() or int(user_input) <= 0 or int(user_input) >= 6:
        print("Invalid input, try again please.")
        user_input = show_menu()
    while int(user_input) != 5:
        if int(user_input) == 1:
            print(find_min(numbers))
            user_input = show_menu()
        elif int(user_input) == 2:
            print(find_max(numbers))
            user_input = show_menu()
        elif int(user_input) == 3:
            number_input = input("Please provide a number: ")
            while not number_input.isdigit():
                print("Invalid number inputted. Please try again")
                number_input = input("Please provide a number: ")
            z = search(numbers, int(number_input))
            if(z) == -1:
                print("Not found.")
            else:
                print(f"Found at index {z}")
            user_input = show_menu()
        elif int(user_input) == 4:
            print(bubble_sort(numbers))
            user_input = show_menu()
    if int(user_input) == 5:
        print("Goodbye.")
main()     
