#!/usr/bin/env python


import os
from io import StringIO

from html_render import Element, Body, P, Html, Head, Title, Hr, Br, A, H,\
    Ul, Li, Doc, Meta


# test utilities

def render_element_file(element, filename='temp_render_file.html',
                        remove=False):
    """
    renders an element, and returns what got rendered

    This version uses an actual file on disk -- yu may want to use it so you
    can see the file afterward.

    :param element: the element to be rendered (its render() method will
     be called)

    :param filename='temp_render_file.html': the name of the temporary file
     to be used.

    :param remove=True: Whether to remove the file after using it to render.
                        Set this to True if you want to be able to look at
                        after the tests run.

    NOTE: - this could be refactored, and still used everywhere.
    """
    with open(filename, 'w') as out_file:
        element.render(out_file)
    with open(filename, 'r') as in_file:
        contents = in_file.read()
    if remove:
        os.remove(filename)
    return contents


def render_element(element, cur_ind=""):
    # this version uses a StringIO object, to keep it all in memory
    """
    renders an element, and returns what got rendered

    This can be used by multiple tests.

    :param element: the element to be rendered (its render() method will be
     called)

    :param filename='temp_render_file.html': the name of the temporary file
     to be used.

    :param remove=True: Whether to remove the file after using it to render.
                        Set this to True if you want to be able to look at
                         after the tests run.

    NOTE: - this could be refactored, and still used everywhere.
    """
    sio = StringIO()
    element.render(sio, cur_ind)
    # if remove:
    #     os.remove(filename)
    return sio.getvalue()


def test_new_element():
    """
    not much here, but it shows Elements can be initialized
    """
    el_object = Element()
    el_object2 = Element('content')


# careful here -- this is testing internal implimentations
# sometimes helpful as you are developing, but you may want to remove
# these tests once you have more working.
# def test_add_content():
#     el_object = Element('content')
#     assert hasattr(el_object.content, 'render')

#     el_object = Element()
#     assert el_object.content == []


# def test_adding_empty_string():
#     el_object = Element('')
#     assert el_object.content == ['']


# def test_append_string():
#     el_object = Element('spam, spam, spam')
#     el_object.append(', wonderful spam')
#     assert el_object.content == ['spam, spam, spam', ', wonderful spam']


# def test_tag_exists():
#     assert Element.tag == 'html'
#     el_object = Element('spam, spam, spam')
#     assert el_object.tag == 'html'


# def test_indent_exists():
#     assert Element.indent == '  '


# Now we get tot he real "meat" of the tests --does the code do what
# it is supposed to do?
def test_render():
    my_stuff = 'spam, spam, spam'
    el_object = Element(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object).strip()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


# you want to be careful with these:
# It is testing an implementation detail, which is less than ideal.
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

