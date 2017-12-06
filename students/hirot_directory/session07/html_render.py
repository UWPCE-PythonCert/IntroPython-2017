#!/usr/bin/env python

class Element():

    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs

    def append(self, content):
        self.content.append(content)


    def render(self, file_obj, cur_ind=""):
        open_tag = self.get_open_tag()
        close_tag = '{}</{}>'.format(cur_ind, self.tag)

        file_obj.write(cur_ind)
        file_obj.write(open_tag)
        file_obj.write("\n")
        for each in self.content:
            try:
                each.render(file_obj, cur_ind + self.indent)
            except AttributeError:
                file_obj.write(cur_ind + self.indent)
                file_obj.write(each)
            file_obj.write("\n")
        file_obj.write(close_tag)

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        for at, val in self.attributes.items():
            open_tag += ' {}="{}"'.format(at, val)
        open_tag += "> "
        return open_tag


class OneLineTag(Element):
    def render(self, file_obj, cur_ind=""):
        open_tag = self.get_open_tag()
        file_obj.write(cur_ind)
        file_obj.write(open_tag)
        for each in self.content:
            file_obj.write(each)
        file_obj.write(' </{}>'.format(self.tag))


class HTML(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    tag = 'selfClosingTag'

    def render(self, file_obj, cur_ind=""):
        file_obj.write(cur_ind)
        opening_tag = self.get_open_tag() 
        file_obj.write(opening_tag)
        file_obj.write('\n')

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        for at, val in self.attributes.items():
            open_tag += ' {}="{}"'.format(at, val)
        open_tag += "/> "
        return open_tag        


class Horizontal(SelfClosingTag):
    tag = 'hr '


class LineBreak(SelfClosingTag):
    tag = 'br '


class A(OneLineTag):
    tag = 'a'
    indent = '  '

    def __init__(self, link=None, content=None, **kwargs):
        kwargs['href'] = link # adding key to dict: d = {}, d['this'] = that. kwargs taking two attr.
        super().__init__(content, **kwargs)


class Li(Element):
    tag = 'li'


class Ul(Element):
    tag = 'ul'


class H(OneLineTag):
    tag = 'h'
    indent = '  '

    def __init__(self, header_level=None, content=None, **kwargs):
        kwargs[''] = header_level
        super().__init__(content, **kwargs)

    def render(self, file_obj, cur_ind=""):
        open_tag = self.get_open_tag()
        close_tag = self.get_close_tag()

        file_obj.write(cur_ind)
        file_obj.write(open_tag)
        # file_obj.write("\n")
        for each in self.content:
            try:
                each.render(file_obj, cur_ind + self.indent)
            except AttributeError:
                file_obj.write(cur_ind + self.indent)
                file_obj.write(each)
            # file_obj.write("\n")
        file_obj.write(close_tag)

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        for at, val in self.attributes.items():
            open_tag += '{}{}'.format(at, val)
        open_tag += ">"
        return open_tag

    def get_close_tag(self):
        close_tag = ' </{}'.format(self.tag)
        for at, val in self.attributes.items():
            close_tag +='{}{}'.format(at, val)
        close_tag += ">"
        return close_tag


class D(Element):
    tag = 'html'
    message = '!DOCTYPE'
    indent = '  '

    def render(self, file_obj, cur_ind=""):
        open_tag = '{}</{} {}>'.format(cur_ind, self.message, self.tag)

        file_obj.write(cur_ind)
        file_obj.write(open_tag)
        file_obj.write("\n")


class M(SelfClosingTag):
    # <meta charset="UTF-8" />
    tag = 'meta '
    indent = '  '

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)    



















