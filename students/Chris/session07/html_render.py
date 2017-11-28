

class Element():

    tag = 'html'
    indent = '  '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, cur_ind=""):
        open_tag = '{}<{}>'.format(cur_ind, self.tag)
        close_tag = '{}</{}>'.format(cur_ind, self.tag)

        file_obj.write(open_tag)
        file_obj.write("\n")
        for each in self.content:
            if isinstance(each, str):
                file_obj.write(cur_ind + self.indent)
                file_obj.write(each)
            else:
                each.render(file_obj, cur_ind + self.indent)
            file_obj.write("\n")
        file_obj.write(close_tag)

class OneLineTag(Element):
    def render(self, file_obj, cur_ind=""):
        # there is some repition here -- maybe factor that out?
        file_obj.write('{}<{}> '.format(cur_ind, self.tag))
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

