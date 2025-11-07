from abc import ABC, abstractmethod


class DocumentElement(ABC):
    
    @abstractmethod
    def render():
        pass

class TextElement(DocumentElement):
    def __init__(self,content:str):
        self.content = content
    
    def render(self):
        print(self.content)
    
    def get(self):
        return self.content

class ImageElement(DocumentElement):
    def __init__(self,path:str):
        self.path = path
    
    def render(self):
        print(f"[image: {self.path}]")
    
    def get(self):
        return self.path