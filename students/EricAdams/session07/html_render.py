

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

    def render(self, file_obj, indent=''):
        # all_content = ('<' + self.tag + '>')
        html_tag = ('<' + self.tag + '>')
        self.write_to_file(file_obj, html_tag)
        text = ""
        for each in self.content:
            try:
                # all_content += each
                text += each
            except TypeError:
                each.render(file_obj)
        html_tag = '</' + self.tag + '>'
        text += html_tag
        self.write_to_file(file_obj, text)

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'

