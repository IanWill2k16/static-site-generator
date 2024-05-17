from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
    
        if self.text_type == "text_type_text":
            return LeafNode(None, self.text)
        elif self.text_type == "text_type_bold":
            return LeafNode("b", self.text)
        elif self.text_type == "text_type_italic":
            return LeafNode("i", self.text)
        elif self.text_type == "text_type_code":
            return LeafNode("code", self.text)
        elif self.text_type == "text_type_link":
            return LeafNode("a", self.text, {"href":self.url})
        elif self.text_type == "text_type_image":
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
        else:
            raise Exception("Text type not supported")
        
