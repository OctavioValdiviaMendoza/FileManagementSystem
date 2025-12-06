from text_file import TextFile


class FolderSystem:
    current_folder = "/main"

    def __init__(self):
        self.folder = {}
    
    def create_folder(self, folder_name, current_folder):
        #If you want to create in main directory
        if current_folder == "/main":
            if folder_name in self.folder:
                print(f"Folder {folder_name} already exists.")
            else:
                self.folder[folder_name] = {}
                print(f"Folder {folder_name} created.")
        #If you want to create in a subdirectory
        else:
            path = current_folder.split("/") #Splitting the path to navigate ex. path = ["main", "sub1", "sub1's sub1"]
            temp = self.folder
            for dir in path[1:]: #Skipping "main" since it's the root
                if dir in temp:
                    temp = temp[dir]
                else:
                    print(f"Directory {dir} does not exist.")
                    return
            if folder_name in temp:
                print(f"Folder {folder_name} already exists in {current_folder}.")
            else:
                temp[folder_name] = {}
                print(f"Folder {folder_name} created in {current_folder}.")


    def add_and_create_file(self, array):
        if self.current_folder == "/main":
            file_name = input("Enter the name of the file to create: ")
            if file_name in self.folder:
                print(f"File {file_name} already exists.")
            else:
                new_file = TextFile(file_name)
                self.folder[file_name] = new_file
                print(f"File {file_name} created.")
                data = input("Enter the content of the file: ")
                new_file.write_file(data, array)
        else:
            path = self.current_folder.split("/")
            temp = self.folder
            for dir in path[1:]:
                if dir in temp:
                    temp = temp[dir]
                else:
                    print(f"Directory {dir} does not exist.")
                    return
            file_name = input("Enter the name of the file to create: ")
            if file_name in temp:
                print(f"File {file_name} already exists in {self.current_folder}.")
            else:
                new_file = TextFile(file_name)
                temp[file_name] = new_file
                print(f"File {file_name} created in {self.current_folder}.")
                data = input("Enter the content of the file: ")
                new_file.write_file(data, array)

    def delete_file(self, array):
        file_to_delete = input("Enter the name of the file to delete: ")
        list_of_files = self.list_all_files_in_current_folder()
        if file_to_delete not in list_of_files:
            print("File does not exist in the current directory.")
            return
        else:
            if self.current_folder == "/main":
                file_obj = self.folder[file_to_delete]
                file_obj.delete_file(array)
                del self.folder[file_to_delete]
            else:
                path = self.current_folder.split("/")
                temp = self.folder
                for dir in path[1:]:
                    if dir in temp:
                        temp = temp[dir]
                    else:
                        print(f"Directory {dir} does not exist.")
                        return
                file_obj = temp[file_to_delete]
                file_obj.delete_file(array)
                del temp[file_to_delete]

    #This method updates the current folder path based on user input
    def update_current_folder(self):
        all_folders = self.list_all_directories_in_current_folder()
        directory_to_open = input("Enter the name of the directory to open or '..' to go up one level: ")
        if directory_to_open not in all_folders and directory_to_open != "..":
            print("Directory does not exist. Please try again.")
            return
        if directory_to_open == "..":
            if self.current_folder != "/main":
                self.current_folder = "/".join(self.current_folder.split("/")[:-1])
            else:
                print("You are already in the main directory.")
        else:
            self.current_folder += "/" + directory_to_open
            path = self.current_folder.split("/")
            temp = self.folder
            for dir in path[1:]:
                if dir in temp:
                    temp = temp[dir]
                else:
                    print(f"Directory {dir} does not exist.")
                    return

    def get_current_folder(self):
        return self.current_folder
    
    #This method list all files and directories in the current folder
    def list_all_contents_in_current_folder(self):
        if self.current_folder == "/main":
            for key in self.folder.keys():
                if isinstance(self.folder[key], dict):
                    print("Folder:", key)
                else:
                    print("File:", key)
        else:
            path = self.current_folder.split("/")
            temp = self.folder
            for dir in path[1:]:
                if dir in temp:
                    temp = temp[dir]
                else:
                    print(f"Directory {dir} does not exist.")
                    return
            for key in temp.keys():
                if isinstance(temp[key], dict):
                    print("Folder:", key)
                else:
                    print("File:", key)

    

    #Creates an array that is used to by update_current_folder method to navigate through directories
    def list_all_directories_in_current_folder(self):
        all_folders = []
        if self.current_folder == "/main":
            for key in self.folder.keys():
                if isinstance(self.folder[key], dict):
                    all_folders.append(key)
        else:
            path = self.current_folder.split("/")
            temp = self.folder
            for dir in path[1:]:
                if dir in temp:
                    temp = temp[dir]
                else:
                    print(f"Directory {dir} does not exist.")
                    return
            for key in temp.keys():
                if isinstance(temp[key], dict):
                    all_folders.append(key)
        
        return all_folders

    def list_all_files_in_current_folder(self):
        all_files = []
        if self.current_folder == "/main":
            for key in self.folder.keys():
                if isinstance(self.folder[key], TextFile):
                    all_files.append(key)
        else:
            path = self.current_folder.split("/")
            temp = self.folder
            for dir in path[1:]:
                if dir in temp:
                    temp = temp[dir]
                else:
                    print(f"Directory {dir} does not exist.")
                    return
            for key in temp.keys():
                if isinstance(temp[key], TextFile):
                    all_files.append(key)

        return all_files
    
    def delete_folder(self):
        folder_to_delete = input("Enter the name of the folder to delete: ")
        list_of_folders = self.list_all_directories_in_current_folder()
        if folder_to_delete not in list_of_folders:
            print("Folder does not exist in the current directory.")
            return
        else:
            if self.current_folder == "/main":
                del self.folder[folder_to_delete]
                print(f"Folder {folder_to_delete} deleted.")
            else:
                path = self.current_folder.split("/")
                temp = self.folder
                for dir in path[1:]:
                    if dir in temp:
                        temp = temp[dir]
                    else:
                        print(f"Directory {dir} does not exist.")
                        return
                del temp[folder_to_delete]
                print(f"Folder {folder_to_delete} deleted.")

    def read_file_from_current_folder(self, array):
        file_to_read = input("Enter the name of the file to read: ")
        list_of_files = self.list_all_files_in_current_folder()
        if file_to_read not in list_of_files:
            print("File does not exist in the current directory.")
            return
        else:
            if self.current_folder == "/main":
                file_obj = self.folder[file_to_read]
                file_obj.read_file(array)
            else:
                path = self.current_folder.split("/")
                temp = self.folder
                for dir in path[1:]:
                    if dir in temp:
                        temp = temp[dir]
                    else:
                        print(f"Directory {dir} does not exist.")
                        return
                file_obj = temp[file_to_read]
                file_obj.read_file(array)


    def get_file(self, name):
        return self.folder.get(name, None)