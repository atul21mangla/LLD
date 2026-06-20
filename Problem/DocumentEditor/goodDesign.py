from abc import ABC, abstractmethod
from typing import List

class DocumentElement(ABC):

    @abstractmethod
    def render(self) -> str:
        pass

# Concrete Implementation of DocumentElement class for text
class TextElement(DocumentElement):

    def __init__(self,text:str):
        self.__text = text

    def render(self)-> str:
        return self.__text
    
#  concrete Implementation of DocumentElement class for image
class ImageElement(DocumentElement):

    def __init__(self,image_path:str):
        self.__image_path = image_path

    def render(self):
        return "f[Image: {self.__image_path}]"
    

# Concrete implementation fro tab Space
class TabSpaceElement(DocumentElement):

    def render(self) -> str:
        return "\t"
    
class NewLineElement(DocumentElement):
    def render(self) -> str:
        return "\n"
    

# Document class responsible for holding a collection of Document Elements

class Document:

    def __init__(self):
        self.__documentElements = []

    def add_element(self,el:DocumentElement):
        self.__documentElements.append(el)

    def render(self)->str:
        result=""
        for el in self.__documentElements:
            result +=el.render()
        return result
    
# Persistence Abstraction

class Persistence(ABC):

    @abstractmethod
    def save(self,data:str):
        pass

# FileStorage implementation of Persistence
class FileStorage(Persistence):

    def save(self,data:str):
        try:
            with open("./Design Patterns/DocumentEditor/document.txt","w") as fs:
                fs.write(data)
            print("Document saved to document[FileStorage].txt")

        except IOError:
            print("Error: Unable to open File.")

class DBStorage(Persistence):

    def save(self,data:str):
        # Simulate saving to a database
        print("Document saved to database.")

    

#  DocumentEditor class responsible for managing the client interaction

class DocumentEditor:

    def __init__(self,document: Document, storage: Persistence):
        self.__document = document
        self.__storage = storage
        self.__rendered_document = ""
    
    def __invalidate_cache(self):
        self.__rendered_document = ""

    def add_text(self,text:str) -> None:
        self.__document.add_element(TextElement(text))
        self.__invalidate_cache()

    def add_image(self,image_path:str) -> None:
        self.__document.add_element(ImageElement(image_path))
        self.__invalidate_cache()

    def add_newLine(self)-> None:
        self.__document.add_element(NewLineElement())
        self.__invalidate_cache()

    def add_tabSpace(self) -> None:
        self.__document.add_element(TabSpaceElement())
        self.__invalidate_cache()

    def render_document(self):
        if not self.__rendered_document:
            self.__rendered_document = self.__document.render()

        return self.__rendered_document
    
    def save_document(self) -> None:
        self.__storage.save(self.render_document())


def main():
    document = Document()
    persistence = FileStorage()
    editor = DocumentEditor(document,persistence)

    editor.add_image("dog.jpg")
    editor.add_newLine()
    editor.add_text("Good Morning..")
    editor.add_tabSpace()
    editor.add_text("My name if Atul.....")
    editor.save_document()
    editor.add_text("New text")
    print(editor.render_document())


if __name__ == "__main__":
    main()