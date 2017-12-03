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

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + self.text)


class Element():

    tag = 'html'
    # might as well make all the extended classes have the same indent
    indent = '    '

    def __init__(self, content=None, **kwargs):
        '''
        It makes much more sense to call the class's append method,
        rather than just append to the self.content.  This way the
        the class append method is always used to process any content.
        Adding **kwargs for step 4..add html tag attributes
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
        self.attributes = kwargs

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
        Adding functionality to render tag parameters and some refactoring
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
        open_tag = self.get_open_tag() + ' \n'
        close_tag = '{}</{}>'.format(cur_indent, self.tag)

        file_obj.write(cur_indent)
        file_obj.write(open_tag)
        for stuff in self.content:
            stuff.render(file_obj, cur_indent + self.indent)
            file_obj.write("\n")
        file_obj.write(close_tag)

    def get_open_tag(self):
        # self.attributes is a dictionary, (tag attributes are key=values)
        open_tag = '<{}'.format(self.tag)
        for at, val in self.attributes.items():
            open_tag += ' {}="{}"'.format(at, val)
        # open_tag += "> \n"
        open_tag += ">"
        return open_tag


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
        open_tag = self.get_open_tag()
        # close_tag = '{}</{}>'.format(cur_indent, self.tag)
        close_tag = '</{}>'.format(self.tag)

        file_obj.write(cur_indent)
        file_obj.write(open_tag)
        for stuff in self.content:
            # stuff.render(file_obj, cur_indent + self.indent)
            stuff.render(file_obj)
            # file_obj.write("\n")
        file_obj.write(close_tag)


class Title(OnelineTag):
    tag = 'title'


class SelfClosingTag(Element):
    # Override Element.render to write on one line only, plus no closing
    # tag.
    # Override __init__ in element class, since there is no text to write.

    def __init__(self, **kwargs):
        '''
        Contents para not used since no text is to be passed
        '''
        self.attributes = kwargs

    def render(self, file_obj, cur_indent=''):
        open_tag = self.get_open_tag()
        # close_tag = '<{} />'.format(self.tag)
        # close_tag = ' />'
        file_obj.write(cur_indent)
        file_obj.write(open_tag)
        # file_obj.write(close_tag)


class Hr(SelfClosingTag):
    '''
    Rule tag
    '''
    tag = 'hr'


class Br(SelfClosingTag):
    '''
    Break tag
    '''
    tag = 'br'


class A(OnelineTag):
    '''
    Anchor tag
    '''
    tag = 'a'

    def __init__(self, link, content):
        self.content = content
        kwarg = {}
        kwarg["href"] = str(link)
        Element.__init__(self, content, **kwarg)


class H(OnelineTag):
    '''
    Heading tag. Override Element.__init__, since the heading size has to be
    passed.  Call Element.__init__ since this heading tag takes standard
    html global attributes.
    Override the OneLineTag render method, since the tag will have the size
    appended to it, (e.g. <h1>), this means that the Element.get_open_tag
    will have to be overridden as well.
    '''
    tag = 'h'

    def __init__(self, size, content, **kwargs):
        self.size = size
        self.content = content
        self.attributes = kwargs
        Element.__init__(self, content, **kwargs)

    def render(self, file_obj, cur_indent=''):
        open_tag = self.get_open_tag()
        close_tag = '</{}{}>'.format(self.tag, self.size)

        file_obj.write(cur_indent)
        file_obj.write(open_tag)
        for stuff in self.content:
            stuff.render(file_obj)
        file_obj.write(close_tag)

    def get_open_tag(self):
        open_tag = '<{}{}'.format(self.tag, self.size)
        for at, val in self.attributes.items():
            open_tag += ' {}="{}"'.format(at, val)
        open_tag += ">"
        return open_tag


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Doc(Element):
    '''
    Print <!DOCTYPE html> at the top of the web page
    Override Element.render
    '''
    # tag = '!DOCTYPE html'

    def render(self, file_obj, cur_indent=''):
        file_obj.write('!DOCTYPE html\n')
        Element.render(self, file_obj, cur_indent)


class Meta(SelfClosingTag):
    tag = 'meta'

