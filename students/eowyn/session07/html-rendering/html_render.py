

class Element():
    tag = 'html'
    indent = 4 * ' '

    def __init__(self, content=None):
        # import pdb; pdb.set_trace()
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=""):
        if self.tag == 'html':
            out_file.write('<!DOCTYPE html>')
        out_file.write('\n')
        out_file.write(ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file, ind + self.indent)
            except AttributeError:
                out_file.write('\n' + ind + self.indent + str(each))
        if ind != "":
            out_file.write('\n' + ind)
        out_file.write('</' + self.tag + '>')

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file, ind=""):
        out_file.write('\n' + ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file)
            except AttributeError:
                out_file.write(str(each))
        out_file.write('</' + self.tag + '>')


class Title(OneLineTag):
    tag = 'title'
