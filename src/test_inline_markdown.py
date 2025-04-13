import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes
)

from textnode import TextNode, TextType



class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode("This is a **bolded** word and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode("This is a **bolded word** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    def test_delim_italic(self):
        node = TextNode("This is a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
        
class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_images(self):
            matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

class TestSplitLinksAndImages(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [   TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ],
            new_nodes)
        
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![picture](https://i.imgur.com/zjjcJKZ.png) and some Text", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [   TextNode("This is text with an ", TextType.TEXT),
                TextNode("picture", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some Text", TextType.TEXT),
                ],
            new_nodes)
        
    def test_split_images_two_nodes(self):
        node = TextNode("This is text with an ![picture](https://i.imgur.com/zjjcJKZ.png) and some Text", TextType.TEXT)
        node1 = TextNode("This is also an ![image](https://wildlife.utah.gov/news_photos/2020-05-27-mule-deer-fawn.jpg)", TextType.TEXT)
        new_nodes = split_nodes_images([node, node1])
        self.assertListEqual(
            [   TextNode("This is text with an ", TextType.TEXT),
                TextNode("picture", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some Text", TextType.TEXT),
                TextNode("This is also an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://wildlife.utah.gov/news_photos/2020-05-27-mule-deer-fawn.jpg"),
                ],
            new_nodes)
        
    def test_split_image_no_image(self):
        node = TextNode("This is just some text", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [   
                TextNode("This is just some text", TextType.TEXT),
                ],
            new_nodes)
        
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [   TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                ],
            new_nodes)
        
    def test_split_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and some Text", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [   TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some Text", TextType.TEXT),
                ],
            new_nodes)
        
    def test_split_links_two_nodes(self):
        node = TextNode("This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and some Text", TextType.TEXT)
        node1 = TextNode("This is also an [link](https://wildlife.utah.gov/news_photos/2020-05-27-mule-deer-fawn.jpg)", TextType.TEXT)
        new_nodes = split_nodes_links([node, node1])
        self.assertListEqual(
            [   TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some Text", TextType.TEXT),
                TextNode("This is also an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://wildlife.utah.gov/news_photos/2020-05-27-mule-deer-fawn.jpg"),
                ],
            new_nodes)
        
    def test_split_link_no_link(self):
        node = TextNode("This is just some text", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [   
                TextNode("This is just some text", TextType.TEXT),
                ],
            new_nodes)
        
class TestTextToTextNode(unittest.TestCase):
    def test_example(self):
        text = ("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),  
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()