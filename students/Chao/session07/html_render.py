#!/usr/bin/env python

class Element():
    tag = 'html'
    indent = ''

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, ind = ''):
        file_obj.write(ind + '<' + self.tag + '>\n')
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
        file_obj.write(ind + '<' + self.tag + '>')
        for each in self.content:
            newind = ind + self.indent
            if type(each) == str:
                file_obj.write(each)
            else:
                each.render(file_obj, newind)
        file_obj.write('</' + self.tag + '>\n')

class Title(OneLineTag):
    tag = 'title'
