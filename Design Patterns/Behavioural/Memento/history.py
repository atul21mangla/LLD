from textMemento import TextMemento
from typing import List
from textEditor import TextEditor

class History:

    def __init__(self):
        self.__history:List[TextMemento] = []

    def save(self,text_editor:TextEditor):

        self.__history.append(text_editor.save())

    def undo(self, textEditor:TextEditor):
        if not self.__history:
            print("Nothing to undo")
        
        self.__history.pop()
        if not self.__history:
            textEditor.restore(TextMemento(""))

        else:
            textEditor.restore(self.__history[-1])

    def show_history(self):
        for i in range(len(self.__history)):
            print(f"{i+1} - {self.__history[i].get_state()}")