# finally! a really good test.
# This is an actual element that we want to render
# so whatever the implimentation deatails, it's working.
def test_render_body():
    my_stuff = 'spam, spam, spam'
    el_object = Body(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object).strip()
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_para():
    my_stuff = 'spam, spam, spam'
    p = P(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    p.append(more_stuff)
    contents = render_element(p).strip()
    assert contents.startswith('<p>')
    assert contents.endswith('</p>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_html():
    my_stuff = 'spam, spam, spam'
    el_object = Html(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    contents = render_element(el_object)
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_non_strings():
    # this is creating a html page with a single body() element in it
    # and a string inside that.
    el_object = Html(Body('any string I like'))

    contents = render_element(el_object)
    # make sure extra whitespace at beginning or end doesn't mess things up.
    contents = contents.strip()

    print(contents)  # so we can see what's going on if a test fails

    # so what should the results be?
    # the html tag is the outer tag, so the contents should start and end
    # with that.
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


def test_render_non_strings2():
    """
    Testing nested elements and text, in a more complex way
    """
    html = Html()
    body = Body()
    html.append(body)
    p = P('any string I like')
    p.append('even more random text')
    body.append(p)
    body.append(P('and this is a different string'))
    contents = render_element(html).strip()

    print(contents)  # so we can see what's going on if a test fails

    # so what should the results be?
    # the html tag is the outer tag, so the contents should start and end
    # with that.
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')

    # the body tags had better be there too
    assert '<body>' in contents
    assert '</body' in contents

    # and two <p> tags
    assert contents.count('<p>')

    # we want the text, too:
    assert 'any string I like' in contents
    assert 'even more random text' in contents
    assert 'and this is a different string' in contents

    # you could, of course, test much more..but hopefully other things are
    # tested, too.


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_element(html, cur_ind="   ")

    print(file_contents)
    lines = file_contents.split("\n")

    assert lines[0].startswith("   <")
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Html("some content")
    file_contents = render_element(html, cur_ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    print(lines)
    assert lines[1].startswith(Element.indent)
    # assert False


def test_multiple_indent():
    """
    make sure multiple levels get indented properly
    """
    body = Body()
    body.append(P("some text"))
    body.append(P("even more text"))
    html = Html(body)

    file_contents = render_element(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):
        assert lines[i].startswith(i * Element.indent + "<")
    assert lines[3].startswith(3 * Element.indent + "some")
    assert lines[4].startswith(2 * Element.indent + "</p>")
    assert lines[5].startswith(2 * Element.indent + "<p>")
    assert lines[6].startswith(3 * Element.indent + "even ")
    for i in range(3):
        assert lines[-(i + 1)].startswith(i * Element.indent + "<")


def test_title():
    """
    This will implicitly test the OneLineTag element
    """
    t = Title("Isn't this a nice title?")

    # making sure indentation still works
    file_contents = render_element(t, cur_ind="     ")

    print(file_contents)
    # no "strip()" -- making sure there are no extra newlines
    assert file_contents.startswith("     <title>I")
    assert file_contents.endswith("?</title>")
    # the only newline should be at the end


def test_head():
    """
    testing Head with a title in it -- it should never be blank
    """
    h = Head()
    h.append(Title("A nifty title for the page"))
    file_contents = render_element(h, cur_ind='   ')

    print(file_contents)
    assert file_contents.startswith("   <head>")
    assert file_contents.endswith("   </head>")

    assert "<title>" in file_contents
    assert "</title>" in file_contents
    assert "A nifty title for the page" in file_contents


def test_full_page_with_title():
    """
    not much to actually test here, but good to see it put together.

    everything should have already been tested.
    """
    page = Html()

    head = Head()
    head.append(Title("PythonClass Example"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of"
                  " them, but this is enough  to show that we can do some"
                  " text"))
    body.append(P("And here is another piece of text -- you should be able"
                  " to add any number"))

    page.append(body)

    file_contents = render_element(page)

    print(file_contents)

    # uncomment this to see results
    # assert False


def test_single_attribute():
    # <p style="text-align: center; font-style: oblique;">
    #        Here is a paragraph of text -- there could be more of them,
    # but this is enough  to show that we can do some text</p>
    p = P("Here is a paragraph of text",
          style="text-align: center; font-style: oblique;")

    results = render_element(p)

    assert results.startswith(
        '<p style="text-align: center; font-style: oblique;">')

    print(results)
    # assert False


def test_multiple_attributes():
    # <p style="text-align: center; font-style: oblique;">
    #             Here is a paragraph of text -- there could
    # be more of them, but this is enough  to show that we can do some text
    #         </p>
    p = P("Here is a paragraph of text",
          id="fred",
          color="red",
          size="12px",
          )

    results = render_element(p)
    print(results)

    lines = results.split('\n')
    assert lines[0].startswith('<p ')
    assert lines[0].endswith('"> ')
    assert 'id="fred"' in lines[0]
    assert 'color="red"' in lines[0]
    assert 'size="12px"' in lines[0]


def test_multiple_attributes_title():
    t = Title("Here is a paragraph of text",
              id="fred",
              color="red",
              size="12px",
              )

    results = render_element(t)
    print(results)

    lines = results.split('\n')
    assert lines[0].startswith('<title ')
    assert lines[0].endswith('</title>')
    assert 'id="fred"' in lines[0]
    assert 'color="red"' in lines[0]
    assert 'size="12px"' in lines[0]


# test class attribute
def test_class_attribute():
    atts = {"id": "fred",
            "class": "special",
            "size": "12px",
            }
    p = P("Here is a paragraph of text",
          **atts)

    results = render_element(p)
    print(results)

    lines = results.split('\n')
    assert lines[0].startswith('<p ')
    assert lines[0].strip().endswith('">')
    assert 'id="fred"' in lines[0]
    assert 'class="special"' in lines[0]
    assert 'size="12px"' in lines[0]


def test_hr_single_attribute():
    hrule = Hr(align="left")
    results = render_element(hrule)
    print(results)
    assert results.startswith('<hr align="left">')
    # assert False


def test_hr_multiple_attributes():
    hrule = Hr(align="left",
               width="50%",
               )
    results = render_element(hrule)
    print(results)
    assert results.startswith('<hr align="left" width="50%">')


def test_br():
    br = Br()
    results = render_element(br)
    print(results)
    assert results.startswith('<br>')
    # assert False


def test_anchor_single_attribute():
    a = A("http://google.com", "link to google")
    results = render_element(a)
    print(results)
    assert results.startswith('<a href="http://google.com">link to google</a')
    # assert False


def test_heading1_with_one_attribute():
    heading = H(1, "Heading 1", align="left")
    results = render_element(heading)
    assert results.startswith('<h1 align="left">Heading 1</h1>')
    print(results)
    # assert False


def test_unordered_list_with_one_attribute():
    unord_list = Ul(align="left")
    results = render_element(unord_list)
    print(results)
    assert results.startswith('<ul align="left"> \n</ul>')


def test_list_tag_with_one_attribute():
    li = Li(align="left")
    results = render_element(li)
    print(results)
    assert results.startswith('<li align="left"> \n</li>')


def test_doc_type():
    doc = Doc("something")
    results = render_element(doc)
    print(repr(results))
    assert results.startswith('!DOCTYPE html\n<html> \n    something\n</html>')
    # assert False


def test_meta_single_attribute():
    meta_tag = Meta(charset="UTF-8")
    results = render_element(meta_tag)
    print(results)
    assert results.startswith('<meta charset="UTF-8">')
    # assert False
