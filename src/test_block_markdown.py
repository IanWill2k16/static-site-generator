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
        block2 = block_to_block_type('```\nThis is a code block\n```')
        block3 = block_to_block_type('>This is a quote\n> block')
        block4 = block_to_block_type('* This is an \n* unordered list')
        block5 = block_to_block_type('1. This is an \n2. ordered list')
        block6 = block_to_block_type('This is a normal paragraph')
        self.assertEqual(block1, block_type_heading)
        self.assertEqual(block2, block_type_code)
        self.assertEqual(block3, block_type_quote)
        self.assertEqual(block4, block_type_ulist)
        self.assertEqual(block5, block_type_olist)
        self.assertEqual(block6, block_type_paragraph)

    def test_markdown_to_html_node(self):
        markdown = """
#### This is an h4 heading

This is a 
paragraph
of lots of lines

- This is a list
- Of things
* We're splitting
* it up

1. This is
2. an ordered
3. List

> This is a
> block quote
> with multiple
> lines

```
This is a
code block
with multiple
lines
```
"""
        result = markdown_to_html_node(markdown)
        print(result)
        expected = "?"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()