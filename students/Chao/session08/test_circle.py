#!/usr/bin/env python

"""
Test for Circle class
"""

from math import pi
from circle import Circle, Sphere
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

def test_atl_con():
    """ Test the alternate constructor """
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4

def test_str_repr():
    c = Circle(4)
    #print(c)
    assert repr(c) == 'Circle(4)'
    d = eval(repr(c))
    assert d.radius == 4

def test_add_radius():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6

def test_compare_radius():
    c1 = Circle(2)
    c2 = Circle(4)

    assert not(c1 > c2)
    assert c1 < c2
    assert not(c1 == c2)
    c3 = Circle(4)
    assert c2 == c3

def test_circle_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    # Iterate through the sorted circle list, make sure they sorted from 0 to 9
    for c in circles:
        assert circles.index(c) == c.radius

def test_sphere_radius():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_from_diameter():
    s = Sphere.from_diameter(10)

    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_str_repr():
    s = Sphere(5)
    #print(c)
    assert repr(s) == 'Sphere(5)'
    t = eval(repr(s))
    assert t.radius == 5
    
def test_sphere_volume():
    s = Sphere(5)
    assert s.volume == (4/3) * pi * 5**3
    
def test_sphere_area():
    s = Sphere(5)
    assert s.area == 4 * pi * 5**2