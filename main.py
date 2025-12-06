from folder_system import FolderSystem

F1 = FolderSystem()

RamArray = [None] * 3000  # Simulated RAM array


def display_menu():
    print(f"\nCurrent location: {F1.get_current_folder()}")
    print("Please select an option:")
    print("1. List all contents in the current folder")
    print("2. Create a file")
    print("3. Read a file")
    print("4. Delete a file")
    print("5. Create a directory")
    print("6. Open a directory")
    print("7. Delete a directory")
    print("8. Exit\n")


print("Welcome to the File System. You are currently in the main directory.")
display_menu()
user_answer = input("Enter your choice: ")
potential_answer = ["1", "2", "3", "4", "5", "6", "7", "8"]

while user_answer not in potential_answer:
    user_answer = input("Invalid option. Please enter a number between 1-8: ")

while user_answer != "8":
    match user_answer:
        case "1":
            F1.list_all_contents_in_current_folder()
        case "2":
            F1.add_and_create_file(RamArray)
        case "3":
            F1.read_file_from_current_folder(RamArray)
        case "4":
            F1.delete_file(RamArray)
        case "5":
            folder_name = input("Enter the name of the folder to create: ")
            F1.create_folder(folder_name, F1.current_folder)
        case "6":
            F1.update_current_folder()
        case "7":
            F1.delete_folder()
    
    display_menu()
    user_answer = input("Enter your choice: ")
    while user_answer not in potential_answer:
        user_answer = input("Invalid option. Please enter a number between 1-8: ")

print("Thank you for using the File System. Goodbye!")


