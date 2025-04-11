import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdownSplitter(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """This is **italic word**

This is another paragraph with `code,` and _italics_ here

This is it"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **italic word**",
                "This is another paragraph with `code,` and _italics_ here",
                "This is it",
            ],
        )

if __name__ == "__main__":
    unittest.main()