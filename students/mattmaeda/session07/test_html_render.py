#!/usr/bin/env python3
""" Unit tests for html_render.py
"""
from io import StringIO
import html_render as hr
import os
import pytest

TEST_RENDER_NO_INDENT = """<tag>
First line
</tag>
<tag>
Second line
</tag>
<tag>
Third line
</tag>
"""

TEST_RENDER_INDENT = """<tag>
    First line
</tag>
<tag>
    Second line
</tag>
<tag>
    Third line
</tag>
"""


def test_init():
    """ Test initialization of Element object
    """
    element = hr.Element("New Content")
    assert element.elements == ["New Content"]


def test_init_empty():
    """ Test empty initialization of Element object
    """
    element = hr.Element()
    assert element.elements == []


def test_render_no_indent():
    """ Test rendering of file with no indent
    """
    element = hr.Element("First line")
    element.append("Second line")
    element.append("Third line")

    f = StringIO()
    element.render(f, "")

    f.seek(0)
    assert f.read() == TEST_RENDER_NO_INDENT


def test_render_4_indent():
    """ Test rendering of file with indentation
    """
    element = hr.Element("First line")
    element.append("Second line")
    element.append("Third line")

    f = StringIO()

    element.render(f, "    ")
    f.seek(0)
    assert f.read() == TEST_RENDER_INDENT


def test_html_render():
    """ Test rendering of html element
    """
    html = hr.Html("This is my content")

    f = StringIO()
    html.render(f, "    ")

    f.seek(0)
    assert f.read() == "<html>\n    This is my content\n</html>\n"


def test_body_render():
    """ Test rendering of body element
    """
    body = hr.Body("This is my body content")

    f = StringIO()
    body.render(f, "    ")

    f.seek(0)
    assert f.read() == "<body>\n    This is my body content\n</body>\n"


def test_p_render():
    """ Test rendering of a paragraph element
    """
    p = hr.P("This is my paragraph content")

    f = StringIO()
    p.render(f, "    ")

    f.seek(0)
    assert f.read() == "<p>\n    This is my paragraph content\n</p>\n"


def test_oneline_tag():
    """ Test rendering of a one line tag element
    """
    one = hr.OneLineTag("This is my oneliner")

    f = StringIO()
    one.render(f, "    ")

    f.seek(0)
    assert f.read() == "    <tag>This is my oneliner</tag>\n"


def test_title_tag():
    """ Test rendering of a title element
    """
    title = hr.Title("This is my title")

    f = StringIO()
    title.render(f, "    ")

    f.seek(0)
    assert f.read() == "    <title>This is my title</title>\n"


def test_element_attributes():
    """ Test rendering of an element with attributes
    """
    elem = hr.Element("test content", style="my-style")

    f = StringIO()
    elem.render(f, "    ")

    f.seek(0)
    assert f.read() == '<tag style="my-style">\n    test content\n</tag>\n'


def test_hr_element():
    """ Test rendering of hr element
    """
    h = hr.Hr()

    f = StringIO()
    h.render(f, "    ")

    f.seek(0)
    assert f.read() == "    <hr />\n"


def test_br_element():
    """ Test rendering of br element
    """
    h = hr.Br()

    f = StringIO()
    h.render(f, "    ")

    f.seek(0)
    assert f.read() == "    <br />\n"


def test_link_element():
    """ Test rendering of a element
    """
    a = hr.A("http://google.com", "Google")

    f = StringIO()
    a.render(f, "    ")

    f.seek(0)
    assert f.read() == '    <a href="http://google.com">Google</a>\n'


def test_h_level_element():
    """ Test rendering of h1 element
    """
    h = hr.H(1, "Level 1")

    f = StringIO()
    h.render(f, "    ")

    f.seek(0)
    assert f.read() == "    <h1>Level 1</h1>\n"


def test_h_level_two_element():
    """ Test rendering of h2 element
    """
    h = hr.H(2, "Level Two")

    f = StringIO()
    h.render(f, "    ")

    f.seek(0)
    assert f.read() == "    <h2>Level Two</h2>\n"
