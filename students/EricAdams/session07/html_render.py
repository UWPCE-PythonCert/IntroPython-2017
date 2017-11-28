

class Element():

    tag = 'html'
    indent = ''
    # keep track of the depth of recursion
    # depth = 0

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, indent=''):
        # what recursion level are we going in
        # indent = self.indent + indent
        # html_tag = (indent + '<' + self.tag + '>\n')
        html_tag = ('\n' + indent + '<' + self.tag + '>\n')
        indent_level = indent[:]
        file_obj.write(html_tag)
        text = ""
        # text = html_tag
        for each in self.content:
            try:
                text += each
            except TypeError:
                indent = indent + self.content[0].indent
                each.render(file_obj, indent)
        html_tag = '\n' + indent_level + '</' + self.tag + '>'
        text = indent_level + text + html_tag
        file_obj.write(text)


class Body(Element):
    tag = 'body'
    indent = '    '


class P(Element):
    tag = 'p'
    indent = '    '
    # indent = ''


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
        # indent = self.indent + indent
        # html_tag = (indent + '<' + self.tag + '>\n')
        html_tag = (indent + '<' + self.tag + '>')
        # indent_level = indent[:]
        file_obj.write(html_tag)
        text = ""
        # text = html_tag
        for each in self.content:
            try:
                text += each
            except TypeError:
                indent = indent + self.content[0].indent
                each.render(file_obj, indent)
        # html_tag = '\n' + indent_level + '</' + self.tag + '>'
        # html_tag = indent_level + '</' + self.tag + '>'
        html_tag = '</' + self.tag + '>'
        # text = indent_level + text + html_tag
        text = text + html_tag
        file_obj.write(text)


class Title(OnelineTag):
    tag = 'title'
    indent = '    '
