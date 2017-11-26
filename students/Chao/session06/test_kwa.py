#!/usr/bin/env python

import kwa_ex

"""
Color function test
"""
# Test default value
def test_default():
    result = kwa_ex.func()

    assert result == ('red', 'blue', 'yellow', 'green')

# Test positional arguments
def test_pos():
    result = kwa_ex.func('red', 'blue', 'yellow', 'chartreuse')

    assert result == ('red', 'blue', 'yellow', 'chartreuse')

# Test keywoord arguments
def test_kw():
    result = kwa_ex.func(link_color='red', back_color='blue')

    assert result == ('red', 'blue', 'red', 'green')

# Test combination of positional and keyword
def test_pk():
    result = kwa_ex.func('purple', link_color='red', back_color='blue')

    assert result == ('purple', 'blue', 'red', 'green')

# Test passing arguments with tuple and dictionary
def test_td():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = kwa_ex.func(*regular, **links)

    assert result == ('red', 'blue', 'chartreuse', 'green')

"""
Color function 2 test with args and kwargs
"""

# Test default value (empty)
def test_func2_empty():
    result = kwa_ex.func2()

    assert result == ((), {})

# Test positoinal argument with args
def test_func2_pos():
    result = kwa_ex.func2('red', 'blue', 'yellow', 'chartreuse')

    assert result == (('red', 'blue', 'yellow', 'chartreuse'), {})

# Test keywoord arguments
def test_fun2_kw():
    result = kwa_ex.func2(link_color='red', back_color='blue')

    assert result == ((), {'link_color': 'red', 'back_color': 'blue'})

# Test combination of positional and keyword
def test_fun2_pk():
    result = kwa_ex.func2('purple', link_color='red', back_color='blue')

    assert result == (('purple',), {'link_color': 'red', 'back_color': 'blue'})

# Test passing arguments with tuple and dictionary
def test_fun2_td():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = kwa_ex.func2(*regular, **links)

    assert result == (('red', 'blue'), {'link_color': 'chartreuse'})
