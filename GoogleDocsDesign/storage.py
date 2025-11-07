from abc import ABC, abstractmethod


class Storage(ABC):
    
    @abstractmethod
    def save(self,content:str):
        pass

class FileStorage(Storage):
    
    def save(self,content:str):
        with open("file.txt",mode="w") as f:
            f.write(content)
        print("stored in text !")

class DBStorage(Storage):
    
    def save(self,content:str):
        print("stored in db !")
    