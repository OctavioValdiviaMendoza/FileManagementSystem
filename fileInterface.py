from abc import ABC, abstractmethod

class FileInterface(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_start_index(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass





