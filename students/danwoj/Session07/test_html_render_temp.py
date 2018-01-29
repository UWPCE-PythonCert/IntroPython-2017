#!/usr/bin/env python

'''
This is the testing file for 'html_render.py' program
'''

import html_render
from html_render import Element, Body, Para, Html

def render_element(element, filename='temp_render_file.html', remove=True):
    """
    renders an element, and returns what got rendered
    This can be used by multiple tests.
    :param element: the element to be rendered (its render() method will be called)
    :param filename='temp_render_file.html': the name of the temporary file to be used.
    :param remove=True: Whether to remove the file after using it to render.
                        Set this to True if you want to be able to look at after
                        the tests run.
    NOTE: - this could be refactored, and still used everywhere.
    """
    with open(filename, 'w') as out_file:
        Element.render(out_file)
    with open(filename, 'r') as in_file:
        contents = in_file.read()
    # NOTE: you could comment out this if you want to see the file.
#    if remove:
#        os.remove(filename)
#    return contents

def test_new_element():
	'''
	This tests if the program can create a new element either with nothing 
	(el_object) or with content (el_object2).
	'''
	el_object = Element()
	el_object2 = Element('content')

def test_add_content():
	'''
	This tests if the program can add content to an element.
	'''
	el_object = Element('content')
	el_object = Element()
	assert el_object.content == []

def test_adding_empty_string():
	el_object = Element('')
	assert el_object.content == ['']

def test_append_string():
	el_object = Element('spam, spam, spam')
	el_object.append(', wonderful spam')
	assert el_object.content == ['spam, spam, spam', ', wonderful spam']

def test_tag_exists():
	assert Element.tag == 'html'
	el_object = Element('spam, spam, spam')
	assert el_object.tag == 'html'

def test_indent_exists():
	assert Element.indent == '  '

def test_render():
	my_stuff = 'spam, spam, spam'
	el_object = Element(my_stuff)
	more_stuff = ', eggs, eggs, eggs'
	el_object.append(more_stuff)
	with open('test_render_output.html', 'w') as out_file:
		el_object.render(out_file)
	with open('test_render_output.html', 'r') as in_file:
		contents = in_file.read()
	assert contents.startswith('<html>\n')
	assert contents.endswith('</html>\n')
	assert my_stuff in contents
	assert more_stuff in contents

def test_body_tag():
	assert Body.tag == 'body'

def test_para_tag():
	assert Para.tag == 'p'

def test_html_tag():
	assert Html.tag == 'html'

def test_render_body():
	my_stuff = 'spam, spam, spam'
	el_object = Body(my_stuff)
	more_stuff = ', eggs, eggs, eggs'
	el_object.append(more_stuff)
	with open('test_render_body_output.html', 'w') as out_file:
		el_object.render(out_file)
	with open('test_render_body_output.html', 'r') as in_file:
		contents = in_file.read()
	assert contents.startswith('<body>\n')
	assert contents.endswith('</body>\n')
	assert my_stuff in contents
	assert more_stuff in contents

#def test_render_non_strings():
#    # this is crating a html page with a single body() element in it
#    el_object = Html(Body('any string I like'))
#    with open('test_render_non_strings_output.html', 'w') as out_file:
#    	el_object.render(out_file)
#    with open('test_render_non_strings_output.html', 'r') as in_file:
#    	contents = in_file.read()
#    # make sure extra whitespace at beginning or end doesn't mess things up.
#    contents = contents.strip()

#    print(contents)  # so we can see what's going on if a test fails

    # so what should the results be?
    # the html tag is the outer tag, so the contents should start and end with that.
#    assert contents.startswith('<html>')
#    assert contents.endswith('</html>')

    # the body tags had better be there too
#    assert '<body>' in contents
#    assert '</body' in contents

    # we want the tesxt, too:
#    assert 'any string I like' in contents

    # now lets get pretty specific:
    # the opening tag should come before the ending tag
#    assert contents.index('<body>') < contents.index('</body>')
    # the opening tag should come before the content
#    assert contents.index('<body>') < contents.index('any string')