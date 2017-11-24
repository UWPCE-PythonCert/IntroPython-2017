"""
Kathryn Egan
"""


class Element:
    indent = '    '
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrs = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, ind=0):
        file_out.write('{}<{}>\n'.format(ind * self.indent, self.tag))
        for c in self.content:
            try:
                c.render(file_out, ind + 1)
            except AttributeError:
                file_out.write('{}{}\n'.format((ind + 1) * self.indent, c))
        file_out.write('{}</{}>\n'.format(ind * self.indent, self.tag))

    # no indent
    # def render(self, file_out):
    #     file_out.write('<{}>'.format(self.tag))
    #     for c in self.content:
    #         try:
    #             c.render(file_out)
    #         except AttributeError:
    #             file_out.write(c)
    #     file_out.write('</{}>'.format(self.tag))


class OneLineTag(Element):
    def render(self, file_out, ind=0):
        file_out.write('{}<{}>'.format(ind * self.indent, self.tag))
        for c in self.content:
            try:
                c.render(file_out, ind + 1)
            except AttributeError:
                file_out.write(c)
        file_out.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, ind=0):
        file_out.write('{}<{} />\n'.format(ind * self.indent, self.tag))


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Head(Element):
    tag = 'head'


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'
