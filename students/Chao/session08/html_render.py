#!/usr/bin/env python

class Element():
    tag = 'html'
    indent = ''

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, ind = ''):
        file_obj.write(ind + '<' + self.tag)
        for at, val in self.attributes.items():
            file_obj.write(' ' + at + '="' + val + '"')
        file_obj.write('>\n')
        for each in self.content:
            newind = ind + self.indent
            if type(each) == str:
                file_obj.write(newind + each + '\n')
            else:
                each.render(file_obj, newind)
        file_obj.write(ind + '</' + self.tag + '>\n')

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'

    # 'special' reder method for html only - set DOCTYPE, indent, and no indent before tags
    def render(self, file_obj, ind = ''):
        Element.indent = ind
        file_obj.write('<!DOCTYPE html>\n' + '<' + self.tag + '>\n')
        for each in self.content:
            if type(each) == str:
                file_obj.write(ind + each + '\n')
            else:
                each.render(file_obj, ind)
        file_obj.write('</' + self.tag + '>\n')

class Head(Element):
    tag = 'head'

class OneLineTag(Element):

    def render(self, file_obj, ind = ''):
        file_obj.write(ind + '<' + self.tag)
        for at, val in self.attributes.items():
            file_obj.write(' ' + at + '="' + val + '"')
        file_obj.write('>')
        for each in self.content:
            newind = ind + self.indent
            if type(each) == str:
                file_obj.write(each)
            else:
                each.render(file_obj, newind)
        file_obj.write('</' + self.tag + '>\n')

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):

    def render(self, file_obj, ind = ''):
        file_obj.write(ind + '<' + self.tag)
        for at, val in self.attributes.items():
            file_obj.write(' ' + at + '="' + val + '"')
        file_obj.write(' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, url, content):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = {'href': url}

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, h, content, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.tag += str(h)
        self.attributes = kwargs

class Meta(SelfClosingTag):
    tag = 'meta'
    