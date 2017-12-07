#!/usr/bin/env python3


'''
unit tests for py
'''


import html_render
from html_render import Element, Html, P, Body


def test_new_element():
    el_object = Element()
    el_object = Element('stuff and things')
    assert el_object.content == ['stuff and things']

def test_add_content():
    el_object = Element('content')
    el_object = Element()
    assert el_object.content == []

def test_adding_empty_string():
    el_object = Element('')
    assert el_object.content == ['']

def test_append_string():
    el_object = Element('olives and figs')
    el_object.append('pita')
    assert el_object.content == ['olives and figs', 'pita']

def test_tag_exists():
    assert Element.tag == 'html'
    el_object = Element()
    assert el_object.tag == 'html'

def test_indent_exists():
    assert Element.indent == '  '
    el_object = Element()
    assert el_object.indent == '  '

def test_render():
    some_stuff = 'blueberries and raspberries'
    el_object = Element(some_stuff)
    more_stuff = 'strawberries'
    el_object.append(more_stuff)
    with open('test1.txt', 'w') as out_file:
        el_object.render(out_file)
    with open('test1.txt', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert some_stuff in contents
    assert more_stuff in contents


def test_body_tag():
    assert Body.tag == 'body'

def test_para_tag():
    assert P.tag == 'p'

def test_html_tag():
    assert Html.tag == 'html'

def test_render_body():
    some_stuff = 'blueberries and raspberries'
    el_object = Body(some_stuff)
    more_stuff = 'strawberries'
    el_object.append(more_stuff)
    with open('test1.txt', 'w') as out_file:
        el_object.render(out_file)
    with open('test1.txt', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert some_stuff in contents
    assert more_stuff in contents

def test_render_non_strings():
    el_object = Element(Body('blah and foooo'))
    with open('test1.txt', 'w') as out_file:
        el_object.render(out_file)
    with open('test1.txt', 'r') as in_file:
        contents = in_file.read()