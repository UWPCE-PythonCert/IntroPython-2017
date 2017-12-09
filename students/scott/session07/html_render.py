#!/usr/bin/env python3

class Element:
    tag = 'html'
    plus_indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        self.render_open_tag(file_out, cur_ind)
        for item in self.content:
            try:
                item.render(file_out, cur_ind + self.plus_indent)
            except AttributeError:
                file_out.write('\n' + cur_ind + self.plus_indent + str(item))
        file_out.write('\n')
        close_tag = '{}</{}>'.format(cur_ind, self.tag)
        file_out.write(close_tag)

    def render_open_tag(self, file_out, cur_ind=""):
        open_tag = self.get_open_tag()
        file_out.write('\n')
        file_out.write(cur_ind)
        file_out.write(open_tag)

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        open_tag += self.get_attr()
        open_tag += ">"
        return open_tag

    def get_attr(self):
        att = ""
        for att, val in self.attributes.items():
            att += ' {}="{}"'.format(att, val)
        return att

class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        self.render_open_tag(file_out, cur_ind)
        for item in self.content:
            file_out.write(' ' + str(item) + ' ')
        close_tag = '</{}>'.format(self.tag)
        file_out.write(close_tag)


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=""):
        self.render_open_tag(file_out, cur_ind)

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        open_tag += self.get_attr()
        open_tag += ' />'
        return open_tag

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link=None, content=None, **kwargs):
        Element.__init__(self, content, href=link, **kwargs)

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'

class Head(Element):
    tag = 'head'

class Title(OneLineTag):
    tag = 'title'