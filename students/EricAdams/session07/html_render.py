'''
Incorporated Chris's solution.
'''


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for just text

    This allows the Element classes to render either Element objects or
    plain text

    This is just too nifty to pass up!

    """

    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)


class Element():

    tag = 'html'
    # might as well make all the extended classes have the same indent
    indent = '    '

    def __init__(self, content=None):
        '''
        It makes much more sense to call the class's append method,
        rather than just append to the self.content.  This way the
        the class append method is always used to process any content.
        '''
        # if content is None:
        #     self.content = []
        # else:
        #     self.content = [content]
        self.content = []
        if content:
            # call the classes append method
            # so that it can do anything special it needs to do
            self.append(content)

    def append(self, content):
        '''
        Ensuring that any appends contain a render attribute is pretty cool.
        This is new to me, but seems much more object oriented than what I had.
        '''
        # self.content.append(content)
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, file_obj, cur_indent=''):
        '''
        This is incredibly simpler than what I had.
        The key, I think, is all content having a render attribute.
        '''
        # html_tag = ('\n' + indent + '<' + self.tag + '>\n')
        # indent_level = indent[:]
        # file_obj.write(html_tag)
        # text = ""
        # # text = html_tag
        # for each in self.content:
        #     try:
        #         text += each
        #     except TypeError:
        #         indent = indent + self.content[0].indent
        #         each.render(file_obj, indent)
        # html_tag = '\n' + indent_level + '</' + self.tag + '>'
        # text = indent_level + text + html_tag
        # file_obj.write(text)
        file_obj.write("{}<{}>\n".format(cur_indent, self.tag))
        for stuff in self.content:
            stuff.render(file_obj, cur_indent + self.indent)
            file_obj.write("\n")
        file_obj.write("{}</{}>".format(cur_indent, self.tag))


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'


class Head(Element):
    tag = 'head'


class OnelineTag(Element):
    # override Element.render to write all on one line
    def render(self, file_obj, cur_indent=''):
        # what recursion level are we going in
        # indent = self.indent + indent
        # html_tag = (indent + '<' + self.tag + '>\n')
        # html_tag = (indent + '<' + self.tag + '>')
        # # indent_level = indent[:]
        # file_obj.write(html_tag)
        # text = ""
        # # text = html_tag
        # for each in self.content:
        #     try:
        #         text += each
        #     except TypeError:
        #         indent = indent + self.content[0].indent
        #         each.render(file_obj, indent)
        # html_tag = '</' + self.tag + '>'
        # text = text + html_tag
        # file_obj.write(text)
        file_obj.write("{}<{}>".format(cur_indent, self.tag))
        for stuff in self.content:
            stuff.render(file_obj)
        file_obj.write("</{}>".format(self.tag))


class Title(OnelineTag):
    tag = 'title'
