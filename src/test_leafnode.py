import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        leafnode = LeafNode("p", "Hello, world!")
        self.assertEqual(leafnode.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        leafnode = LeafNode('a', "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(leafnode.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_leaf_to_html_img(self):
        leafnode = LeafNode('img', "",
                            {"src": "https://www.google.com",
                            "alt": "this is a test value"})
        self.assertEqual(leafnode.to_html(), '<img src="https://www.google.com" alt="this is a test value"></img>')

    def test_eq(self):
        leafnode = LeafNode("p", "this is an HTML leafnode", {})
        leafnode2 = LeafNode("p", "this is an HTML leafnode", {})
        self.assertEqual(leafnode, leafnode2)

    def test_neq(self):
        leafnode = LeafNode("p", "this is an HTML leafnode", {})
        leafnode2 = LeafNode("h1", "this is a different HTML leafnode", {})
        self.assertNotEqual(leafnode, leafnode2)

    def test_props(self):
        leafnode = LeafNode("p", "this is an HTML leafnode with a prop", {"href": "https://www.google.com"})
        leafnode2 = LeafNode("p", "this is an HTML leafnode with a prop", {"href": "https://www.google.com"})
        self.assertEqual(leafnode, leafnode2)

    def test_props_to_html(self):
        leafnode = LeafNode("p", "this is an HTML leafnode with a prop",
                         {"href": "https://www.google.com",
                          "testKey": "this is a test value"})
        #print(leafnode.props_to_html())
        self.assertIsInstance(leafnode.props_to_html(), str)

if __name__ == "__main__":
    unittest.main()