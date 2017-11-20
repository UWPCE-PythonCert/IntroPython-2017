import html_render
from html_render import Element, Body, P, Html,Head,OneLineTag,Title

def test_new_element():
    el_obj = Element
    el_obj2 = Element('content')


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
    assert ' ' in Element.indent


def test_render():
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = Element(my_stuff)
    el_object.append(more_stuff)
    with open('test1', 'w') as out_file:
        el_object.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<!DOCTYPE html>\n<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents

def test_body_tag():
    assert Body().tag == 'body'

def test_paragraph_tag():
    assert P().tag == 'p'


def test_html_tag():
    assert Html().tag == 'html'

def test_render_body():
    my_stuff = 'spam, spam, spam'
    more_stuff = '\neggs, eggs, eggs'
    el_object = Body(my_stuff)
    el_object.append(more_stuff)
    with open('test1', 'w') as out_file:
        el_object.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('\n<body>')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents

def test_render_non_strings():
    my_stuff = 'any string I like'
    el_object = Element(Body(my_stuff))
    with open('test3', 'w') as out_file:
        el_object.render(out_file)
    with open('test3', 'r') as in_file:
        contents = in_file.read()
    assert my_stuff in contents

def test_head_tag():
    newobj = Head()
    assert newobj.tag == 'head'


def test_title_tag():
    assert Title().tag == 'title'


def test_title_render():
    my_stuff= 'bye bye ms american pie'
    titleobj = Title(my_stuff)
    more_stuff = ' drove my chevy to the levy'
    titleobj.append(more_stuff)
    with open('test2', 'w') as out_file:
        titleobj.render(out_file)
    with open('test2', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('\n<title>')
    assert contents.endswith('</title>')
    assert my_stuff in contents
    assert more_stuff in contents
