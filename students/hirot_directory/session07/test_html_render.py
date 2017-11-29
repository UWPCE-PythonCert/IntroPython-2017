#!/usr/bin/env python


import os

from html_render import Element, Body, Para, HTML, OneLineTag, Title, head, SelfClosingTag, Horizontal, LineBreak

# test utilities


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
        element.render(out_file)
    with open(filename, 'r') as in_file:
        contents = in_file.read()
    # NOTE: you could comment out this if you want to see the file.
    if remove:
        os.remove(filename)
    return contents


def test_new_element():
    el_object = Element()
    el_object2 = Element('content')


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
    assert el_object.content == ['spam, spam, spam', ', wonderful spam']


def test_tag_exists():
    assert Element.tag == 'html'
    el_object = Element('spam, spam, spam')
    assert el_object.tag == 'html'


def test_indent_exists():
    assert Element.ind == '  '


def test_render():
    my_stuff = 'spam, spam, spam'
    el_object = Element(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object)
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents



# you want to be careful with these:
# It is testing an implementation detail, which is less than idea.
#  sometimes in TDD, it's helpful to have quickies tests of
#  implementation details so you can see that partially written code
#  is working -- but if/when you can test actual functionality, that's
#  better. In this case, once we have a render() method, we can test
#  that the tag gets rendered properly, so don't need to test if the
#  tag attribute is correct.

# def test_body_tag():
#    assert Body.tag == 'body'

# def test_p_tag():
#     assert Para.tag == 'p'


# def test_html_tag():
#     assert HTML.tag == 'html'


def test_render_body():
    my_stuff = 'spam, spam, spam'
    el_object = Body(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object)
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_para():
    my_stuff = 'spam, spam, spam'
    el_object = Para(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object)
    assert contents.startswith('<p>')
    assert contents.endswith('</p>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_html():
    my_stuff = 'spam, spam, spam'
    el_object = HTML(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object)
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_non_strings():
    # this is crating a html page with a single body() element in it
    el_object = HTML(Body('any string I like'))

    contents = render_element(el_object, remove=False) # adding remove=False to see the output
    # make sure extra whitespace at beginning or end doesn't mess things up.
    contents = contents.strip()

    print(contents)  # so we can see what's going on if a test fails

    # so what should the results be?
    # the html tag is the outer tag, so the contents should start and end with that.
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')

    # the body tags had better be there too
    assert '<body>' in contents
    assert '</body' in contents

    # we want the tesxt, too:
    assert 'any string I like' in contents

    # now lets get pretty specific:
    # the opening tag should come before the ending tag
    assert contents.index('<body>') < contents.index('</body>')
    # the opening tag should come before the content
    assert contents.index('<body>') < contents.index('any string')


def test_indent():
        # this is crating a html page with a single body() element in it
    el_object = Para('any string I like')

    contents = render_element(el_object, remove=False) # adding remove=False to see the output
    # make sure extra whitespace at beginning or end doesn't mess things up.
    contents = contents.strip()

    print(contents)  # so we can see what's going on if a test fails

    lines = contents.split('\n')

    print(lines)

    assert len(lines) == 3
    assert lines[1].startswith(''+'any') # Element.ind+'any'


def test_indent_nested():
        # this is crating a html page with a single body() element in it
    el_object = Para('any string I like')

    filename = 'anything.html'

    with open(filename, 'w') as out_file:
        el_object.render(out_file, ind='  ')
    with open(filename, 'r') as in_file:
        contents = in_file.read()

    print(contents)

    lines = contents.split('\n')

    # assert len(lines) == 3
    assert lines[0].startswith('  <')
    assert lines[1].startswith('  ' + Element.ind)
    assert lines[2].startswith('  <')

# def test_indent_nested():
#         # this is crating a html page with a single body() element in it
#     el_object = HTML(Body(Para('any string I like')))

#     contents = render_element(el_object, remove=False) # adding remove=False to see the output
#     # make sure extra whitespace at beginning or end doesn't mess things up.
#     contents = contents.strip()

#     print(contents)  # so we can see what's going on if a test fails

#     lines = contents.split('\n')

#     print(lines)

#     # assert len(lines) == 3
#     assert lines[1].startswith(Element.indent) # body opening
#     assert lines[2].startswith(Element.indent*2) # p opening
#     assert lines[3].startswith(Element.indent*3+'any') # content
#     assert lines[4].startswith(Element.indent*2) # p closing
#     assert lines[5].startswith(Element.indent) # body closing

def test_OneLineTag():
        # this is crating a html page with a single body() element in it
    el_object = Title('')

    contents = render_element(el_object, remove=False) # adding remove=False to see the output
    # make sure extra whitespace at beginning or end doesn't mess things up.
    contents = contents.strip()

    print(contents)  # so we can see what's going on if a test fails

    assert contents.startswith('<') # Element.ind+'any'
    assert contents.endswith('>')


def test_Horizontal():
    pass


def test_LineBreak():
    pass

