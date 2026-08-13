names = ["Alex", "George", "Mary", "Juan", "Andre", "Michelle", "Lisa", "Jennifer"]
x = input("Enter a name to search for: ")
index = 0
match_found = False
for name in names:
    if x == name:
       print(f'Found "{x}" at index {index}.')
       match_found = True
       break
    index += 1
if match_found == False:
    print(f'"{x}" was not found in the list.')
