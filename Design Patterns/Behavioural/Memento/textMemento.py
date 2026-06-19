class TextMemento:

    def __init__(self,state):
        self.__saved_state = state

    def get_state(self):
        return self.__saved_state