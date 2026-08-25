try:
    with open("../data/missing.txt", "r"):
        print("File read successfully")
except FileNotFoundError:
        print(f'Error: "missing.txt" was not found. Please check the file path and try again.')