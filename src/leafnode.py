from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def __repr__(self):
        props = self.props_to_html()
        return f"LeafNode({self.tag}, {self.value}, {props})"

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode has no value")
        if self.tag == None:
            return self.value
        if self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'