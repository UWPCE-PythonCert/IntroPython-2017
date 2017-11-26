import html_render
from html_render import Element, Body, Para, Html

def test_new_element():
    el_object = Element()
    el_objec2 = Element('content')

def test_add_content():
    el_object = Element('content')
    el_object = Element()
    assert el_object.content == []

def test_adding_empty_string():
    el_object = Element('')
    assert el_object.content == ['']

def test_append_string():
    el_object = Element('spam, spam, spam')
    el_object.append(', wonderful spam')
    el_object.content == ['spam, spam, spam', ', wonderful spam']

def test_tag_exists():
    assert Element.tag == 'html'
    el_object = Element('spam, spam, spam')
    assert el_object.tag == 'html'

def test_indent_exists():
    assert Element.indent == '  '

def test_reder():
    mystuff = 'spam, spam, spam'
    el_object = Element(mystuff)
    morestuff = 'eggs, eggs, eggs'
    el_object.append(morestuff)
    with open('text1.htm', 'w') as out_file:
        el_object.render(out_file)
    with open('text1.htm', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert mystuff in contents
    assert morestuff in contents

def test_body_tag():
    assert Body.tag == 'body'

def test_p_tag():
    assert Para.tag == 'p'

def test_html_tag():
    assert Html.tag == 'html'

def test_render_body():
    mystuff = 'spam, spam, spam'
    el_object = Body(mystuff)
    morestuff = 'eggs, eggs, eggs'
    el_object.append(morestuff)
    with open('text2.htm', 'w') as out_file:
        el_object.render(out_file)
    with open('text2.htm', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert mystuff in contents
    assert morestuff in contents

#def test_render_non_strings():
#    el_object = Element(Body('some string'))
    