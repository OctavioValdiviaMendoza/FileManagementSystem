from fileInterface import FileInterface

class TextFile(FileInterface):
    def __init__(self, name, startIndex, size):
        self.name = name
        self.startIndex = startIndex
        self.size = size

    def get_name(self):
        return self.name
    def get_start_index(self):
        return self.startIndex
    def get_size(self):
        return self.size
    
    """
       WRITE TO FILE METHOD
    
       DELETE FILE METHOD
       
       READ FROM FILE METHOD
       
    """