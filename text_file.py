from fileInterface import FileInterface
import time

class TextFile(FileInterface):

    name = ""
    startIndex = 0
    size = 0

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    def get_start_index(self):
        return self.startIndex
    def get_size(self):
        return self.size
    
    def write_file(self, data, array):
        data_length = len(data)
        self.size = data_length
        print(self.size)
        if self.startIndex + data_length > len(array):
            print("Error: Not enough space to write the file.")
            return            
        count = 0 #count empty spaces to see if we can write
        for i in range(0, len(array)):
            if array[i] is None:
                count += 1
            if count == data_length:
                self.startIndex = i - data_length 
                for j in range(data_length):
                    array[self.startIndex + j] = data[j]
                break
            if i == len(array) - 1 and count != data_length:
                print("Error: Not enough space to write the file...")
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

    def read_file (self, array):
        string = array[self.startIndex:self.startIndex + self.size]
        #result = "".join(string)
        print("Reading", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()
        print(string)