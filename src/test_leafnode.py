import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1, node2)
    def test_child_error(self):
        with self.assertRaises(TypeError):
            LeafNode("p", "This is a paragraph of text.", "OtherNode", "https://www.google.com")
    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)
    def test_to_html2(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected)
    def test_to_html_lotsa_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        expected = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected)
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        expected = 'This is a paragraph of text.'
        self.assertEqual(node.to_html(), expected)
    

if __name__ == "__main__":
    unittest.main()