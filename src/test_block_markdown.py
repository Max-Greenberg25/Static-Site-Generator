import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node

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

class TestBlockToBlock(unittest.TestCase):
    
    def test_Heading(self):
        block = "### This is a heading"
        self.assertEqual(
            block_to_block_type(block), BlockType.HEADING
        )
    def test_code(self):
        block = "```\nThis is some code\n```"
        self.assertEqual(
            block_to_block_type(block), BlockType.CODE
        )
    def test_quote(self):
        block = (
            "> This is a quote line \n> this is a secont quote line"
        )
        self.assertEqual(
            block_to_block_type(block), BlockType.QUOTE
        )
    def test_uolist(self):
        block = "- this is a uolist\n- this is the second line of a list\n- and third"
        self.assertEqual(
            block_to_block_type(block), BlockType.UOLIST
        )
    def test_olist(self):
        block = "1. this is a uolist\n2. this is the second line of a list\n3. and third"
        self.assertEqual(
            block_to_block_type(block), BlockType.OLIST
        )
    def test_PARAGRAPH(self):
        block = "This is just a paragraph\nWith two lines."
        self.assertEqual(
            block_to_block_type(block), BlockType.PARAGRAPH
        )

####################################
    #TESTING NOT EQUAL:
####################################

    def test_Heading_neq(self):
        block = " ### This is aN incorrect heading"
        self.assertNotEqual(
            block_to_block_type(block), BlockType.HEADING
        )
    def test_code_neq(self):
        block = "```\nThis is some wrongly formatted code ``"
        self.assertNotEqual(
            block_to_block_type(block), BlockType.CODE
        )
    def test_quote_neq(self):
        block = (
            "> This is a quote line \n this is a secont quote line"
        )
        self.assertNotEqual(
            block_to_block_type(block), BlockType.QUOTE
        )
    def test_quote_neq2(self):
        block = (
            " > This is a quote line \n> this is a secont quote line"
        )
        self.assertNotEqual(
            block_to_block_type(block), BlockType.QUOTE
        )
    def test_uolist_neq(self):
        block = "-this is a uolist\n this is the second line of a list\n- and third"
        self.assertNotEqual(
            block_to_block_type(block), BlockType.UOLIST
        )
    def test_olist_neq(self):
        block = "1. this is a uolist\n2 this is the second line of a list\n3. and third"
        self.assertNotEqual(
            block_to_block_type(block), BlockType.OLIST
        )
    def test_paragraph_neq(self):
        block = "# This is just a paragraph\nWith two lines."
        self.assertNotEqual(
            block_to_block_type(block), BlockType.PARAGRAPH
        )


class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()