#!/usr/bin/env python


class Element():

    tag = 'html'
    ind = '  ' # indent = '   '

    def __init__(self, content=None):

        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):

        self.content.append(content)

    def render(self, file_obj, ind=""):
        file_obj.write(ind)
        opening_tag = ('<' + self.tag + '>')  
        file_obj.write(opening_tag)
        file_obj.write('\n')

        for each in self.content:  
            try:
                file_obj.write(ind) # self.indent
                file_obj.write(ind)
                file_obj.write(each)
            except TypeError:
                each.render(file_obj)

        file_obj.write('\n')

        file_obj.write(ind)
        closing_tag = ('</' + self.tag + '>')
        file_obj.write(closing_tag)




class HTML(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_obj):
        opening_tag = ('<' + self.tag + '>') 
        file_obj.write(opening_tag)

        for each in self.content:  
            try:
                file_obj.write(each)
            except TypeError:
                each.render(file_obj)

        closing_tag = ('</' + self.tag + '>')  
        file_obj.write(closing_tag)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    tag = 'selfClosingTag'

    def render(self, file_obj, ind=""):
        file_obj.write(ind)
        opening_tag = ('<' + self.tag + '>')  
        file_obj.write(opening_tag)
        file_obj.write('\n')


class Horizontal(SelfClosingTag):
    tag = 'hr /'


class LineBreak(SelfClosingTag):
    tag = 'br /'



