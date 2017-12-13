'''
Test file for HTML Render
'''

import html_render
from html_render import Element, Body, Paragraph, HTML, HEAD, OneLineTag, Title

def test_new_element():
    el_object = Element()
    el_object2 = Element('content')


def test_add_content():
    el_object = Element('content')
    print(el_object.content)
    assert el_object.content == ['content']


def test_adding_empty_string():
    el_object = Element('')
    assert el_object.content == ['']


def test_append_string():
    el_object = Element('hamma, hamma, hamma')
    el_object.append("wonderful hamma")
    assert el_object.content == ['hamma, hamma, hamma', "wonderful hamma"]


def test_tag_exists():
    assert Element.tag == 'html'
    el_object = Element('hamma, hamma, hamma')
    assert el_object.tag == 'html'


def test_indent_exists():
    assert Element.indent == ' '


def test_render_indent():
    my_stuff = 'indentedstuff'
    el_object = HTML(my_stuff)
    el_object.indent = 5
    with open('test-ind', "w") as out_file:
        el_object.render(out_file)
    with open('test-ind', 'r') as in_file:
        contents = in_file.read()
    assert el_object.indent == 5


def test_render_element():
    my_stuff = 'hamma, hamma, hamma'
    el_object = Element(my_stuff)
    more_stuff = "umma, umma, umma"
    el_object.append(more_stuff)
    with open('test1', 'w') as out_file:
        el_object.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_body_tag():
    assert Body.tag == "body"


def test_render_body():
    my_stuff = 'hamma, hamma, hamma'
    el_object = Body(my_stuff)
    more_stuff = "umma, umma, umma"
    el_object.append(more_stuff)
    with open('testb', 'w') as out_file:
        el_object.render(out_file)
    with open('testb', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<body')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_paragraph_tag():
    assert Paragraph.tag == "p"


def test_render_paragraph():
    my_stuff = 'hamma, hamma, hamma'
    el_object = Paragraph(my_stuff)
    more_stuff = "umma, umma, umma"
    el_object.append(more_stuff)
    with open('testp', 'w') as out_file:
        el_object.render(out_file)
    with open('testp', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<p>')
    assert contents.endswith('</p>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_HTML_tag():
    assert HTML.tag == "html"


def test_render_HTML():
    my_stuff = 'hamma, hamma, hamma'
    el_object = HTML(my_stuff)
    more_stuff = "umma, umma, umma"
    el_object.append(more_stuff)
    with open('testh', 'w') as out_file:
        el_object.render(out_file)
    with open('testh', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_HEAD_tag():
    assert HEAD.tag == "head"


def test_render_HEAD():
    my_stuff = "items, items, items"
    el_object = HEAD(my_stuff)
    with open('testhead', 'w') as out_file:
        el_object.render(out_file)
    with open('testhead', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<head>')
    assert contents.endswith('</head>')
    assert my_stuff in contents


def test_OneLineTag_render():
    cont = "it is"
    el_object = OneLineTag(cont)
    more_stuff = "umma, umma, umma"
    el_object.append(more_stuff)
    with open('testline', 'w') as out_file:
        el_object.render(out_file)
    with open('testline', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>it isumma, umma, umma</html><html>it isumma, umma, umma</html>')


def test_Title_tag():
    assert Title.tag == "title"


def test_title_render():
    my_stuff = "items, items, items"
    el_object = Title(my_stuff)
    with open('testtitle', 'w') as out_file:
        el_object.render(out_file)
    with open('testtitle', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<title>')
    assert contents.endswith('</title>')
    assert my_stuff in contents