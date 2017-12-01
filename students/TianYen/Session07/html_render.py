class Element():
    """ A class that allows for formatting and writing of html code"""
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        """initialize the class"""
        self.attr = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        """append content to the object"""
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, file_obj, current_ind = ""):
        """render the html code to a file with standard indentation"""
        self.write_open_tag(current_ind, file_obj)
        file_obj.write('\n')
        for each in self.content:
            if hasattr(each, 'render'):
                each.render(file_obj, current_ind + self.indent)
            else:
                file_obj.write(((current_ind + self.indent) + each + '\n'))
        file_obj.write('{}</{}>\n'.format(current_ind, self.tag))

    def write_open_tag(self, current_ind, file_obj):
        file_obj.write('{}<{}'.format(current_ind,self.tag,))
        if self.attr != {}:
            format_attr = ' {}="{}"'
            for key, value in self.attr.items():
                file_obj.write(format_attr.format(key, value))
                file_obj.write('> ')

class TextWrapper():
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text + '\n')

class Html(Element):
    """Subclass of Element for the html tag"""
    tag = 'html'

class Body(Element):
    """Subclass of Element for the body tag"""
    tag = 'body'

class P(Element):
    """Subclass of Element for the paragraph tag"""
    tag = 'p'

class Head(Element):
    """Subclass of Element for the head tag"""
    tag = 'head'

class OneLineTag(Element):
    """Subclass of Element, used for simple one line tags"""

    def render(self, file_obj, current_ind = ""):
        """render the html code to a file with standard indentation"""
        self.write_open_tag(current_ind, file_obj)
        for each in self.content:
            file_obj.write((each))
        file_obj.write(' </{}>\n'.format(self.tag))

class Title(OneLineTag):
    """Subclass of OneLineTag, used for the title tag"""
    tag = 'title'

class A(OneLineTag):
    """Subclass of OneLineTag for anchoring a link"""
    tag = 'a'
    def __init__(self, link, content=None):
        self.attr = {'href': str(link)}
        if content is None:
            self.content = []
        else:
            self.content = [content]

class SelfClosingTag(Element):
    """Subclass of Element, used for self closing tags"""

    def render(self, file_obj, current_ind = ""):
        """render the html code to a file with standard indentation"""
        ind = current_ind + self.indent
        file_obj.write('{current_ind}<{tag}'.format(tag = self.tag, current_ind = current_ind))
        if self.attr != {}:
            format_attr = " {}=\"{}\""
            for key, value in self.attr.items():
                file_obj.write(format_attr.format(key, value))
        file_obj.write(' />\n')

class Hr(SelfClosingTag):
    """Subclass of SelfClosingTag, used for horizontal rule"""
    tag = 'hr'

class Br(SelfClosingTag):
    """Subclass of SelfClosingTag, used for line breaks"""
    tag = 'br'
