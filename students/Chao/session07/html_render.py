#!/usr/bin/env python

class Element():
    tag = 'html'
    indent = ""

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)
        #print(self.content)

    def render(self, file_obj, ind = ""):
        file_obj.write('<' + self.tag + '>\n')
        for each in self.content:
            if type(each) == str:
                file_obj.write(ind + each + '\n')
            else:
                self.content = self.content.content
                # for a in each.content:
                #     file_obj.write(ind + a + '\n')
        file_obj.write('</' + self.tag + '>\n')

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'
