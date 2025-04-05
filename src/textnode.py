from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, TextType, url=None):
        self.text = text
        self.text_type = TextType
        self.url = url

    def __eq__(self, TextNode):
        if self == TextNode:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    