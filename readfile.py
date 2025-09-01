# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        print("File content:")
        for line in file:
            print(line.strip())  # strip() removes extra newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
