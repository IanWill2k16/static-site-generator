class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        html_props = ""
        for k, v in self.props.items():
            html_props += f' {k}="{v}"'
        return html_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, props)
        self.children = None

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value
        
        return f'<{self.tag}>{self.value}</{self.tag}>'