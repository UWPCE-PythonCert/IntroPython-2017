class Element():
    # Pretty-print HTML files with increasing indent levels
    # for each depth of tag.
    tag = 'html'
    extra_indent = 4 * ' '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        # Collect additional objects alongside existing objects
        self.content.append(content)

    def render(self, out_file, current_ind=""):
        # Pretty-print content and tags to file.
        # For objects, pretty-print all the content and tags
        # they contain to the file. Nest tags with indentation.

        out_file.write('\n' + current_ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file, current_ind + self.extra_indent)
            except AttributeError:
                out_file.write('\n' + current_ind +
                               self.extra_indent + str(each))
        out_file.write('\n' + current_ind + '</' + self.tag + '>')


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

        out_file.write('\n' + current_ind + '<' + self.tag + '>')
        for each in self.content:
            out_file.write(' ' + str(each) + ' ')
        out_file.write('</' + self.tag + '>')


class Title(OneLineTag):
    tag = 'title'
