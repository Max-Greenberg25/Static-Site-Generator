class HTMLNode():
    def __init__(self, tag=None, TextNode=None, children=None, props=None):
        self.tag = tag
        self.value = TextNode
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
             return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    def __eq__(self, HTMLNode):
        if (self.tag == HTMLNode.tag and 
            self.value == HTMLNode.value and
            self.children == HTMLNode.children and
            self.props == HTMLNode.props):
                return True
        return False

    def __repr__(self):
        props = self.props_to_html()
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {props})"