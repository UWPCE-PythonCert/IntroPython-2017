#!/usr/bin/env python3
# coding=utf-8
from __future__ import unicode_literals

class Element(object):
    """ class for rendering HTML element
    """
    def __init__(self, content=None, **kwargs):
        self.tag = "tag"
        self.elements = []
        self.kwargs = {}

        if content is not None:
            self.append(content)

        if kwargs is not None:
            self.kwargs = kwargs

    def append(self, content):
        """ Appends content to class attribute elements list
        """
        self.elements.append(content)


    def render(self, file_out, ind="", depth=1):
        """ Writes content to StringIO buffer with optional indentation
        :file_out StringIO: StringIO
        :ind String: char indentation
        """
        formatted_open_tag = self.tag
        for key, value in self.kwargs.items():
            formatted_open_tag += ' {}="{}"'.format(key, value)

        file_out.write("{}<{}>\n".format(ind*depth, formatted_open_tag))

        for elem in self.elements:
            if isinstance(elem, str):
                file_out.write("{}{}\n".format(ind*(depth+1), elem))
            else:
                elem.render(file_out, ind, depth+1)

        else:
            file_out.write("{}</{}>\n".format(ind*depth, self.tag))


class OneLineTag(Element):
    def __init__(self, content=None, **kwargs):
        super(OneLineTag, self).__init__(content, **kwargs)


    def render(self, file_out, ind = "", depth=1):
        for elem in self.elements:
            file_out.write("{0}<{1}>{2}</{1}>\n".format(ind*depth, self.tag,
                                                        elem))


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        super(SelfClosingTag, self).__init__(content, **kwargs)


    def render(self, file_out, ind = "", depth=1):
        file_out.write("{}<{} />\n".format(ind*depth, self.tag))


class Html(Element):
    """ Subclass of element for HTML tags
    """
    def __init__(self, content=None, **kwargs):
        super(Html, self).__init__(content, **kwargs)
        self.tag = "html"


    def render(self, file_out, ind="", depth=1):
        """ Overrides render method and prepends DOCTYPE string
        """
        file_out.write("<!DOCTYPE html>\n")
        super(Html, self).render(file_out, ind, depth)


class Title(OneLineTag):
    """ Subclass of element for title tags
    """
    def __init__(self, content=None, **kwargs):
        super(Title, self).__init__(content, **kwargs)
        self.tag = "title"


class Head(Element):
    """ Subclass of element for head tags
    """
    def __init__(self, content=None, **kwargs):
        super(Head, self).__init__(content, **kwargs)
        self.tag = "head"


class Body(Element):
    """ Subclass of element for body tags
    """
    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content, **kwargs)
        self.tag = "body"


class P(Element):
    """ Subclass of element for paragraph tags
    """
    def __init__(self, content=None, **kwargs):
        super(P, self).__init__(content, **kwargs)
        self.tag = "p"


class Hr(SelfClosingTag):
    """ Element class for hr
    """
    def __init__(self, content=None, **kwargs):
        super(Hr, self).__init__(content, **kwargs)
        self.tag = "hr"


class Br(SelfClosingTag):
    """ Element class for br
    """
    def __init__(self, content=None, **kwargs):
        super(Br, self).__init__(content, **kwargs)
        self.tag = "br"


class A(Element):
    """ Element class for anchor link
    """
    def __init__(self, link, text):
        super(A, self).__init__()
        self.link = link
        self.text = text


    def render(self, file_out, ind="", depth=1):
        """ Overrides element render method
        """
        file_out.write('{}<a href="{}">{}</a>\n'.format(ind*depth, self.link,
                                                        self.text))


class Ul(Element):
    """ Element class for ul
    """
    def __init__(self, content=None, **kwargs):
        super(Ul, self).__init__(None, **kwargs)
        self.tag = "ul"


class Li(Element):
    """ Element class for li
    """
    def __init__(self, content=None, **kwargs):
        super(Li, self).__init__(content, **kwargs)
        self.tag = "li"


class H(OneLineTag):
    """ Element class for headers
    """
    def __init__(self, level, text):
        super(H, self).__init__()
        self.level = level
        self.text = text

    def render(self, file_out, ind="", depth=1):
        """ Overrides render method for OneLineTag
        """
        file_out.write("{0}<h{1}>{2}</h{1}>\n".format(ind*depth, self.level,
                                                      self.text))
