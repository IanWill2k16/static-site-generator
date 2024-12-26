import unittest

from page_generation import extract_title

class TestPageGeneration(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is my titular title!"
        title = extract_title(markdown)
        self.assertEqual(title, "This is my titular title!")
    def test_extract_title_2(self):
        markdown = "### This is my titular title!"
        with self.assertRaises(ValueError):
            extract_title(markdown)
    def test_extract_title_3(self):
        markdown = """
### This is my titular title!
# But this is the true title
"""
        title = extract_title(markdown)
        self.assertEqual(title, "But this is the true title")