

class Element():

    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, cur_ind=""):
        open_tag = self.get_open_tag()
        close_tag = '{}</{}>'.format(cur_ind, self.tag)

        file_obj.write(cur_ind)
        file_obj.write(open_tag)
        file_obj.write("\n")
        for each in self.content:
            try:
                each.render(file_obj, cur_ind + self.indent)
            except AttributeError:
                file_obj.write(cur_ind + self.indent)
                file_obj.write(each)
            file_obj.write("\n")
        file_obj.write(close_tag)

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag)
        for at, val in self.attributes.items():
            open_tag += ' {}="{}"'.format(at, val)
        open_tag += "> "
        return open_tag


class OneLineTag(Element):
    def render(self, file_obj, cur_ind=""):
        # there is some repition here -- maybe factor that out?
        open_tag = self.get_open_tag()
        file_obj.write(cur_ind)
        file_obj.write(open_tag)
        for each in self.content:
            # OneLineTags should only have strings...
            file_obj.write(each)
        file_obj.write(' </{}>'.format(self.tag))

class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class HTML(Element):
    tag = 'html'


class Head(Element):
    tag = 'head'


class Title(OneLineTag):
    tag = 'title'

