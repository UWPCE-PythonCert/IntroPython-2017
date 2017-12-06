'''
Render HTML
'''

class Element():
    tag = 'html'
    indent = ' '
    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]


    def append(self, content):
        self.content.append(content)


    def render(self, file_obj, cur_ind=0):
        ind = str(self.indent * cur_ind)
        file_obj.write('<' + self.tag + '>')
        for i in self.content:
            file_obj.write(i)
        file_obj.write(ind +'</' + self.tag + '>')

class Body(Element):
    tag = 'body'

class Paragraph(Element):
    tag = 'p'

class HTML(Element):
    tag = 'html'

class HEAD(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, file_obj, cur_ind=0):
        ind = str(self.indent * cur_ind)
        outstring = '<' + self.tag + '>'
        for i in self.content:
            outstring += i
        outstring += '</' + self.tag + '>'
        outstring += outstring.replace('\n', " ")
        file_obj.write(outstring)

class Title(OneLineTag):
    tag = "title"
