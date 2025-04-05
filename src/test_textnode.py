import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_NoneUrl(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        node2 = TextNode("This is a text node", TextType.LINKS, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()