import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_google(self):
        actual = HTMLNode("p", "Google", None, {"href": "https://www.google.com", "target": "_blank"})
        expected =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual.props_to_html(), expected)
    
    def test_props_yahoo(self):    
        actual = HTMLNode("p", "Yahoo", None, {"href": "https://www.yahoo.com", "target": "_blank"})
        expected =  ' href="https://www.yahoo.com" target="_blank"'
        self.assertEqual(actual.props_to_html(), expected)

    def test_props_none(self):    
        actual = HTMLNode("p", "Yahoo")
        expected =  ''
        self.assertEqual(actual.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()