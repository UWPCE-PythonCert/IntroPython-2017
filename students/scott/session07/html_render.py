#!/usr/bin/env python3

class TextWrapper:
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)


class Element:
    tag = 'html'
    indent = '  '

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))


    def render(self, file_out, ind=""):
        file_out.write("{}<{}>\n".format(ind,self.tag))
        for item in self.content:
            item.render(file_out, ind + self.indent)
            file_out.write("\n")
        file_out.write("{}</{}>\n".format(ind,self.tag))

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'