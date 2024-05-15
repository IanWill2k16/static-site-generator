import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()
