#!/usr/bin/env python

import kwa_ex


def test_default():
    result = kwa_ex.func()

    assert result == ('red', 'blue', 'yellow', 'green')

def test_pos():
    result = kwa_ex.func('red', 'blue', 'yellow', 'chartreuse')

    assert result == ('red', 'blue', 'yellow', 'chartreuse')

def test_kw():
    result = kwa_ex.func(link_color='red', back_color='blue')

    assert result == ('red', 'blue', 'red', 'green')

def test_pk():
    result = kwa_ex.func('purple', link_color='red', back_color='blue')

    assert result == ('purple', 'blue', 'red', 'green')

def test_td():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = kwa_ex.func(*regular, **links)

    assert result == ('red', 'blue', 'chartreuse', 'green')

def test_func2_empty():
    result = kwa_ex.func2()

    assert result == ((), {})

def test_func2_empty():
    result = kwa_ex.func2()

    assert result == ((), {})
