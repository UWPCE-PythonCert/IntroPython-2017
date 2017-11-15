"""
Kathryn Egan
"""
from html_render import Element
from html_render import Body
from html_render import Paragraph


def test_new_element():
    element1 = Element()
    assert element1.content == []
    element2 = Element('content')
    assert element2.content == ['content']


def test_add_content():
    element = Element('content')
    element.add_content('more content')
    assert element.content == ['content', 'more content']


def test_render():
    element = Element('stuff')
    element.add_content('more stuff')
    element.add_content('stuffy stuff')
    with open('test1', 'w') as out_file:
        element.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert 'stuff' in contents


def test_html():
    assert HTML.tag == 'html'


def test_body():
    assert Body.tag == 'body'


def test_paragraph():
    assert Paragraph.tag == 'p'
