import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestTextNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child", {"child_prop": "this is a child prop"})
        parent_node = ParentNode("div", [child_node], {"prop": "this is a prop"})
        self.assertEqual(parent_node.to_html(),
                          '<div prop="this is a prop"><span child_prop="this is a child prop">child</span></div>')

    def test_to_html_with_children_and_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"gc_prop": "this is a grandchild prop"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"prop": "this is a prop"})
        self.assertEqual(parent_node.to_html(),
                          '<div prop="this is a prop"><span><b gc_prop="this is a grandchild prop">grandchild</b></span></div>')

if __name__ == "__main__":
    unittest.main()