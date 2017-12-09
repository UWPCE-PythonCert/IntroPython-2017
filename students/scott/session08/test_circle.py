#!/usr/bin/env python3


"""
tests for Circle class
"""

from circle  import Circle
from math import pi
import pytest

def test_init():
    Circle(5)

def test_radius():
    c = Circle(5)
    assert c.radius == 5

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_change_radius():
    c = Circle(4)
    assert c.diameter == 8
    c.radius = 5
    assert c.radius == 5
    assert c.diameter == 10

def test_change_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 10
    assert c.radius == 5

def test_area():
    c = Circle(10)
    assert c.area == pi * 10**2

def test_set_area():
    c = Circle(10)
    with pytest.raises(AttributeError):
        c.area = 100

def test_delete_radius():
    c = Circle(10)
    del c.radius

def test_adding_two_circles():
    assert Circle(3) + Circle(9) == Circle(12)

def test_multiply_circles():
    assert Circle(5) * 3 == Circle(15)

def test_equality():
    c1 = Circle(6)
    c2 = Circle(4)
    c3 = Circle(9)
    c4 = Circle(50)
    assert c1 != c2
    assert c1 > c2
    assert c3 < c4
    assert c2 <= c3
    assert c2 <= c1

def test_sort_circles():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    after_sorting = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    new_list = sorted(circles)

    assert new_list == after_sorting 






