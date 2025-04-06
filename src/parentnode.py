from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def __repr__(self):
        props = self.props_to_html()
        return f"LeafNode({self.tag}, {self.children}, {props})"

    def to_html(self):
        if self.tag == None:
            raise ValueError("LeafNode has no tag")
        if self.children == None:
            raise ValueError("LeafNode has no children")
        if not self.props:
            #The Lame Way:
            result = ""
            for child in self.children:
                result += child.to_html()

            return f'<{self.tag}>{result}</{self.tag}>'
        else:
            result = ""
            for child in self.children:
                result += child.to_html()
            return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'
            
            #(The cool way): return f'<{self.tag}>{"".join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>'
