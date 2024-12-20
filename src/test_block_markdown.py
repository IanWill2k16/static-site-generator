import unittest

from textnode import *
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
 # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(markdown)
        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(result, expected)

    def test_block_to_block_type(self):
        block1 = block_to_block_type('#### This is a heading')
        block2 = block_to_block_type('```This is a code block```')
        block3 = block_to_block_type('>This is a quote block')
        block4 = block_to_block_type('* This is an unordered list')
        block5 = block_to_block_type('. This is an ordered list')
        block6 = block_to_block_type('This is a normal paragraph')
        self.assertEqual(block1, "heading")
        self.assertEqual(block2, "code")
        self.assertEqual(block3, "quote")
        self.assertEqual(block4, "unordered list")
        self.assertEqual(block5, "ordered list")
        self.assertEqual(block6, "paragraph")


if __name__ == "__main__":
    unittest.main()