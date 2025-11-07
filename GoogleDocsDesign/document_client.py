from document_editor import DocumentEditor
from document_renderer import DocumentRenderer
from storage import FileStorage
from document import Document
class DocumentEditorDemo:
    
    @staticmethod
    def main():
        
        doc = Document()
        db = FileStorage()
        renderer = DocumentRenderer()
        
        doc_editor = DocumentEditor(doc,db,renderer)
        doc_editor.add_text("hi aarti")
        doc_editor.add_image("image.png")
        doc_editor.render()
        doc_editor.save()

DocumentEditorDemo.main()
        
        
        
    