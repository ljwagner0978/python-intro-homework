names = ["Alex", "George", "Mary", "Juan", "Andre", "Michelle", "Lisa", "Jennifer"]
x = input("Enter a name to search for: ")
index = 0
for name in names:
    if x == name:
       print(f'Found "{x}" at index {index}.')
       break
    elif index == len(names)-1:
        print(f'"{x}" was not found in the list.')
    index += 1
