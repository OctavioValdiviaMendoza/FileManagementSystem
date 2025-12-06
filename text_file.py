from fileInterface import FileInterface
import time

class TextFile(FileInterface):
    def __init__(self, name, startIndex, size):
        self.name = name
        self.startIndex = 0
        self.size = 0

    def get_name(self):
        return self.name
    def get_start_index(self):
        return self.startIndex
    def get_size(self):
        return self.size
    
    def write_file(self, data, array):
        temp = 0
        data_length = len(data)
        self.size = data_length
        can_write = True
        if self.startIndex + data_length > len(array):
            print("Error: Not enough space to write the file.")
            can_write = False

        for i in range(0, len(array)):
            count = 0 #count empty spaces to see if we can write
            if array[i] is None:
                count += 1
            if count == data_length:
                self.startIndex = i
                break
            if i == len(array) - 1 and count < data_length:
                print("Error: Not enough contiguous space to write the file.")
                can_write = False
            if array[i] is not None:
                count = 0
        
            
    
    def delete_file(self, array):
        print("Deleting", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()  # for newline after loading dots

        for i in range(self.startIndex, self.startIndex + self.size):
            array[i] = None
        print(f"File {self.name} is now deleted.")
    
    """
       WRITE TO FILE METHOD
    
       DELETE FILE METHOD
       
       READ FROM FILE METHOD
       
    """