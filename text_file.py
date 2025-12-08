from fileInterface import FileInterface
import time
import textwrap
from typing import override

class TextFile(FileInterface):

    def __init__(self, name):
        self.name = name
        self.startIndex = 0
        self.size = 0

    @override
    def get_name(self):
        return self.name
    
    @override
    def get_start_index(self):
        return self.startIndex
    
    @override
    def get_size(self):
        return self.size
    
    def write_file(self, data, array):
        data_length = len(data)
        self.size = data_length
        if self.startIndex + data_length > len(array):
            print()
            print("=" * 45)
            print("Error: Not enough space to write the file.")
            print("=" * 45)
            return            
        count = 0 #count empty spaces to see if we can write
        for i in range(0, len(array)):
            if array[i] is None:
                count += 1
            if count == data_length:
                self.startIndex = i - data_length + 1
                for j in range(data_length):
                    array[self.startIndex + j] = data[j]
                break
            if i == len(array) - 1 and count != data_length:
                print()
                print("=" * 45)
                print("Error: Not enough space to write the file...")
                print("=" * 45)
            if array[i] is not None:
                count = 0
        
            
    @override
    def delete_file(self, array):
        print("Deleting", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()  # for newline after loading dots

        for i in range(self.startIndex, self.startIndex + self.size):
            array[i] = None
        print()
        print("=" * 45)
        print(f"File {self.name} is now deleted.")
        print("=" * 45)

    @override
    def read_file (self, array):
        string = array[self.startIndex:self.startIndex + self.size]
        try:
            if string[0] is None:
                raise ValueError("has been deleted or is empty")
        except ValueError as e:
            print(e)
            return
        result = "".join(string)
        print("Reading", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        width = 45
        WrappedText = textwrap.wrap(result, width=width)
        print()
        print()
        print(f"File '{self.name}':")
        print("=" * (width + 5))
        for line in WrappedText:
            print("=", line.ljust(width), "=")
        print("=" * (width + 5))