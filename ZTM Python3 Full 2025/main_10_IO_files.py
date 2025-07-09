# Working with files in Python

import os

# Opening a file in read mode
with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

    # Resetting the file pointer to the beginning, so it can be read again
    file.seek(0)
    content_readline = file.readline()  # Reads the first line of the file
    content_readlines = file.readlines()  # Reads all lines of the file into a list

    file.close()  # Closing the file after reading, though it's not necessary when using 'with' context manager

# Opening a file in write mode
# This will overwrite the file if it exists or create a new one if it doesn't
with open('my_file.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line Hi Hello World.\n")

# Opening a file in read mode and reading the content
with open('my_file.txt', 'r+') as file:
    text = file.write("hey hello\n")
    # This will write to the file and return the number of characters written
    print(text)
    content = file.readlines()  # Reads all lines of the file into a list
    print(content)

# Opening a file in append mode
with open('my_file.txt', 'a') as file:
    file.write("Appending a new line.\n")
    file.write("Appending another new line.\n")

# Opening a file in binary mode
with open('my_file.txt', 'rb') as file:
    binary_content = file.read()
    print(f"binary mode: {binary_content}")

# Opening a file in text mode
with open('my_file.txt', 'rt') as file:
    text_content = file.read()
    print(f"text mode: {text_content}")

# Files Paths - always use forward slashes (/) in file paths, and avoid using backslashes (\) as they can be interpreted as escape characters in Python strings.

# "_/_/main_10_IO_files.py" is a relative path, which means it is relative to the current working directory.
# "../../../" is a relative path that goes up three directories from the current directory.
# Relative paths are used to specify the location of a file or directory in relation to the current working directory.

# Absolute paths start from the root directory and specify the complete path to the file.


# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Get the absolute path of a file
file_path = os.path.abspath('my_file.txt')
print(f"Absolute File Path: {file_path}")

# Check if a file exists
file_exists = os.path.exists('my_file.txt')
print(f"Does the file exist? {file_exists}")

# List all files in the current directory
files_in_directory = os.listdir(current_directory)
print(f"Files in Current Directory: {files_in_directory}")

# Create a new directory
new_directory = os.path.join(current_directory, 'new_folder')
os.makedirs(new_directory, exist_ok=True)
print(f"New Directory Created: {new_directory}")

# Create a new file
with open(os.path.join(new_directory, 'new_file.txt'), 'w') as new_file:
    new_file.write("This is a new file in the new directory.\n")
    print("New file created in the new directory.")

# Remove a file
# if os.path.exists('my_file.txt'):
#     os.remove('my_file.txt')
#     print("File 'my_file.txt' has been removed.")

# # Remove a directory
# if os.path.exists(new_directory):
#     os.rmdir(new_directory)
#     print(f"Directory '{new_directory}' has been removed.")

# You can also use the `os.path.join()` function to create file paths that are compatible with the operating system you are using. This is especially useful when working with file paths in a cross-platform environment.

# Note: Always handle file operations with care, especially when deleting files or directories, to avoid accidental data loss.

# YEYY Good Job: Lewy :d go go go
