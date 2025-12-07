from text_file import TextFile


class FolderSystem:
    current_folder = "/main"

    def __init__(self):
        self.folder = {}
    
    def create_folder(self, folder_name):
        if self.current_folder == "/main":
            if folder_name in self.folder:
                print(f"Folder {folder_name} already exists.")
            else:
                self.folder[folder_name] = {}
                print(f"Folder {folder_name} created.")
        else:
            current_obj = self.get_current_folder_object()
            
            if current_obj is None:
                print(f"Directory {self.current_folder} does not exist.")
                return
            
            if folder_name in current_obj:
                print(f"Folder {folder_name} already exists in {self.current_folder}.")
            else:
                current_obj[folder_name] = {}
                print(f"Folder {folder_name} created in {self.current_folder}.")


    def add_and_create_file(self, array):
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            print(f"Error: Cannot access {self.current_folder}")
            return
        
        file_name = input("Enter the name of the file to create: ").strip()
        if file_name in current_obj:
            print(f"File {file_name} already exists in {self.current_folder}.")
        else:
            new_file = TextFile(file_name)
            current_obj[file_name] = new_file
            print(f"File {file_name} created.")
            data = input("Enter the content of the file: ")
            new_file.write_file(data, array)

    def delete_file(self, array):
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            print(f"Error: Cannot access {self.current_folder}")
            return
        
        file_to_delete = input("Enter the name of the file to delete: ").strip()
        list_of_files = self.list_all_files_in_current_folder()
        if file_to_delete not in list_of_files:
            print("File does not exist in the current directory.")
            return
        
        file_obj = current_obj[file_to_delete]
        file_obj.delete_file(array)
        del current_obj[file_to_delete]

    #This method updates the current folder path based on user input
    def update_current_folder(self):
        all_folders = self.list_all_directories_in_current_folder()
        directory_to_open = input("Enter the name of the directory to open or '..' to go up one level: ").strip()
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

    def get_current_folder(self):
        return self.current_folder
    
    def get_current_folder_object(self):
        """Returns the dictionary object at the current folder location"""
        if self.current_folder == "/main":
            return self.folder
        else:
            path = self.current_folder.split("/")
            temp = self.folder
            # path is like ['', 'main', 'Test'], so we skip the empty string and 'main'
            for dir in path[2:]:
                if dir in temp:
                    temp = temp[dir]
                else:
                    return None
            return temp
    
    #This method list all files and directories in the current folder
    def list_all_contents_in_current_folder(self):
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            print(f"Error: Cannot access {self.current_folder}")
            return
        
        if len(current_obj) == 0:
            print("The current folder is empty.")
            return
        
        for key, value in current_obj.items():
            if isinstance(value, dict):
                print("Folder:", key)
            else:
                print("File:", key)

    

    #Creates an array that is used to by update_current_folder method to navigate through directories
    def list_all_directories_in_current_folder(self):
        all_folders = []
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            return []
        
        for key, value in current_obj.items():
            if isinstance(value, dict):
                all_folders.append(key)
        
        return all_folders

    def list_all_files_in_current_folder(self):
        all_files = []
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            return []
        
        for key, value in current_obj.items():
            if isinstance(value, TextFile):
                all_files.append(key)

        return all_files
    
    def delete_folder(self):
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            print(f"Error: Cannot access {self.current_folder}")
            return
        
        folder_to_delete = input("Enter the name of the folder to delete: ").strip()
        list_of_folders = self.list_all_directories_in_current_folder()
        if folder_to_delete not in list_of_folders:
            print("Folder does not exist in the current directory.")
            return
        
        del current_obj[folder_to_delete]
        print(f"Folder {folder_to_delete} deleted.")

    def read_file_from_current_folder(self, array):
        current_obj = self.get_current_folder_object()
        if current_obj is None:
            print(f"Error: Cannot access {self.current_folder}")
            return
        
        file_to_read = input("Enter the name of the file to read: ").strip()
        list_of_files = self.list_all_files_in_current_folder()
        if file_to_read not in list_of_files:
            print("File does not exist in the current directory.")
            return
        
        file_obj = current_obj[file_to_read]
        file_obj.read_file(array)


    def get_file(self, name):
        return self.folder.get(name, None)