#! /usr/bin/env python

# test_circle.py
# Use pytest to run these tests

from circle import Circle, Sphere
import math
import pytest


# Instance of Circle can be instantiated
def test_circle_instantiation():
    r = 4
    circle_obj = Circle(r)
    # print(circle_obj)
    assert circle_obj.radius == r
    # assert False


def test_circle_diameter_getter():
    r = 4
    circle_obj = Circle(r)
    assert circle_obj.diameter == 2 * r


def test_circle_diameter_setter():
    r = 4
    circle_obj = Circle(r)
    circle_obj.diameter = 10
    assert circle_obj.radius == 5
    assert circle_obj.diameter == 10


def test_circle_area_getter():
    r = 4
    circle_obj = Circle(r)
    assert circle_obj.area == math.pi * r**2


def test_circle_area_setter():
    r = 4
    circle_obj = Circle(r)
    with pytest.raises(AttributeError):
        circle_obj.area = 10
    assert AttributeError
    # assert False


def test_circle_from_diameter():
    circ_obj = Circle.from_diameter(8)
    assert circ_obj.diameter == 8
    assert circ_obj.radius == 4


def test_circle__str__():
    circ_obj = Circle(4)
    # print(circ_obj)
    assert str(circ_obj) == 'Circle with radius:4'
    # assert False


def test_circle__repr__():
    circ_obj = Circle(4)
    assert 'Circle(4)' == repr(circ_obj)


def test_add_circles():
    circ_obj_1 = Circle(4)
    circ_obj_2 = Circle(2)
    result = circ_obj_1 + circ_obj_2
    print(repr(result))
    assert repr(result) == 'Circle(6)'
    # assert False


def test_multiply_times_number():
    circ_obj_1 = Circle(4)
    result = circ_obj_1 * 2
    assert repr(result) == 'Circle(8)'


def test_multipy_number_times_object():
    circ_obj_1 = Circle(4)
    result = 2 * circ_obj_1
    assert repr(result) == 'Circle(8)'


def test_lt():
    circ_obj_1 = Circle(4)
    circ_obj_2 = Circle(6)
    if circ_obj_1 < circ_obj_2:
        assert True
    else:
        assert False


def test_gt():
    circ_obj_1 = Circle(4)
    circ_obj_2 = Circle(6)
    if circ_obj_2 > circ_obj_1:
        assert True
    else:
        assert False


def test_eq():
    circ_obj_1 = Circle(5)
    circ_obj_2 = Circle(5)
    assert circ_obj_1 == circ_obj_2


def test_sort():
    circles = [Circle(6), Circle(4), Circle(2), Circle(
        3), Circle(5), Circle(1), Circle(7), Circle(8), ]
    circles.sort()
    for i in range(0, 7):
        assert circles[i] < circles[i + 1]
    # print(circles)
    # assert False


def test_sphere__str__():
    sphere_obj = Sphere(4)
    # print(circ_obj)
    assert str(sphere_obj) == 'Sphere with radius:4'
    # assert False


def test_sphere__repr__():
    sphere_obj = Sphere(4)
    assert 'Sphere(4)' == repr(sphere_obj)


def test_sphere_volume():
    sphere_obj = Sphere(4)
    assert sphere_obj.volume == 4 / 3 * math.pi * sphere_obj.radius**3


def test_sphere_surface_area():
    sphere_obj = Sphere(4)
    assert sphere_obj.area == 4 * math.pi * sphere_obj.radius**2


def test_sphere_from_diameter():
    sphere_obj = Sphere.from_diameter(8)
    assert sphere_obj.radius == 4
    assert sphere_obj.area == 4 * math.pi * sphere_obj.radius**2
