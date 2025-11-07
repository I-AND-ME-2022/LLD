from document import Document
from storage import Storage
from document_element import TextElement,ImageElement
from document_renderer import DocumentRenderer

class DocumentEditor:
    
    def __init__(self,doc:Document,db:Storage,renderer:DocumentRenderer):
        self.doc = doc
        self.db = db
        self.renderer = renderer
    
    def add_text(self,text:str):
        self.doc.add_element(TextElement(text))
    
    def add_image(self,path:str):
        self.doc.add_element(ImageElement(path))

    def save(self):
        self.db.save(self.doc.get_content())
    
    def render(self):        
        self.renderer.render(self.doc)
    