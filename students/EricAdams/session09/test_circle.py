#! /usr/bin/env python

# test_circle.py
# Use pytest to run these tests

import circle
import math
import pytest


# Instance of Circle can be instantiated
def test_circle_instantiation():
    r = 4
    circle_obj = circle.Circle(r)
    # print(circle_obj)
    assert circle_obj.radius == r
    # assert False


def test_circle_diameter_getter():
    r = 4
    circle_obj = circle.Circle(r)
    assert circle_obj.diameter == 2 * r


def test_circle_diameter_setter():
    r = 4
    circle_obj = circle.Circle(r)
    circle_obj.diameter = 10
    assert circle_obj.radius == 5
    assert circle_obj.diameter == 10


def test_circle_area_getter():
    r = 4
    circle_obj = circle.Circle(r)
    assert circle_obj.area == math.pi * r**2


def test_circle_area_setter():
    r = 4
    circle_obj = circle.Circle(r)
    print(circle_obj.area)
    with pytest.raises(Exception) as excinfo:
        circle_obj.area = 10
    x = repr(excinfo)
    assert 'AttributeError' in x
    # assert False

