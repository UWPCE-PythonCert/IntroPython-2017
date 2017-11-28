#!/usr/bin/env python3

import kwargs_ex


def test_basic():
    assert True


a = 6
b = 6


def test_basic_fail():
    assert a == b


def test_kw():
    result = kwargs_ex.fun(fore_color='blue',
                           back_color='red',
                           link_color='yellow',
                           visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_new_order():
    result = kwargs_ex.fun('green', 'blue', 'purple', 'red')
    assert result == ('green', 'blue', 'purple', 'red')


def test_kw_tuple():
    tup = ('green',
           'blue',
           'purple',
           'red')
    result = kwargs_ex.fun(*tup)
    # assert result == ('green', 'blue', 'yellow', 'green')
    assert result == tup


def test_kw_dict():
    dic = {'fore_color': 'blue',
           'back_color': 'red',
           'link_color': 'yellow',
           'visited_color': 'green'}
    result = kwargs_ex.fun(**dic)
    assert result == ('blue', 'red', 'yellow', 'green')
    # assert result == tup


def test_deault():
    result = kwargs_ex.fun()
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_combo():
    '''
    Positional argument vs keyword arguments
    '''
    tup = ('green',
           'blue',
           )
    dic = {#'fore_color': 'blue',
           #'back_color': 'red',
           'link_color': 'yellow',
           'visited_color': 'green',
           }
    result = kwargs_ex.fun(*tup, **dic)

    assert result == ('green', 'blue', 'yellow', 'green')


def test_fun2():
    result = kwargs_ex.fun2()
    
    assert result == ((), dict())


