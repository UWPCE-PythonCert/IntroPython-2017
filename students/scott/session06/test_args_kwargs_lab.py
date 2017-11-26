
import args_kwargs_lab

import pytest


def test_kw():
    result = args_kwargs_lab.fun(fore_color='blue',
                                 back_color='red',
                                 link_color='yellow',
                                 visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_new_order():
    result = args_kwargs_lab.fun('blue',
                                 'yellow',
                                 'red',
                                 'green')
    assert result == ('blue', 'yellow', 'red', 'green')


def test_kw_combo():
    result = args_kwargs_lab.fun('blue',
                                 'yellow',
                                 link_color='red',
                                 visited_color='green')
    assert result == ('blue', 'yellow', 'red', 'green')


def test_kw_combo_tuple():
    tup = ('green',
           'blue',
           'purple',
           'red')
    result = args_kwargs_lab.fun(*tup)

    assert result == ('green', 'blue', 'purple', 'red')


def test_kw_combo_dict():
    dict = {"fore_color": 'blue',
            "back_color": 'red',
            "link_color": 'yellow',
            "visited_color": 'green'}

    result = args_kwargs_lab.fun(**dict)

    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_combo_():
    tup = ('green',
           'blue',)
    dict = {"link_color": 'yellow',
            "visited_color": 'red'}

    result = args_kwargs_lab.fun(*tup, **dict)

    assert result == ('green', 'blue', 'yellow', 'red')


def test_noargs():
    result = args_kwargs_lab.fun()
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_combo_again():
    tup = ('green',
           'blue',)
    dict = {"link_color": 'yellow',
            }

    result = args_kwargs_lab.fun(*tup, **dict)

    assert result == ('green', 'blue', 'yellow', 'green')


# You can have a test pass if you get a certain error by using pytest.raises
# with pytest.raises(TypeError)

def test_fun2():

    result = args_kwargs_lab.fun2(2, 3)
    assert result == ((2, 3), {})
    
    
