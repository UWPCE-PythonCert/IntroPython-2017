#!/usr/bin/env python3

"""
HTML Rendering Exercise
--The goal is to create a set of classes to render html pages – in a “pretty printed” way.
--Nicely indented and human readable.

--cur_ind is the current level of indentation for amount the entire tag should be indented

"""


# step 1 - create an Element class with append and render methods
class Element():
    # class attribute
    tag = 'html'
    # 4 spaces per indentation
    indent = '    '

    def __init__(self, content=None, **kwargs):
        # **kwargs can except any keyword arguments (return dictionary) - step 4
        self.attributes = kwargs
        # content is expecting a string and default at None
        if content is None:
            self.content = []
        else:
            self.content = [content]

    # to add another string to the content
    def append(self, content):
        self.content.append(content)

    # create open tag for all tags
    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        for attr, attr_val in self.attributes.items():
            open_tag += ' {}="{}"'.format(attr, attr_val)
        open_tag += "> "
        return open_tag

   #create close tag for all tags
    def get_close_tag(self):
        close_tag = '<\{}>'.format(self.tag)
        return close_tag

    #created this method for onelinetag method, but I don't need it anymore
    # #make attribute tags:
    # def attribute_tag(self):
    #     open_tag = '<{} '.format(self.tag)
    #     for attr, attr_val in self.attributes.items():
    #         if open_tag == '<{} '.format(self.tag):
    #             open_tag += '{}="{}"'.format(attr, attr_val)
    #         else:
    #             open_tag = "<{}>\n".format(self.tag)
    #     return open_tag

    #takes a file like object and write html tags
    def render(self, file_obj, cur_ind=""):
        file_obj.write(cur_ind)
        file_obj.write(self.get_open_tag())
        file_obj.write("\n")
        for each in self.content:
            try:
                each.render(file_obj, cur_ind + self.indent)
            except AttributeError:
                file_obj.write(cur_ind + self.indent)
                file_obj.write(each)
        file_obj.write(self.get_close_tag())


#step 2 - create subclasses (Body, Html, Para, Head, Title, etc) and inherit it from the parent class, Element
class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

#step 3 create a OneLineTag subclass of Element and a Title subclass of OneLineTag
class OneLineTag(Element):
    """ this method overrides the Element's render method to render everything on one line"""

    def render(self, file_obj, cur_ind=""):
        file_obj.write(cur_ind)
        file_obj.write(self.get_open_tag())
        for each in self.content:
            file_obj.write(each)
        file_obj.write(self.get_close_tag())

class Title(OneLineTag):
    tag = 'title'

#step 5
class SelfClosingTag(Element):
    """ Base class for tags that have no content
        Render tags like <hr /> and <br /> """

    def render(self, file_obj, cur_ind=""):
        open_tag = '<{}'.format(self.tag)
        close_tag = ' />'
        try:
            file_obj.write(cur_ind)
            file_obj.write(open_tag)
            file_obj.write(close_tag)
        except TypeError:
            print("Can't add content to a self closing tag")

class Hr(SelfClosingTag):
    """horizontal rule"""
    tag = "hr"

class Br(SelfClosingTag):
    """line break"""
    tag = 'br'

#step 6
class A(OneLineTag):
    """anchor element"""
    tag = 'a'

    def __init__(self, link, *args, **kwargs):
        #TODO: how to include 'href' and link
        kwargs['href'] = link
        super().__init__(*args, **kwargs)

#step 7
class Ul(Element):
    """unordered list"""
    tag = 'ul'

class Li(Element):
    """list element"""
    tag = 'li'

class H(OneLineTag):
    """section head"""

    def __init__(self, level, *args, **kwargs):
        #TODO: need to visit html code for header samples
        #header has <h1> to <h6> tags
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)

#step 8
class Html(Element):
    """Print <!DOCTYPE html> above html tag"""
    tag = 'html'

    def render(self, file_obj, cur_ind=""):
        file_obj.write('!<DOCTYPE html>\n')
        Element.render(self, file_obj, cur_ind)

class Meta(SelfClosingTag):
    tag = 'meta'




