import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_none_match(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Blaaarrb", "italic", "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    def test_url_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    def test_name_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Blaaaarb", "bold")
        self.assertNotEqual(node, node2)
    def test_text_type_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node = TextNode("Hello, world!", "text_type_text")
        html_node = node.text_node_to_html_node()
        assert repr(html_node) == "HTMLNode(None, Hello, world!, None, None)"
    def test_text_to_html_bold(self):    
        node = TextNode("Bold text", "text_type_bold")
        html_node = node.text_node_to_html_node()
        assert repr(html_node) == "HTMLNode(b, Bold text, None, None)"
    def test_text_to_html_img(self):
        node = TextNode("Alt text", "text_type_image", "http://example.com/image.png")
        html_node = node.text_node_to_html_node()
        assert repr(html_node) == "HTMLNode(img, , None, {'src': 'http://example.com/image.png', 'alt': 'Alt text'})"
    def test_text_to_html_unsupported(self):
        try:
            node = TextNode("Unsupported", "text_type_unknown")
            html_node = node.text_node_to_html_node()
            assert False, "Exception not raised"
        except Exception as e:
            assert str(e) == "Text type not supported"


if __name__ == "__main__":
    unittest.main()
