import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)
    def test_eq2(self):
        node1 = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node1, node2)
    def test_noteq(self):
        node1 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertNotEqual(node1, node2)
    def test_noteq2(self):
        node1 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertNotEqual(node1, node2)
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        html = node.props_to_html()
        expectedOutcome = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(html, expectedOutcome)
    def test_props_to_html2(self):
        node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})
        html = node.props_to_html()
        expectedOutcome = 'href="https://www.google.com"'
        self.assertEqual(html, expectedOutcome)


if __name__ == "__main__":
    unittest.main()