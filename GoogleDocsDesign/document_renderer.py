
from document import Document

class DocumentRenderer:
    
    
    def render(self,doc:Document):
        
        for element in doc.get_elements():
            element.render()