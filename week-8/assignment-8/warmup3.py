try:
    with open("../data/missing.txt", "r") as f:
        print (line.strip() for line in f if line.strip())
except FileNotFoundError:
        print(f'Error: "missing.txt" was not found. Please check the file path and try again.')