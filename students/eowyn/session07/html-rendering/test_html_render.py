import os
from html_render import Element, Body, P, Html, Head, OneLineTag, Title


def render_element(el_object, filename='test1.html', remove=True):
    with open(filename, 'w') as out_file:
        el_object.render(out_file)
    with open(filename, 'r') as in_file:
        contents = in_file.read()
    if remove:
        os.remove(filename)
    return contents


def test_add_content():
    el_object = Element('content')
    el_object = Element()
    assert el_object.content == []


def test_adding_empty_string():
    el_object = Element('')
    assert el_object .content == ['']


def test_append_string():
    el_object = Element('spam, spam, eggs')
    el_object.append(' and spam')
    assert el_object.content == ['spam, spam, eggs', ' and spam']


def test_tag_exists():
    assert Element.tag == 'html'
    el_object = Element('spam, spam, spam')
    assert el_object.tag == 'html'


def test_indent_exists():
    # could alternately test that it is any number of spaces
    assert ' ' in Element.extra_indent


def test_render():
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = Element(my_stuff)
    el_object.append(more_stuff)
    contents = render_element(el_object)
    contents = contents.strip()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_body_tag():
    # assert Body().tag == 'body'
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = Body(my_stuff)
    el_object.append(more_stuff)
    contents = render_element(el_object)
    contents = contents.strip()
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_paragraph_tag():
    # assert P().tag == 'p'
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = P(my_stuff)
    el_object.append(more_stuff)
    contents = render_element(el_object)
    contents = contents.strip()
    assert contents.startswith('<p>')
    assert contents.endswith('</p>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_html_tag():
    # assert Html().tag == 'html'
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = Html(my_stuff)
    el_object.append(more_stuff)
    contents = render_element(el_object)
    assert contents.startswith('<!DOCTYPE html>\n<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_body():
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = Body(my_stuff)
    el_object.append(more_stuff)
    contents = render_element(el_object)
    contents = contents.strip()
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_non_strings():
    my_stuff = 'any string I like'
    el_object = Element(Body(my_stuff))
    contents = render_element(el_object)
    contents = contents.strip()
    print(contents)
    assert my_stuff in contents
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert '<body>' in contents
    assert '</body>' in contents
    assert contents.index('<body>') < contents.index(my_stuff)
    assert contents.index('<body>') < contents.index('</body>')


def test_head_tag():
    # assert newobj.tag == 'head'
    my_stuff = 'any string I like'
    head_obj = Head(my_stuff)
    contents = render_element(head_obj)
    contents = contents.strip()
    assert my_stuff in contents
    assert contents.startswith('<head>')
    assert contents.endswith('</head>')


def test_title_tag():
    # assert Title().tag == 'title'
    my_stuff = 'any string I like'
    titleobj = Title(my_stuff)
    contents = render_element(titleobj)
    contents = contents.strip()
    assert my_stuff in contents
    assert contents.startswith('<title>')
    assert contents.endswith('</title>')


def test_one_line_tag():
    oneliner = OneLineTag('this is a one line tag')
    contents = render_element(oneliner)
    contents = contents.strip()
    lines = contents.split('\n')
    assert 'this is a one line tag' in contents
    assert oneliner.tag == 'html'
    assert len(lines) == 1


def test_title_render():
    my_stuff = 'bye bye ms american pie'
    titleobj = Title(my_stuff)
    more_stuff = ' drove my chevy to the levy'
    titleobj.append(more_stuff)
    contents = render_element(titleobj)
    contents = contents.strip()
    assert contents.startswith('<title>')
    assert contents.endswith('</title>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_indentation():
    my_stuff = 'Blondes just have more fun'
    el_object = Element(my_stuff)
    contents = render_element(el_object)
    contents = contents.strip()
    print(contents)
    lines = contents.split('\n')
    assert len(lines) == 3
    assert lines[1].startswith(Element.extra_indent + 'Blondes')


def test_multiple_indentation():
    my_stuff = "Q: Where in the world is Grover Norquist?"
    more_stuff = "A: Pretending the Laffer curve is relevant"
    el_object = Body(my_stuff)
    el_object.append(P(more_stuff))
    contents = render_element(el_object)
    contents = contents.strip()
    print(contents)
    lines = contents.split('\n')
    assert len(lines) == 6
    # Check content indentation
    assert lines[1].startswith(Element.extra_indent + 'Q:')
    assert lines[3].startswith(2 * Element.extra_indent + 'A:')
    print('Len of Element.extra_indent is: ', len(Element.extra_indent))
    print('Len of el_object.indent is: ', len(el_object.extra_indent))
    # Check body tag indentation (level 0)
    assert lines[0].startswith('<body>')
    assert lines[5].startswith('</body>')
    # Check paragraph tag indendation (level 1)
    assert lines[2].startswith(Element.extra_indent + '<p>')
    assert lines[4].startswith(Element.extra_indent + '</p>')


def test_title_indendation_onestring():
    my_stuff = "Q: Where in the world is Grover Norquist?"
    el_object = Title(my_stuff)
    contents = render_element(el_object)
    contents = contents.strip()
    print(contents)
    lines = contents.split('\n')
    assert len(lines) == 1
    assert lines[0].startswith('<title> ')
    assert my_stuff in lines[0]
    assert lines[0].endswith(' </title>')


def test_title_indendation_twothings():
    my_stuff = "Q: Where in the world is Grover Norquist?"
    more_stuff = "A: Pretending the Laffer curve is relevant"
    el_object = Title(my_stuff)
    body_object = Body(more_stuff)
    el_object.append(body_object)
    contents = render_element(el_object)
    contents = contents.strip()
    print(contents)
    lines = contents.split('\n')
    assert len(lines) == 1
    assert lines[0].startswith('<title> ')
    assert my_stuff in lines[0]
