from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type.value == "text":
        return LeafNode(None, text_node.text)
    if text_node.text_type.value == "bold":
        return LeafNode("b", text_node.text)
    if text_node.text_type.value == "italic":
        return LeafNode("i", text_node.text)
    if text_node.text_type.value == "code":
        return LeafNode("code", text_node.text)
    if text_node.text_type.value == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type.value == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f'Invalid text type: {text_node.text_type}')
    
    # def text(self):
    #     return self.text