#!/usr/bin/env python3

import kwargs_exercise
import pytest

def test_func_default():
    result = kwargs_exercise.func()
    assert result == ('black', 'white', 'blue', 'purple')


def test_func_kw():
    result = kwargs_exercise.func(fore_color="blue",
                                  back_color="red",
                                  link_color="yellow",
                                  visited_color="green")
    assert result == ('blue', 'red', 'yellow', 'green')


def test_func_positional_args():
    result = kwargs_exercise.func("orange", "black", "white", "red")
    assert result == ('orange', 'black', 'white', 'red')


def test_func_kwargs():
    result = kwargs_exercise.func(link_color='red', back_color='blue')
    assert result == ('black', 'blue', 'red', 'purple')


def test_func_combo_positional_kwargs():
    result = kwargs_exercise.func('purple', link_color='red', back_color='blue')
    assert result == ('purple', 'blue', 'red', 'purple')


def test_func_tuple_dict_combo():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = kwargs_exercise.func(*regular, **links)
    assert result == ('red', 'blue', 'chartreuse', 'purple')


def test_func_kwargs_default():
    result = kwargs_exercise.func_kwargs()
    assert result == ('black', 'white', 'blue', 'purple')


def test_func_kwargs_kw():
    result = kwargs_exercise.func_kwargs(fore_color="blue",
                                         back_color="red",
                                         link_color="yellow",
                                         visited_color="green")
    assert result == ('blue', 'red', 'yellow', 'green')


def test_func_kwargs_positional_args():
    result = kwargs_exercise.func_kwargs("orange", "black", "white", "red")
    assert result == ('orange', 'black', 'white', 'red')


def test_func_kwargs():
    result = kwargs_exercise.func_kwargs(link_color='red', back_color='blue')
    assert result == ('black', 'blue', 'red', 'purple')


def test_func_kwargs_combo_positional_kwargs():
    result = kwargs_exercise.func_kwargs('purple',
                                         link_color='red',
                                         back_color='blue')

    assert result == ('purple', 'blue', 'red', 'purple')


def test_func_kwargs_tuple_dict_combo():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = kwargs_exercise.func_kwargs(*regular, **links)
    assert result == ('red', 'blue', 'chartreuse', 'purple')


def test_func_kwargs_bad_combo():
    with pytest.raises(TypeError):
        result = kwargs_exercise.func_kwargs('green',
                                             visited_color="green",
                                             no_color="green")
