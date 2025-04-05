import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is an HTML node", [], {})
        node2 = HTMLNode("p", "this is an HTML node", [], {})
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("p", "this is an HTML node", [], {})
        node2 = HTMLNode("h1", "this is a different HTML node", [], {})
        self.assertNotEqual(node, node2)

    def test_children(self):
        node = HTMLNode("p", "this is an HTML node",
                         [HTMLNode("p", "this is a CHILD HTML node", [], {}),
                          HTMLNode("p", "this is a 2nd CHILD HTML node", [], {})], {})
        node2 = HTMLNode("p", "this is an HTML node",
                         [HTMLNode("p", "this is a CHILD HTML node", [], {}),
                          HTMLNode("p", "this is a 2nd CHILD HTML node", [], {})], {})
        self.assertEqual(node, node2)

    def test_diff_children(self):
        node = HTMLNode("p", "this is an HTML node",
                         [HTMLNode("p", "this is a CHILD HTML node", [], {}),
                          HTMLNode("p", "this is a 2nd CHILD HTML node", [], {})], {})
        node2 = HTMLNode("p", "this is an HTML node",
                         [HTMLNode("p", "this is a CHILD HTML node", [], {}),
                          HTMLNode("a", "this is a Different 2nd CHILD HTML node", [], {})], {})
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode("p", "this is an HTML node with a prop", [], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "this is an HTML node with a prop", [], {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "this is an HTML node with a prop", [],
                         {"href": "https://www.google.com",
                          "testKey": "this is a test value"})
        #print(node.props_to_html())
        self.assertIsInstance(node.props_to_html(), str)

if __name__ == "__main__":
    unittest.main()