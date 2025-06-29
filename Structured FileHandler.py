import os

# 1. Create and write to a file
def create_and_write_file(filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Welcome to the world of Python!\n")
        file.write("This file was created using Python code.\n")
    print(f"File '{filename}' has been created and written to.")

# 2. Read the entire file content
def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    else:
        print("File does not exist.")

# 3. Append text to the file
def append_to_file(filename, text):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print(f"Text has been appended to '{filename}'.")

# 4. Read file line by line
def read_file_by_line(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            print("\nReading file line by line:")
            for line in file:
                print("Line:", line.strip())
    else:
        print("File does not exist.")

# 5. Delete the file (optional)
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' has been deleted.")
    else:
        print("File does not exist, cannot delete.")

#  Run all file operations
file_name = "my_python_file.txt"

create_and_write_file(file_name)
read_file(file_name)
append_to_file(file_name, "This line was added later.")
read_file_by_line(file_name)

# Uncomment the next line to delete the file:
# delete_file(file_name)
