import html_render as ht

def test_new_Element():
    el_object = ht.Element()
    el_object = ht.Element('content')


def test_add_content():
    el_object = ht.Element()
    assert el_object.content == []


def test_adding_empty_string():
    el_object = ht.Element('')
    assert el_object.content == ['']


def test_append_string():
    el_object = ht.Element('spam, spam. spam')
    el_object.append(', wonderful spam')
    assert el_object.content == ['spam, spam. spam', ', wonderful spam']


def test_tag_exists():
    assert ht.Html.tag == 'html'
    el_object = ht.Html('spam, spam, spam')
    assert el_object.tag == 'html'


def test_indent_exists():
    assert ht.Element.indent == ''


def test_Redner():
    my_stuff = 'spam, spam, spam'
    el_object = ht.Html(my_stuff)
    more_stuff = 'eggs, eggs, eggs'
    el_object.append(more_stuff)
    with open('test1', 'w') as out_file:
        el_object.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<!DOCTYPE html>')
    assert contents.endswith('</html>\n')
    assert my_stuff in contents
    assert more_stuff in contents


def test_body_tag():
    assert ht.Body.tag == 'body'


def test_p_tag():
    assert ht.P.tag == 'p'


def test_HMTL_tag():
    assert ht.Html.tag == 'html'


def test_Head_tag():
    assert ht.Head.tag == 'head'


def test_element_attribute():
    el_object = ht.Element(title='test')


def test_element_content():
    return ht.Element('test')


from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr
# reloading in case you are running this in iPython
#  -- we want to make sure the latest version is used
import importlib
importlib.reload(hr)


# writing the file out:
def render_page(page, filename):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    page.render(f, "    ")

    f.seek(0)

    print(f.read())

    f.seek(0)
    open(filename, 'w').write(f.read())


# # Step 8
# ########

page = hr.Html()


head = hr.Head()
head.append( hr.Meta(charset="UTF-8") )
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append( hr.H(2, "PythonClass - Class 6 example") )

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
                 style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())

list = hr.Ul(id="TheList", style="line-height:200%")

list.append( hr.Li("The first item in a list") )
list.append( hr.Li("This is the second item", style="color: red") )

item = hr.Li()
item.append("And this is a ")
item.append( hr.A("http://google.com", "link") )
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output.html")

