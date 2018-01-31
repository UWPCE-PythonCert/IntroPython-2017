

class Element():
    tag = 'html'
    indent = ' ' * 3


    def __init__(self,content=None, **kwargs):
        # import pdb; pdb.set_trace()
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs


    def append(self, content):
        self.content.append(content)

    def render(self, out_file, current_ind=" " * 0):    
        open_tag = self.get_open_tag()
        close_tag = '{}</{}>'.format(current_ind, self.tag)

        out_file.write(current_ind)
        out_file.write(open_tag)
        out_file.write("\n")
        
        for each in self.content:
            try:
                each.render(out_file, current_ind+ self.indent)
            except AttributeError:
                out_file.write(current_ind + self.indent)
                out_file.write(each)
            out_file.write("\n")

        out_file.write(close_tag)

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        for at, val in self.attributes.items():
            open_tag += ' {}="{}"'.format(at,val)
        open_tag += "> "
        return open_tag


class OneLineTag(Element):
    def render(self, out_file, ind=""):
        # out_file.write("{}<{}>".format(ind, self.tag))
        open_tag = self.get_open_tag()
        out_file.write(ind)
        out_file.write(open_tag)
        for stuff in self.content:
            out_file.write(stuff)
        out_file.write("</{}>".format(self.tag))

class SelfClosingTag(Element):
    def render(self, out_file, ind=""):
        out_file.write(ind)
        out_file.write("<{} />".format(self.tag))

class A(Element):
    tag = 'a'
    indent = ""

    def __init__(self, link, content=None):
        self.link = link
        self.content = content
        
        

    def render(self, out_file, current_ind=""):
        linkage = '{}<{} href="{}"> {} </{}>'.format(current_ind, self.tag, self.link, self.content, self.tag)
        out_file.write(linkage)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, size, content=None):
        self.size = self.tag + str(size)
        self.content = content


    def render(self, out_file, current_ind=""):
        blah = "{}<{}> {} </{}>".format(current_ind, self.size, self.content, self.size)
        out_file.write(blah)

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(OneLineTag):
    tag = 'title'





class Html(Element):
    tag = 'html'

# class TextWrapper:
#     def __init(self, text):
#         self.text = text

#     def render(self, file_out, current_ind=""):
#         file_out.write(current_ind + self.text)


# class Html(Element):

#     tag = "html"
#     indent = " " * 4

#     def __init__(self, content=None):
#         self.content = []

#         if content:
#             self.append(content)

#     def append(self, content):
#         if hasattr(content, 'render'):
#             self.content.append(content)
#         else:
#             self.content.append(TextWrapper(str(content)))

#     def render(self, out_file, ind=""):
#         out_file.write("{}<{}>\n".format(ind, self.tag))
#         for stuff in self.content:
#             stuff.render(out_file, ind + self.indent)
#             out_file.write("\n")
#         out_file.write("{}</{}>".format(ind, self.tag))



