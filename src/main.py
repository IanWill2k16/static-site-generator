from textnode import TextNode
from htmlnode import LeafNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)


main()