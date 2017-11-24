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
        file_out.write(self.open_tag(ind))
        file_out.write('\n')
        for c in self.content:
            try:
                c.render(file_out, ind + 1)
            except AttributeError:
                file_out.write('{}{}\n'.format((ind + 1) * self.indent, c))
        file_out.write(self.close_tag(ind))
        file_out.write('\n')

    def open_tag(self, ind, selfclosing=False):
        attrs = ''.join([
            ' {}="{}"'.format(key, self.attrs[key])
            for key in sorted(self.attrs)])
        close = ' /' if selfclosing else ''
        tag = '{}<{}{}{}>'.format(ind * self.indent, self.tag, attrs, close)
        return tag

    def close_tag(self, ind):
        tag = '{}</{}>'.format(ind * self.indent, self.tag)
        return tag


class OneLineTag(Element):
    def render(self, file_out, ind=0):
        file_out.write(self.open_tag(ind))
        for c in self.content:
            file_out.write(c)
        file_out.write(self.close_tag(0))
        file_out.write('\n')


class SelfClosingTag(Element):
    def render(self, file_out, ind=0):
        file_out.write(self.open_tag(ind, selfclosing=True))
        file_out.write('\n')


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)


class Title(OneLineTag):
    tag = 'title'


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


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Header(OneLineTag):

    def __init__(self, level, content):
        self.tag = 'h' + str(level)
        Element.__init__(self, content)
