#!/usr/bin/env python3

import kwargs_ex
import pytest

def test_true():
    assert True


def test_basic():
    result = kwargs_ex.fun( fore_color="blue",
                            back_color="red",
                            link_color="yellow",
                            visited_color="green")
    assert result == ("blue", "red", "yellow", "green")


def test_mixed_order():
    result = kwargs_ex.fun( fore_color="blue",
                            link_color="yellow",
                            back_color="red",
                            visited_color="green")
    assert result == ("blue", "red", "yellow", "green")


def test_basic():
    result = kwargs_ex.fun( "blue",
                            "red",
                            "yellow",
                            "green")
    assert result == ("blue", "red", "yellow", "green")


def test_defaults():
    result = kwargs_ex.fun()
    assert result == ("blue", "red", "yellow", "green")


def test_positional():
    result = kwargs_ex.fun( "blue",
                            "red",
                            visited_color="green",
                            link_color="yellow")

    assert result == ("blue", "red", "yellow", "green")


def test_tuple():
    tuple = ( "blue", "red", "yellow", "green")
    result = kwargs_ex.fun( *tuple )
    assert result == tuple


def test_dict():
    # fore_color, back_color, link_color, visited_color
    dic = { "fore_color": "blue",
            "back_color": "red",
            "link_color": "yellow",
            "visited_color": "green" }
    result = kwargs_ex.fun( ** dic )
    assert result == ("blue", "red", "yellow", "green")


def test_combo():
    # fore_color, back_color, link_color, visited_color
    tuple = ( "blue", "red" )
    dic = { "link_color": "yellow",
            "visited_color": "green" }
    result = kwargs_ex.fun( *tuple, **dic )
    assert result == ("blue", "red", "yellow", "green")

def test_fun2_positional():
    result = kwargs_ex.fun2( "foo", "bar")
    assert result == ( ( "foo", "bar" ), {} )

def test_fun2_defaults():
    result = kwargs_ex.fun2( )
    assert result == ( (), {} )

def test_fun2_w_values():
    result = kwargs_ex.fun2("foo", athing="boo")
    assert result == (('foo',), {'athing': 'boo'})





