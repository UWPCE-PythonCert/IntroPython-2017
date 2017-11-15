"""
Kathryn Egan
"""


class Element:
    indent = '  '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def add_content(self, content):
        self.content.append(content)

    def render(self, file_obj):
        file_obj.write('<{}>'.format(self.tag))
        for c in self.content:
            file_obj.write(c)
        file_obj.write('</{}>'.format(self.tag))


class HTML(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class Paragraph(Element):
    tag = 'p'
