#!/usr/bin/env python

'''
This is the testing file for 'html_render.py' program
'''

import html_render2
from html_render2 import Element, Body, Para, Html, Head, OneLineTag, Title

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
	assert Element.indent == ''

def test_render():
	my_stuff = 'spam, spam, spam'
	el_object = Element(my_stuff)
	more_stuff = ', eggs, eggs, eggs'
	el_object.append(more_stuff)
	with open('test_render_output.html', 'w') as out_file:
		el_object.render(out_file)
	with open('test_render_output.html', 'r') as in_file:
		contents = in_file.read()
	assert contents.startswith('<!DOCTYPE html>\n')
	assert contents.endswith('</html>')
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
	assert contents.startswith('        <body>')
	assert contents.endswith('        </body>')
	assert my_stuff in contents
	assert more_stuff in contents

def test_render_non_strings():
    # This is crating a html page with a single body() element in it
    el_object = Html(Body('spam, spam, spam, wonderful spam'))
    with open('test_render_non_strings_output.html', 'w') as out_file:
    	el_object.render(out_file)
    with open('test_render_non_strings_output.html', 'r') as in_file:
    	contents = in_file.read()
    # Make sure extra whitespace at beginning or end doesn't mess things up.
    contents = contents.strip()

    print(contents)  # To see what's going on if a test fails

    # Ensure the file begins with 'DOCTYPE' tag per the example
    assert contents.startswith('<!DOCTYPE html>')
    assert contents.endswith('</html>')

    # Validates the 'body' tag is in the file
    assert '<body>' in contents
    assert '</body>' in contents

    # Validates sample text is in the file
    assert 'spam, spam, spam, wonderful spam' in contents

    # The opening tag should come before the ending tag
    assert contents.index('<body>') < contents.index('</body>')
    # The opening tag should come before the content
    assert contents.index('<body>') < contents.index('wonderful spam')

def test_render_hbp():
    '''
    This test renders an HTML file with properly formed 'head', 'body',
    and 'para' tags within it.
    '''
    el_object = Html(Head(Body(Para('spam, spam, spam, wonderful spam'))))
    with open('test_render_hbp_output.html', 'w') as out_file:
    	el_object.render(out_file)
    with open('test_render_hbp_output.html', 'r') as in_file:
    	contents = in_file.read()
    # Make sure extra whitespace at beginning or end doesn't mess things up.
    contents = contents.strip()

    print(contents)  # To see what's going on if a test fails

    # Ensure the file begins with 'DOCTYPE' tag per the example
    assert contents.startswith('<!DOCTYPE html>')
    assert contents.endswith('</html>')

    # Validates the 'Body' tag is in the file
    assert '<body>' in contents
    assert '</body>' in contents

    # Validates the 'Para' tag is in the file
    assert '<p>' in contents
    assert '</p>' in contents

    # Validates the 'Head' tag is in the file
    assert '<head>' in contents
    assert '</head>' in contents

    # Validates sample text is in the file
    assert 'spam, spam, spam, wonderful spam' in contents

    # The opening tag should come before the ending tag
    assert contents.index('<p>') < contents.index('</p>')
    # The opening tag should come before the content
    assert contents.index('<p>') < contents.index('wonderful spam')
    # The next two assertions validate the 'Head' tags remain above the 'Body'
    assert contents.index('<head>') < contents.index('<body>')
    assert contents.index('</head>') < contents.index('<body>')
    # The next two assertions validate the 'Para' tags are nested within the 'Body'
    assert contents.index('<body>') < contents.index('<p>')
    assert contents.index('</p>') < contents.index('</body>')

def test_onelinetag():
	el_object = OneLineTag('PythonClass - Session 6 example')
	assert el_object.content == ['PythonClass - Session 6 example']

def test_title_tag():
	assert Title.tag == 'title'

#def test_title_render():
#    '''
#    This test renders an HTML file with properly formed 'title', 'head', 'body',
#    and 'para' tags within it.
#    '''
#    words = 'spam, spam, spam, wonderful spam'
#    words2 = 'PythonClass = Revision 1087:'
#    el_object2 = Head(Title(words2))
#    el_object = Body(Para(words))
#    with open('test_title_render_output.html', 'w') as out_file:
#    	el_object2.render(out_file)
#    	el_object.render(out_file)
#    with open('test_title_render_output.html', 'r') as in_file:
#    	contents = in_file.read()
    # Make sure extra whitespace at beginning or end doesn't mess things up.
#    contents = contents.strip()

#    print(contents)  # To see what's going on if a test fails

    # Ensure the file begins with 'DOCTYPE' tag per the example
 #   assert contents.startswith('<!DOCTYPE html>')
 #   assert contents.endswith('</html>')

    # Validates the 'Body' tag is in the file
 #   assert '<body>' in contents
 #   assert '</body>' in contents

    # Validates the 'Para' tag is in the file
 #   assert '<p>' in contents
 #   assert '</p>' in contents

    # Validates the 'Head' tag is in the file
 #   assert '<head>' in contents
 #   assert '</head>' in contents

    # Validates sample text is in the file
 #   assert 'spam, spam, spam, wonderful spam' in contents

    # The opening tag should come before the ending tag
 #   assert contents.index('<p>') < contents.index('</p>')
    # The opening tag should come before the content
 #   assert contents.index('<p>') < contents.index('wonderful spam')
    # The next two assertions validate the 'Head' tags remain above the 'Body'
 #   assert contents.index('<head>') < contents.index('<body>')
 #   assert contents.index('</head>') < contents.index('<body>')
    # The next two assertions validate the 'Para' tags are nested within the 'Body'
 #   assert contents.index('<body>') < contents.index('<p>')
 #   assert contents.index('</p>') < contents.index('</body>')

#def test_adding_empty_string():
#	el_object = Element('')
#	assert el_object.content == ['']

