from history import History
from textEditor import TextEditor

def main():

    text_editor = TextEditor()
    history = History()

    text_editor.write("Hello, ")
    history.save(text_editor)

    text_editor.write("World!")
    history.save(text_editor)

    text_editor.write(" How are you?")
    history.save(text_editor)

    history.show_history()

    history.undo(text_editor)
    print(f"Text after undo: {text_editor.get_text()}")

if __name__ == "__main__":
    main()