"""
Kathryn Egan
"""


class Element:
    """ Stores behavior and data for an Element of HTML. """
    indent = '    '

    def __init__(self, content=None, **kwargs):
        """ Initializes an Element with content, if given,
        and any HTML attributes of the Element.
        Args:
            content (str or Element) : text or a nested Element
            kwargs (dic str:str) : HTML attributes for Element
        """
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrs = kwargs

    def append(self, content):
        """ Adds content to this Element.
        Args:
            content (str or Element) : text or a nested Element
        """
        self.content.append(content)

    def render(self, file_out, ind=0):
        """ Renders the contents of this Element into HTML
        format and pretty prints to file using given file handler.
        Args:
            file_out (TextIOWrapper) : file handler
            ind (int) : level of indentation for this Element
        """
        file_out.write('{}<{}{}>\n'.format(
            self.indent * ind, self.tag, self.attribute_str()))
        for c in self.content:
            try:
                c.render(file_out, ind + 1)
            except AttributeError:
                file_out.write('{}{}\n'.format((ind + 1) * self.indent, c))
        file_out.write('{}</{}>\n'.format(self.indent * ind, self.tag))

    def attribute_str(self):
        """ Returns this Element's attributes as a string.
        Returns:
            str : attributes as a string
        """
        return ''.join([
            ' {}="{}"'.format(key, self.attrs[key]) for key in self.attrs])


class OneLineTag(Element):
    """ Handles ne-line HTML elements. """

    def render(self, file_out, ind=0):
        """ Renders the contents of this Element into HTML format
        on one line and writes to file using given file handler.
        Args:
            file_out (TextIOWrapper) : file handler
            ind (int) : level of indentation for this Element
        """
        file_out.write('{}<{}{}>'.format(
            self.indent * ind, self.tag, self.attribute_str()))
        for c in self.content:
            file_out.write(c)
        file_out.write('</{}>\n'.format(self.tag))


class SelfClosingTag(Element):
    """ Handles contentless HTML elements. """

    def render(self, file_out, ind=0):
        """ Renders this contentless Element into HTML
        and writes to file using given file handler.
        Args:
            file_out (TextIOWrapper) : file handler
            ind (int) : level of indentation for this Element
        """
        file_out.write('{}<{}{} />\n'.format(
            self.indent * ind, self.tag, self.attribute_str()))


class Html(Element):
    """ HTML page. """
    tag = 'html'

    def render(self, file_out, ind=0):
        """ Renders the contents of this Element into HTML
        format headed by doctype. Writes to file using given file handler.
        Args:
            file_out (TextIOWrapper) : file handler
            ind (int) : level of indentation for this Element
        """
        file_out.write('<!DOCTYPE {}>\n'.format(self.tag))
        Element.render(self, file_out, ind=1)


class A(OneLineTag):
    """ HTML hyperlink element. """
    tag = 'a'

    def __init__(self, link, content, **kwargs):
        """ Maps link to content as an HTML attribute of an Element.
        Args:
            link (str) : hyperlink
            content (str) : content to map hyperlink to
        """
        kwargs['href'] = link
        Element.__init__(self, content, **kwargs)


class H(OneLineTag):
    """ HTML header element. """

    def __init__(self, level, content, **kwargs):
        """ Initializes this element with the given level and content.
        Args:
            level (int) : level of this header
            content (str) : content of this header
        """
        self.tag = 'h' + str(level)
        Element.__init__(self, content, **kwargs)


class Title(OneLineTag):
    """ HTML title element. """
    tag = 'title'


class Hr(SelfClosingTag):
    """ HTML horizontal line element. """
    tag = 'hr'


class Br(SelfClosingTag):
    """ HTML line break element. """
    tag = 'br'


class Meta(SelfClosingTag):
    """ HTML head encoding. """
    tag = 'meta'


class Head(Element):
    """ HTML Head element. """
    tag = 'head'


class Body(Element):
    """ HTML body element. """
    tag = 'body'


class P(Element):
    """ HTML paragpraph element. """
    tag = 'p'


class Ul(Element):
    """ HTML unordered list. """
    tag = 'ul'


class Li(Element):
    """ HTML list element. """
    tag = 'li'