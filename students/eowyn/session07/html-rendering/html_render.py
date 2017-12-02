class Element():
    # Pretty-print HTML files with increasing indent levels
    # for each depth of tag.
    tag = 'html'
    extra_indent = 4 * ' '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs  # a dictionary w/all the keyword args

    def append(self, content):
        # Collect additional objects alongside existing objects
        self.content.append(content)

    def render(self, out_file, current_ind=""):
        # Pretty-print content and tags to file.
        # For objects, pretty-print all the content and tags
        # they contain to the file. Nest tags with indentation.
        self.render_open_tag(out_file, current_ind)
        for each in self.content:
            try:
                each.render(out_file, current_ind + self.extra_indent)
            except AttributeError:
                out_file.write('\n' + current_ind +
                               self.extra_indent + str(each))
        out_file.write('\n')
        close_tag = '{}</{}>'.format(current_ind, self.tag)
        out_file.write(close_tag)

    def render_open_tag(self, out_file, current_ind):
        # This code was repeated so I refactored it!
        # Get and write an open tag to out_file
        open_tag = self.get_open_tag()
        out_file.write('\n')
        out_file.write(current_ind)
        out_file.write(open_tag)

    def get_open_tag(self):
        # This code was repeated so I refactored it!
        # Construct the open tag with its attributes, if present
        open_tag = '<{}'.format(self.tag)
        open_tag += self.get_tag_attributes()
        open_tag += ">"
        return open_tag

    def get_tag_attributes(self):
        # This code was repeated so I refactored it!
        # Construct string of any/all attributes
        att_str = ""
        for att, val in self.attributes.items():
            att_str += ' {}="{}"'.format(att, val)
        return att_str


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'

    def render(self, out_file, ind=""):
        # Pretty-print content and tags to file.
        # For objects, pretty-print all the content and tags
        # they contain to the file. Nest tags with indentation.
        # For html files, include a top level DOCTYPE string.
        out_file.write('<!DOCTYPE html>')
        Element.render(self, out_file, ind)


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file, current_ind=""):
        # Pretty-print content and tags to file on one line.
        # Print the string representation of all objects within content.
        self.render_open_tag(out_file, current_ind)
        for each in self.content:
            out_file.write(' ' + str(each) + ' ')
        close_tag = '</{}>'.format(self.tag)
        out_file.write(close_tag)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    # render tags like <hr /> and <br />
    # render just one tag and any attributes

    def render(self, out_file, current_ind=""):
        # Render just a tag and any attributes, ignore contents
        self.render_open_tag(out_file, current_ind)

    def get_open_tag(self):
        # Override method to  have /> at end of open_tag instead of >
        open_tag = '<{}'.format(self.tag)
        open_tag += self.get_tag_attributes()
        open_tag += ' />'
        return open_tag


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    # Make anchor tags for hyperlinks, like this:
    # <a href="http://google.com"> link to google </a>
    # Instructions said subclass from Element but we want it on one line
    tag = 'a'

    def __init__(self, link=None, content=None, **kwargs):
        # Include href=link in the kwargs dictionary
        Element.__init__(self, content, href=link, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, hlevel, content=None, **kwargs):
        # Include hlevel for different header levels eg <h2>
        self.tag = 'h' + str(hlevel)
        Element.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    # Render method of self closing tag already uses key:value pairs
    # So we only need to update the tag!
    tag = 'meta'




