'''
Circle class, exercise (testing)
'''

from math import pi
from circle import Circle

def test_init():
    Circle(5)

    assert True

def test_radius():
    c = Circle(5)

    assert c.radius == 5

def test_diameter():
    c = Circle(4)

    assert c.diameter == 8

    c.diameter = 10
    assert c.radius == 5
    assert c.diameter == 10

def test_area():
    c = Circle(10)

    assert c.area == pi * c.radius**2

def test_delete():
    c = Circle(10)
    try:
        del c.radius
    except AttributeError as err:
        print(err.args)

    assert True

def test_repr():
    c = Circle(10)

    assert eval(repr(c)) == "Circle(10)"

def test_string():
    c = Circle(10)

    assert str(c) == "Circle with a radius of 10"

