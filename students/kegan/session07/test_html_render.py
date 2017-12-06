"""
Kathryn Egan
Suite of tests for components of html_render.py
"""
import io
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


def test_indent():
    html = Html()
    body = Body()
    p = P()
    p.append('some text')
    body.append(p)
    html.append(body)
    outfile = io.StringIO()
    html.render(outfile)
    output = outfile.getvalue().strip().split('\n')
    assert output[0] == '<!DOCTYPE html>'
    assert output[1] == html.indent + '<html>'
    assert output[-1] == html.indent + '</html>'
    assert output[2] == html.indent * 2 + '<body>'
    assert output[-2] == html.indent * 2 + '</body>'
    assert output[3] == html.indent * 3 + '<p>'
    assert output[-3] == html.indent * 3 + '</p>'
    assert output[4] == html.indent * 4 + 'some text'


def test_render():
    html = Html()
    html.append('some content')
    outfile = io.StringIO()
    html.render(outfile)
    output = outfile.getvalue()
    assert output.startswith('<!DOCTYPE html>')
    assert '<html>' in output
    assert '</html>' in output
    assert 'some content' in output


def test_attrs():
    attrs = {'class': 'intro'}
    html = Html(**attrs)
    assert 'class' in html.attrs
    assert html.attrs['class'] == 'intro'
    outfile = io.StringIO()
    html.render(outfile)
    output = outfile.getvalue()
    assert '<html class="intro">' in output
    assert '</html class="intro">' not in output


def test_one_line_tag():
    title = Title('the title')
    outfile = io.StringIO()
    title.render(outfile)
    assert outfile.getvalue().strip() == '<title>the title</title>'


def test_self_closing_tag():
    hr = Hr()
    outfile = io.StringIO()
    hr.render(outfile)
    assert outfile.getvalue().strip() == '<hr />'


def test_link():
    a = A('www.google.com', 'google', color='blue', style='bold')
    outfile = io.StringIO()
    a.render(outfile)
    assert (
        '<a color="blue" style="bold" href="www.google.com">'
        in outfile.getvalue())


def test_header():
    h1 = H(138, 'header', style="italic")
    outfile = io.StringIO()
    h1.render(outfile)
    assert '<h138 style="italic">header</h138>' in outfile.getvalue()


def test_meta():
    head = Head()
    head.append(Meta(charset='UTF-8'))
    outfile = io.StringIO()
    head.render(outfile)
    output = outfile.getvalue().strip().split('\n')
    assert output[0].strip() == '<head>'
    assert output[-1].strip() == '</head>'
    assert output[1].strip() == '<meta charset="UTF-8" />'