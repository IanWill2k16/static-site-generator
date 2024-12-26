import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.CODE, None)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.yahoo.com")
        self.assertNotEqual(node, node2)
    def test_text_node_to_html_node_text_only(self):
        node = TextNode("This is purely text", TextType.TEXT)
        result = text_node_to_html_node(node)
        node2 = LeafNode(None, "This is purely text")
        self.assertEqual(result, node2)
    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        result = text_node_to_html_node(node)
        node2 = HTMLNode("a", "This is a text node", None, {"href": "https://www.google.com"})
        self.assertEqual(result, node2)
    def test_text_node_to_html_node_image(self):
        node = TextNode("This is alt text", TextType.IMAGE, "https://www.google.com")
        result = text_node_to_html_node(node)
        node2 = HTMLNode("img", "", None, {"src": "https://www.google.com", "alt": "This is alt text"})
        self.assertEqual(result, node2)


if __name__ == "__main__":
    unittest.main()