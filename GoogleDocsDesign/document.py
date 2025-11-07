from typing import List
from document_element import DocumentElement

class Document:
    
    def __init__(self):
        self.doc_elements : List[DocumentElement] =[]
    
    def add_element(self,element:DocumentElement):
        self.doc_elements.append(element)
    
    def delete_element(self,element_id:str):
        for element in self.doc_elements:
            if element.get_id == element_id:
                self.doc_elements.remove(element)
                print("element with id : {element_id} deleted !")
                return
        print("element not found")
        
    def get_elements(self):
        return self.doc_elements

    def get_content(self):
        content = ""
        for element in self.doc_elements:
            content += element.get()
        return content
            