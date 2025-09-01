# Task 2: Write and Append Data to a File

# Step 1: Write data to file
user_input = input("Enter something to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
    print("Data successfully written to 'output.txt'")

# Step 2: Append data to the file
append_input = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")
    print("Data successfully appended to 'output.txt'")

# Step 3: Read and display final content
print("\nFinal file content:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
