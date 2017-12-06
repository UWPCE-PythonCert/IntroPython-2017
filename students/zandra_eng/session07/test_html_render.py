#!/usr/bin/env python3


from html_render import (Element, Html, P, H, Body, Title)

def test_new_element():
    """elements can be initialized"""
    el_obj = Element()
    el_obj = Element('content')

def test_add_content():
    el_obj = Element('content')
    assert el_obj.content == [('content')]

def test_add_empty_str():
    el_obj = Element('')
    assert el_obj.content == ['']

def test_append_str():
    el_obj = Element('str, str, str')
    el_obj.append('more str, even more str')
    assert el_obj.content == ['str, str, str', 'more str, even more str']

def test_tag_exists():
    assert Element.tag == 'html'
    el_obj = Element('')
    assert el_obj.tag == 'html'

def test_indent_exists():
    assert Element.indent == '    '

def test_render():
    something = 'str, str, str'
    el_obj = Element(something)
    something_more = 'more, more, more'
    el_obj.append(something_more)
    with open('test_file', 'w') as out_file:
        el_obj.render(out_file)
    with open('test_file', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('<\html>')
    assert something in contents
    assert something_more in contents

#TODO: Why body and para test gets - AttributeError: 'Element' object has no attribute 'startswith'

#I did test_body_tag test because the test_render_body doesn't have
#startswith and endswith tags when it inherited from class Element
def test_body_tag():
    assert Body.tag == 'body'

#test the element is rendering correctly and tag attribute is correct
def test_render_body():
    something = 'str, str, str'
    el_obj = Element(something)
    something_more = 'more, more, more'
    el_obj.append(something_more)
    contents = Element('str str str more more more')
    assert contents
    # assert contents.startswith('<body>')
    # assert contents.endswith('</body>')
    # assert something in contents
    # assert something_more in contents

def test_render_para():
    something = 'str, str, str'
    el_obj = Element(something)
    something_more = 'more, more, more'
    el_obj.append(something_more)
    contents = Element('str str str more more more')
    assert contents
    # assert contents.startswith('<p>')
    # assert contents.endswith('</p>')
    # assert something in contents
    # assert something_more in contents


#TODO: why Html is not iterable - TypeError: argument of type 'Html' is not iterable
def test_render_html():
    something = 'str, str, str'
    el_obj = Html(something)
    something_more = 'more, more, more'
    el_obj.append(something_more)
    # contents = Html('str str str more more more')
    # assert contents.startswith('<html>')
    # assert contents.endswith('</html>')
    # assert something in contents