from abc import ABC, abstractmethod
from typing import List, Optional, Union
from enum import Enum
import json
from datetime import datetime

# ============ FORMATTING SUPPORT ============
class TextStyle:
    def __init__(self, bold: bool = False, italic: bool = False, 
                 underline: bool = False, color: Optional[str] = None,
                 font_size: int = 12, font_name: str = "Arial"):
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.color = color
        self.font_size = font_size
        self.font_name = font_name

# ============ DOCUMENT ELEMENTS ============
class DocumentElement(ABC):
    @abstractmethod
    def render(self, renderer: 'DocumentRenderer') -> str:
        pass
    
    @abstractmethod
    def clone(self) -> 'DocumentElement':
        pass

class TextElement(DocumentElement):
    def __init__(self, text: str, style: Optional[TextStyle] = None):
        self.text = text
        self.style = style or TextStyle()
        self.id = id(self)  # For undo/redo
    
    def render(self, renderer: 'DocumentRenderer') -> str:
        return renderer.render_text(self)
    
    def clone(self) -> 'TextElement':
        return TextElement(self.text, self.style)

class ImageElement(DocumentElement):
    def __init__(self, image_path: str, width: int = 100, height: int = 100, 
                 caption: str = ""):
        self.image_path = image_path
        self.width = width
        self.height = height
        self.caption = caption
    
    def render(self, renderer: 'DocumentRenderer') -> str:
        return renderer.render_image(self)
    
    def clone(self) -> 'ImageElement':
        return ImageElement(self.image_path, self.width, self.height, self.caption)

class TableElement(DocumentElement):
    def __init__(self, headers: List[str], rows: List[List[str]]):
        self.headers = headers
        self.rows = rows
    
    def render(self, renderer: 'DocumentRenderer') -> str:
        return renderer.render_table(self)
    
    def clone(self) -> 'TableElement':
        return TableElement(self.headers.copy(), [row.copy() for row in self.rows])

# ============ RENDERERS (Multiple Formats) ============
class DocumentRenderer(ABC):
    @abstractmethod
    def render_text(self, element: TextElement) -> str:
        pass
    
    @abstractmethod
    def render_image(self, element: ImageElement) -> str:
        pass
    
    @abstractmethod
    def render_table(self, element: TableElement) -> str:
        pass

class TextRenderer(DocumentRenderer):
    def render_text(self, element: TextElement) -> str:
        return element.text
    
    def render_image(self, element: ImageElement) -> str:
        return f"[Image: {element.image_path}]"
    
    def render_table(self, element: TableElement) -> str:
        # Simple text table rendering
        result = " | ".join(element.headers) + "\n"
        result += "-" * len(result) + "\n"
        for row in element.rows:
            result += " | ".join(row) + "\n"
        return result

class HTMLRenderer(DocumentRenderer):
    def render_text(self, element: TextElement) -> str:
        style = element.style
        text = element.text
        if style.bold:
            text = f"<b>{text}</b>"
        if style.italic:
            text = f"<i>{text}</i>"
        if style.underline:
            text = f"<u>{text}</u>"
        if style.color:
            text = f'<span style="color:{style.color}">{text}</span>'
        return text
    
    def render_image(self, element: ImageElement) -> str:
        return f'<img src="{element.image_path}" width="{element.width}" height="{element.height}" alt="{element.caption}"/>'
    
    def render_table(self, element: TableElement) -> str:
        result = "<table>\n<thead><tr>"
        for header in element.headers:
            result += f"<th>{header}</th>"
        result += "</tr></thead>\n<tbody>"
        for row in element.rows:
            result += "<tr>"
            for cell in row:
                result += f"<td>{cell}</td>"
            result += "</tr>\n"
        result += "</tbody></table>"
        return result

class MarkdownRenderer(DocumentRenderer):
    def render_text(self, element: TextElement) -> str:
        text = element.text
        if element.style.bold:
            text = f"**{text}**"
        if element.style.italic:
            text = f"*{text}*"
        return text
    
    def render_image(self, element: ImageElement) -> str:
        return f"![{element.caption}]({element.image_path})"
    
    def render_table(self, element: TableElement) -> str:
        # Simplified markdown table
        header = "| " + " | ".join(element.headers) + " |\n"
        separator = "|" + "|".join(["---"] * len(element.headers)) + "|\n"
        rows = ""
        for row in element.rows:
            rows += "| " + " | ".join(row) + " |\n"
        return header + separator + rows

