import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
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

    ##======================================================
    ##lEAF NODE TESTS:

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

    ##======================================================
    ##PARENT NODE TESTS:
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), 
                         "<div><span><b>grandchild</b></span></div>",)
        
    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child", {"child_prop": "this is a child prop"})
        parent_node = ParentNode("div", [child_node], {"prop": "this is a prop"})
        self.assertEqual(parent_node.to_html(),
                          '<div prop="this is a prop"><span child_prop="this is a child prop">child</span></div>')

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_to_html_with_children_and_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"gc_prop": "this is a grandchild prop"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"prop": "this is a prop"})
        self.assertEqual(parent_node.to_html(),
                          '<div prop="this is a prop">'
                          '<span><b gc_prop="this is a grandchild prop">grandchild</b></span></div>')

if __name__ == "__main__":
    unittest.main()