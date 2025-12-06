#File System Operations Example
from text_file import TextFile

#Import a file object 
File1 = TextFile("example.txt", 0, 20)

print("Welcome to the File System you are currently in the main directory.")
user_answer = input("Please select an option:\n1. List files\n2. Create a file\n3. Read a file\n4. Delete a file\n5. List directories\n6. Create a directory\n7. Delete a directory\n8. Exit\n")
potential_answer = ["1", "2", "3", "4", "5", "6", "7", "8"]


while user_answer not in potential_answer:
    user_answer = input("Invalid option. Please enter a number between 1-8 based on the options provided above:\n")

"""
Switch case to handle user input for file system operations
"""


