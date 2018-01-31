import html_render
from html_render import Element, Body, P, Html, Head, Title
from io import StringIO


def render_element_file(element, filename='temp_render_file.html', remove=False):
    with open(filename, 'w') as out_file:
        element.render(out_file)
    with open(filename, 'r') as in_file:
        contents = in_file.read()
    if remove:
        os.remove(filename)
    return contents

def render_element(element, cur_ind=""):
    sio = StringIO()
    element.render(sio, current_ind=cur_ind)
    return sio.getvalue()

def test_new_element():
    el_object = html_render.Element()
    el_object = html_render.Element('content')


def test_add_content():
    el_object = html_render.Element('content')
    print(el_object.content)
    el_object = html_render.Element()
    assert el_object.content == []

def test_empty_string():
    el_object = html_render.Element('')
    print(el_object.content)
    assert el_object.content == ['']

def test_append():
    el_object = html_render.Element('nerp')
    el_object.append('Ma derp')
    assert el_object.content == ['nerp','Ma derp']

def test_tag_exists():
    assert Element.tag == 'html'
    el_object = html_render.Element('nerp')
    assert el_object.tag == 'html'

def test_indent_exists():
    assert Element.indent == '   '

def test_render():
    my_stuff = 'nerp'
    more_stuff = 'eggs, eggs, eggs'
    el_object = html_render.Element('nerp')
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
    assert Body.tag == 'body'

def test_para_tag():
    assert P.tag == 'p'

def test_html_tag():
    assert Html.tag == 'html'

def test_render_page():
    my_stuff = 'nerp'
    more_stuff = 'eggs, eggs, eggs'
    el_object = Body(my_stuff)
    el_object.append(more_stuff)
    with open('test1', 'w') as out_file:
        el_object.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read() 
        assert contents.startswith('<body>')
        assert contents.endswith('</body>')
        assert my_stuff in contents
        assert more_stuff in contents

def test_render_non_strings():
    el_object = Html(Body('any string i like'))
    contents = render_element(el_object)
    content = contents.strip()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')