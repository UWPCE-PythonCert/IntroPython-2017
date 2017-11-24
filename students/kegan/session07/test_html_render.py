"""
Kathryn Egan
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


def check_render(html, expected):
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
        '<html>',
        '    <body>',
        '        <p>',
        '            paragraph 1',
        '        </p>',
        '        <p>',
        '            paragraph 2',
        '        </p>',
        '    </body>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_one_line_tag():
    html = Html()
    html.append(Title('this is the title'))
    elements = [
        '<html>',
        '    <title>this is the title</title>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_self_closing_tag():
    html = Html()
    html.append(Hr())
    html.append(Br())
    elements = [
        '<html>',
        '    <hr />',
        '    <br />',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_attrs1():
    html = Html()
    attrs = {'class': 'intro', 'font': 'Arial'}
    html.append(P('paragraph', **attrs))
    elements = [
        '<html>',
        '    <p class="intro" font="Arial">',
        '        paragraph',
        '    </p>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_attrs2():
    html = Html()
    attrs = {'style': 'bold'}
    html.append(Title('title', **attrs))
    elements = [
        '<html>',
        '    <title style="bold">title</title>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_attrs3():
    html = Html()
    html.append(Hr(style="dashed"))
    elements = [
        '<html>',
        '    <hr style="dashed" />',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_link():
    html = Html()
    body = Body()
    body.append('let me')
    body.append(A('https://www.tutorialspoint.com/html/', 'google'))
    body.append('that for you')
    html.append(body)
    elements = [
        '<html>',
        '    <body>',
        '        let me',
        '        <a href="https://www.tutorialspoint.com/html/">google</a>',
        '        that for you',
        '    </body>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_list():
    html = Html()
    ul = Ul(id='MyList')
    ul.append(Li('first item'))
    ul.append(Li('second item'))
    html.append(ul)
    elements = [
        '<html>',
        '    <ul id="MyList">',
        '        <li>',
        '            first item',
        '        </li>',
        '        <li>',
        '            second item',
        '        </li>',
        '    </ul>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)


def test_header():
    html = Html()
    html.append(Header(1, 'My Header'))
    html.append(Header(2, 'Second Header'))
    elements = [
        '<html>',
        '    <h1>My Header</h1>',
        '    <h2>Second Header</h2>',
        '</html>']
    expected = '\n'.join(elements) + '\n'
    check_render(html, expected)

