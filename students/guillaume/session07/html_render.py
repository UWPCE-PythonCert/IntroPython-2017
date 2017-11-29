

class Element():
    tag = ''
    indent = ''

    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content=None, **kwargs):
        self.kwargs.update(kwargs)
        if content is not None:
            self.content.append(content)

    def render(self, file_obj, ind=""):

        # add attribute to the tag
        att = ', '.join(['{}="{}"'.format(arg, self.kwargs[arg])
                        for arg in self.kwargs])
        if att != "":
            att = ' {}'.format(att)
        file_obj.write('{}<{}{}>\n'.format(ind, self.tag, att))

        for each in self.content:
            if hasattr(each, 'render'):
                each.render(file_obj, ind + each.indent)
            else:
                file_obj.write('{}{}\n'.format(ind + 4 * ' ', each))
        file_obj.write('{}</{}>\n'.format(ind, self.tag))


class OneLineTag(Element):

    def render(self, file_obj, ind=""):
        att = ', '.join(['{}="{}"'.format(arg, self.kwargs[arg])
                        for arg in self.kwargs])
        if att != "":
            att = ' {}'.format(att)
        output_ls = [ind, self.tag, att, ', '.join(self.content), self.tag]
        output = '{}<{}{}> {} </{}>\n '.format(*output_ls)
        file_obj.write(output)


class H(OneLineTag):
    tag = 'h'
    indent = 4 * ' '

    def __init__(self, level, content=None):
        OneLineTag.__init__(self, content)
        self.tag = '{}{}'.format(self.tag, str(level))


class SelfClosingTag(Element):

    def render(self, file_obj, ind=""):
        att = ', '.join(['{}="{}"'.format(arg, self.kwargs[arg])
                        for arg in self.kwargs])
        if att != "":
            att = ' {}'.format(att)
        file_obj.write('{}<{}{} />\n'.format(ind, self.tag, att))


class Ul(Element):
    tag = 'ul'
    indent = 4 * ' '


class Li(Element):
    tag = 'li'
    indent = 4 * ' '


class A(OneLineTag):
    tag = 'a'
    indent = 4 * ' '

    def __init__(self, link, content=None, **kwargs):
        self.kwargs = kwargs
        self.kwargs.update({'href': link})
        Element.__init__(self, content, **self.kwargs)


class Html(Element):
    tag = 'html'
    indent = 4 * ' '

    def render(self, file_obj, ind=""):
        file_obj.write('<!DOCTYPE html>\n')
        Element.render(self, file_obj, ind)


class Meta(SelfClosingTag):
    tag = 'meta'
    indent = 4 * ' '


class Body(Element):
    indent = 4 * ' '
    tag = 'body'


class P(Element):
    indent = 4 * ' '
    tag = 'p'


class Head(Element):
    indent = 4 * ' '
    tag = 'head'


class Title(OneLineTag):
    tag = 'title'
    indent = 4 * ' '


class Hr(SelfClosingTag):
    tag = 'hr'
    indent = 4 * ' '


class Br(SelfClosingTag):
    tag = 'br'
    indent = 4 * ' '

