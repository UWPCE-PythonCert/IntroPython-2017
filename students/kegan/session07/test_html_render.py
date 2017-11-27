"""
Kathryn Egan

Suite of tests for components of html_render.py
"""
from html_render import *


def test_element_init():
    element = Element()
    assert element.content == []
    element = Element('content')
    assert element.content == ['content']
    element = Element('')
    assert element.content == ['']


def test_append():
    element = Element()
    element.append('content')
    element.append('more content')
    assert element.content == ['content', 'more content']


# def test_render_no_indent():
#     html = Html()
#     html.append(Body('body content'))
#     html.append(P())
#     temp = 'html_test.html'
#     with open(temp, 'w') as f:
#         html.render(f)
#     with open(temp, 'r') as f:
#         assert f.read() == '<html><body>body content</body><p></p></html>'


def prepare(elements):
    """ Generates the HTML output based on given indents and
    elements to compare rendered HTML to.
    Args:
        elements (list of tuples) : indent, element pairs
    Returns:
        str : elements as rendered HTML
    """
    output = '\n'.join([
        '    ' * (indent + 1) + element for indent, element in elements])
    output = '<!DOCTYPE html>\n{}\n'.format(output)
    return output


def check_render(html, expected):
    """ Checks results of rendered HTML against expected output."""
    temp = 'html_test.html'
    with open(temp, 'w') as f:
        html.render(f)
    with open(temp, 'r') as f:
        assert f.read() == expected


def test_render():
    html = Html()
    body = Body()
    body.append(P('paragraph 1'))
    body.append(P('paragraph 2'))
    html.append(body)
    elements = [
        (0, '<html>'),
        (1, '<body>'),
        (2, '<p>'),
        (3, 'paragraph 1'),
        (2, '</p>'),
        (2, '<p>'),
        (3, 'paragraph 2'),
        (2, '</p>'),
        (1, '</body>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_one_line_tag():
    html = Html()
    html.append(Title('this is the title'))
    elements = [
        (0, '<html>'),
        (1, '<title>this is the title</title>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_self_closing_tag():
    html = Html()
    html.append(Hr())
    html.append(Br())
    elements = [
        (0, '<html>'),
        (1, '<hr />'),
        (1, '<br />'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_attrs1():
    html = Html()
    attrs = {'class': 'intro', 'font': 'Arial'}
    html.append(P('paragraph', **attrs))
    elements = [
        (0, '<html>'),
        (1, '<p class="intro" font="Arial">'),
        (2, 'paragraph'),
        (1, '</p>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_attrs2():
    html = Html()
    attrs = {'style': 'bold'}
    html.append(Title('title', **attrs))
    elements = [
        (0, '<html>'),
        (1, '<title style="bold">title</title>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_attrs3():
    html = Html()
    html.append(Hr(style="dashed"))
    elements = [
        (0, '<html>'),
        (1, '<hr style="dashed" />'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_link():
    html = Html()
    body = Body()
    body.append('let me')
    body.append(A('https://www.tutorialspoint.com/html/', 'google'))
    body.append('that for you')
    html.append(body)
    elements = [
        (0, '<html>'),
        (1, '<body>'),
        (2, 'let me'),
        (2, '<a href="https://www.tutorialspoint.com/html/">google</a>'),
        (2, 'that for you'),
        (1, '</body>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_list():
    html = Html()
    ul = Ul(id='MyList')
    ul.append(Li('first item'))
    ul.append(Li('second item'))
    html.append(ul)
    elements = [
        (0, '<html>'),
        (1, '<ul id="MyList">'),
        (2, '<li>'),
        (3, 'first item'),
        (2, '</li>'),
        (2, '<li>'),
        (3, 'second item'),
        (2, '</li>'),
        (1, '</ul>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_header():
    html = Html()
    html.append(H(1, 'My Header'))
    html.append(H(2, 'Second Header'))
    elements = [
        (0, '<html>'),
        (1, '<h1>My Header</h1>'),
        (1, '<h2>Second Header</h2>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)


def test_meta():
    html = Html()
    head = Head()
    head.append(Meta(charset='UTF-8'))
    head.append(Title('Title'))
    html.append(head)
    elements = [
        (0, '<html>'),
        (1, '<head>'),
        (2, '<meta charset="UTF-8" />'),
        (2, '<title>Title</title>'),
        (1, '</head>'),
        (0, '</html>')]
    expected = prepare(elements)
    check_render(html, expected)
