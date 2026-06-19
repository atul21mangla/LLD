from textMemento import TextMemento

class TextEditor:

    def __init__(self):
        self.__text = ""

    def write(self,new_text):
        self.__text += new_text
    
    def get_text(self):
        return self.__text
    
    def save(self):
        print("Saving current state of text editor")
        return TextMemento(self.__text)
    
    def restore(self,textMemento:TextMemento):
        print("Restoring previous state of text editor")
        self.__text = textMemento.get_state()
    