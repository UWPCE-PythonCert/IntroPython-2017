#!/usr/bin/env python3


# is this is a subclass of a parent class? 
#If so, put the parent class in the Attributes of this class

class Element():
    tag = 'html'
    indent = '  '
   
    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content  = [content]


    def append(self, content):
        self.content.append(content)

    def render(self, file_obj):
        file_obj.write('<' + self.tag + '>')
        for item in self.content:
            file_obj.write(item)
        file_obj.write('</' + self.tag + '>')


class Body(Element):
    tag = 'body'

class Para(Element):
    tag = 'p'

class HTML(Element):
    tag = 'html'
