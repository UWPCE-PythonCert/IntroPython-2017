# break_me test
# Python 3.6


import pytest
import break_me


def test_name_error():
    with pytest.raises(NameError):
        break_me.name_error()


def test_type_error():
    with pytest.raises(TypeError):
        break_me.type_error()


def test_syntax_error():
    with pytest.raises(SyntaxError):
        break_me.syntax_error()


def test_attribute_error():
    with pytest.raises(AttributeError):
        break_me.attribute_error()
