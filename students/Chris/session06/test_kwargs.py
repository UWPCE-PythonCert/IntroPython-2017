#!/usr/bin/env python3

import kwargs_ex

import pytest


def test_basic():
    assert True

def test_kw():
    result = kwargs_ex.fun(fore_color='blue',
                           back_color='red',
                           link_color='yellow',
                           visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_new_order():
    result = kwargs_ex.fun(visited_color='green',
                           fore_color='blue',
                           link_color='yellow',
                           back_color='red',
                           )
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_new_order():
    result = kwargs_ex.fun('green',
                           'blue',
                           'purple',
                           'red',
                           )
    assert result == ('green', 'blue', 'purple', 'red')


def test_kw_combo():
    result = kwargs_ex.fun('green',
                           'blue',
                           visited_color='green',
                           link_color='yellow',
                           )
    assert result == ('green', 'blue', 'yellow', 'green')

def test_kw_tuple():
    tup = ('green',
           'blue',
           'purple',
           'red',
           )
    result = kwargs_ex.fun(*tup)

#    assert result == ('green', 'blue', 'purple', 'red')
    assert result == tup


def test_kw_dict():
    dic = {"fore_color": 'blue',
           "back_color": 'red',
           "link_color": 'yellow',
           "visited_color": 'green',
           }
    result = kwargs_ex.fun(**dic)

    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_combo():
    tup = ('green',
           'blue',
           )
    dic = {"link_color": 'yellow',
           "visited_color": 'green',
           }
    result = kwargs_ex.fun(*tup, **dic)

    assert result == ('green', 'blue', 'yellow', 'green')


def test_default():
    result = kwargs_ex.fun()

    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_combo():
    tup = ('green',
           )
    dic = {"link_color": 'yellow',
           "visited_color": 'green',
           }
    result = kwargs_ex.fun(*tup, **dic)

    assert result == ('green', 'red', 'yellow', 'green')


def test_kw_combo_bad():
    with pytest.raises(TypeError):
        result = kwargs_ex.fun('green',
                               visited_color='green',
                               no_color='green'
                               )


def test_fun2_empty():
    result = kwargs_ex.fun2()

    assert result == ((), {})


def test_fun2_pos():
    result = kwargs_ex.fun2(2, 3)

    assert result == ((2, 3), {})


def test_fun2_kw():
    result = kwargs_ex.fun2(this=45)

    assert result == ((), {"this": 45})

def test_fun2_both():
    result = kwargs_ex.fun2(4, 5, this=45)

    assert result[0] == (4, 5)
    assert result[1] == {"this": 45}


def test_fun2_args():
    t = (4, 5, 6, 7)
    result = kwargs_ex.fun2(*t, this=45)

    assert result[0] == t
    assert result[1] == {"this": 45}


def test_fun2_args2():
    t = (4, 5, 6, 7)
    result = kwargs_ex.fun2(6, *t, 7, this=45)

    assert result[0] == (6, 4, 5, 6, 7, 7)
    assert result[1] == {"this": 45}


def test_fun2_args3():
    t = (4, 5, 6, 7)
    d = {'this': 45,
         'that': 65,
         }
    result = kwargs_ex.fun2(6, *t, 7, **d, other=80)

    assert result[0] == (6, 4, 5, 6, 7, 7)
    assert result[1] == {'other': 80, 'that': 65, 'this': 45}


def test_fun2_args4():
    t = (4, 5, 6, 7)
    d = {'this': 45,
         'that': 65,
         }
    result = kwargs_ex.fun2(6, *t, 7, other=80)

    assert result[0] == (6, 4, 5, 6, 7, 7)
    assert result[1] == {'other': 80, 'that': 65, 'this': 45}

