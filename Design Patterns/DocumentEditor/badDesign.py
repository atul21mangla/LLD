class DocumentEditor:

    def __init__(self):
        self.__documentElements = []
        self.rendered_document = ""

    def add_text(self,text):
        """Adds a text as a plain string to the document."""
        self.__documentElements.append(text)

    def add_image(self,image_path):
        """Adds an image to the document."""
        self.__documentElements.append(image_path)

    def render_document(self) -> str:

        if not self.rendered_document:
            result = ""

            for el in self.__documentElements:
                if (len(el)>4 and (el[-4:] == ".jpg" or el[-4:] == ".png")):
                    result += f"[Image: {el}]\n"

                else:
                    result += f"{el}\n"

            self.rendered_document = result
        return self.rendered_document

            
    def save_to_file(self):
        """Saves document to file"""
        try:
            with open("./Design Patterns/DocumentEditor/document.txt","w") as file:
                file.write(self.render_document())
            print("Document saved to document.txt")

        except IOError:
            print("Error: Unable to open file for writing.")

    
def main():

    editor = DocumentEditor()

    editor.add_text("Hello World!")
    editor.add_image("picture.jpg")
    editor.add_text("Good Bye....")

    print(editor.render_document())

    editor.save_to_file()

if __name__ == "__main__":
        main()

        

        