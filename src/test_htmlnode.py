import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def leafnode_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        assert node.to_html() == "<p>This is a paragraph</p>"

    def leafnode_with_props(self):
        node = LeafNode("a", "Click me!", '{"href": "https://www.google.com"}')
        assert node.to_html() == '<a href="https://www.google.com>Click me!</a>'

    def leafnode_with_none(self):
        node = LeafNode(None, "Just some text")
        assert node.to_html() == "Just some text"

    def leafnode_missing_value(self):
        try:
            node = LeafNode("p", None)
        except ValueError as e:
            assert str(e) == "LeafNode must have a value"

    def test_leaf_node(self):
        leaf = LeafNode("span", "Hello, World!", None)
        expected_html = "<span>Hello, World!</span>"
        self.assertEqual(leaf.to_html(), expected_html)

    def test_parent_node_with_one_child(self):
        leaf = LeafNode("span", "Hello, World!", None)
        parent = ParentNode("div", children=[leaf])
        expected_html = "<div><span>Hello, World!</span></div>"
        self.assertEqual(parent.to_html(), expected_html)
    
    def test_parent_node_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold text", None),
            LeafNode(None, "Normal text", None),
            LeafNode("i", "italic text", None),
            LeafNode(None, "Normal text", None),
        ]
        parent = ParentNode("p", children=children)
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parent.to_html(), expected_html)
    
    def test_nested_parent_nodes(self):
        leaf1 = LeafNode("b", "Bold text", None)
        leaf2 = LeafNode("i", "Italic text", None)
        inner_parent = ParentNode("span", children=[leaf1, leaf2])
        outer_parent = ParentNode("div", children=[inner_parent, LeafNode(None, "Plain text", None)])
        expected_html = "<div><span><b>Bold text</b><i>Italic text</i></span>Plain text</div>"
        self.assertEqual(outer_parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()