# ============ DOCUMENT WITH UNDO/REDO ============
class Document:
    def __init__(self):
        self.elements: List[DocumentElement] = []
        self.undo_stack: List[List[DocumentElement]] = []
        self.redo_stack: List[List[DocumentElement]] = []
        self.version = 0
        self.max_history = 50
    
    def _save_state(self) -> None:
        """Save current state for undo/redo"""
        state = [element.clone() for element in self.elements]
        self.undo_stack.append(state)
        if len(self.undo_stack) > self.max_history:
            self.undo_stack.pop(0)
        self.redo_stack.clear()
        self.version += 1
    
    def add_element(self, element: DocumentElement) -> None:
        self._save_state()
        self.elements.append(element)
    
    def remove_element(self, index: int) -> None:
        if 0 <= index < len(self.elements):
            self._save_state()
            self.elements.pop(index)
    
    def insert_element(self, index: int, element: DocumentElement) -> None:
        if 0 <= index <= len(self.elements):
            self._save_state()
            self.elements.insert(index, element)
    
    def undo(self) -> bool:
        if not self.undo_stack:
            return False
        current_state = [element.clone() for element in self.elements]
        self.redo_stack.append(current_state)
        self.elements = self.undo_stack.pop()
        self.version += 1
        return True
    
    def redo(self) -> bool:
        if not self.redo_stack:
            return False
        current_state = [element.clone() for element in self.elements]
        self.undo_stack.append(current_state)
        self.elements = self.redo_stack.pop()
        self.version += 1
        return True
    
    def render(self, renderer: DocumentRenderer) -> str:
        result = ""
        for element in self.elements:
            result += element.render(renderer)
        return result

# ============ PERSISTENCE ============
class Persistence(ABC):
    @abstractmethod
    def save(self, data: str, format: str = "txt") -> None:
        pass
    
    @abstractmethod
    def load(self) -> str:
        pass

class FileStorage(Persistence):
    def __init__(self, filename: str = "document.txt"):
        self.filename = filename
    
    def save(self, data: str, format: str = "txt") -> None:
        try:
            filename = self.filename.replace(".txt", f".{format}")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"Document saved to {filename}")
        except IOError as e:
            raise RuntimeError(f"Failed to save document: {e}")
    
    def load(self) -> str:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        except IOError as e:
            raise RuntimeError(f"Failed to load document: {e}")

# ============ DOCUMENT EDITOR (Fluent Interface) ============
class DocumentEditor:
    def __init__(self, document: Document, storage: Persistence, 
                 renderer: DocumentRenderer = None):
        self.document = document
        self.storage = storage
        self.renderer = renderer or TextRenderer()
        self._dirty = False  # Track changes for smarter saving
    
    def add_text(self, text: str, style: Optional[TextStyle] = None) -> 'DocumentEditor':
        self.document.add_element(TextElement(text, style))
        self._dirty = True
        return self  # Fluent interface
    
    def add_image(self, path: str, width: int = 100, height: int = 100, 
                  caption: str = "") -> 'DocumentEditor':
        self.document.add_element(ImageElement(path, width, height, caption))
        self._dirty = True
        return self
    
    def add_table(self, headers: List[str], rows: List[List[str]]) -> 'DocumentEditor':
        self.document.add_element(TableElement(headers, rows))
        self._dirty = True
        return self
    
    def undo(self) -> 'DocumentEditor':
        if self.document.undo():
            self._dirty = True
        return self
    
    def redo(self) -> 'DocumentEditor':
        if self.document.redo():
            self._dirty = True
        return self
    
    def render(self, renderer: Optional[DocumentRenderer] = None) -> str:
        renderer = renderer or self.renderer
        return self.document.render(renderer)
    
    def save(self, format: str = "txt") -> None:
        """Save the document in specified format"""
        renderer_map = {
            "txt": TextRenderer(),
            "html": HTMLRenderer(),
            "md": MarkdownRenderer()
        }
        renderer = renderer_map.get(format, self.renderer)
        rendered_data = self.render(renderer)
        self.storage.save(rendered_data, format)
        self._dirty = False
    
    def export(self, format: str) -> str:
        """Export document as string without saving"""
        renderer_map = {
            "txt": TextRenderer(),
            "html": HTMLRenderer(),
            "md": MarkdownRenderer()
        }
        renderer = renderer_map.get(format, self.renderer)
        return self.render(renderer)

# ============ USAGE EXAMPLE ============
def main():
    # Create document
    doc = Document()
    storage = FileStorage("my_document.txt")
    
    # Create editor with fluent interface
    editor = DocumentEditor(doc, storage)
    
    # Build document with fluent API
    (editor
     .add_text("Hello, world!", TextStyle(bold=True, color="blue"))
     .add_text("\nThis is a ")
     .add_text("real-world", TextStyle(bold=True, italic=True))
     .add_text(" document editor example.")
     .add_text("\n\n")
     .add_table(
         headers=["Name", "Age", "City"],
         rows=[
             ["Alice", "30", "NYC"],
             ["Bob", "25", "LA"],
             ["Charlie", "35", "Chicago"]
         ]
     )
     .add_text("\n\n")
     .add_image("picture.jpg", width=400, height=300, caption="Sample Image")
    )
    
    # Render in different formats
    print("=== TEXT FORMAT ===")
    print(editor.render())
    
    print("\n=== HTML FORMAT ===")
    print(editor.export("html"))
    
    print("\n=== MARKDOWN FORMAT ===")
    print(editor.export("md"))
    
    # Save in different formats
    editor.save("txt")
    editor.save("html")
    editor.save("md")
    
    # Test undo/redo
    print("\n=== UNDO TEST ===")
    editor.add_text("\nNew text added")
    print("After adding:", editor.render())
    
    editor.undo()
    print("After undo:", editor.render())
    
    editor.redo()
    print("After redo:", editor.render())

if __name__ == "__main__":
    main()