

class Element():

    tag = 'html'
    indent = ''
    # keep track of the depth of recursion
    depth = 0

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, indent=''):
        # what recursion level are we going in
        Element.depth += 1
        html_tag = (self.indent * (Element.depth - 1) + '<' + self.tag + '>\n')
        self.write_to_file(file_obj, html_tag)
        text = ""
        for each in self.content:
            try:
                text += each
            except TypeError:
                each.render(file_obj)
        # what recursion level are at coming out
        Element.depth -= 1
        html_tag = '\n' + (self.indent * (Element.depth)) + \
            '</' + self.tag + '>\n'
        text = self.indent * (Element.depth) + text + html_tag
        self.write_to_file(file_obj, text)

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)


class Body(Element):
    tag = 'body'
    indent = '    '


class P(Element):
    tag = 'p'
    indent = '    '


class Html(Element):
    tag = 'html'
    indent = ''


class Head(Element):
    tag = 'head'
    indent = '    '


class OnelineTag(Element):
    # override Element.render to write all on one line
    def render(self, file_obj, indent=''):
        # what recursion level are we going in
        Element.depth += 1
        html_tag = (self.indent * (Element.depth - 1) + '<' + self.tag + '>')
        file_obj.write(html_tag)
        text = ""
        for each in self.content:
            try:
                text += each
            except TypeError:
                each.render(file_obj)
        # what recursion level are at coming out
        Element.depth -= 1
        html_tag = '</' + self.tag + '>'
        # text = self.indent * (Element.depth) + text + html_tag
        text = text + html_tag
        file_obj.write(text)


class Title(OnelineTag):
    tag = 'title'
    indent = '    '
