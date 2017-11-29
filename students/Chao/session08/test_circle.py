#!/usr/bin/env python

"""
Test for Circle class
"""

from math import pi
from circle import Circle
import pytest

def test_init():
    Circle(5)
    assert True

def test_radius():
    c = Circle(5)
    assert c.radius == 5

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
    assert c.diameter == 10

def test_area():
    c = Circle(10)

    assert c.area == pi * 10**2

def test_set_area():
     c= Circle(10)

     with pytest.raises(AttributeError):
        c.area = 100

def test_delete_diameter():
    c = Circle(10)

    del c.diameter
