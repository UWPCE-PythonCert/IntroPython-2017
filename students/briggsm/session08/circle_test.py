'''
Circle class, exercise (testing)
'''

from math import pi
from circle import Circle, Sphere



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
    assert "Circle(10)" == repr(c)
    assert c == eval(repr(c))

def test_string():
    c = Circle(10)

    assert str(c) == "Circle with a radius of 10"


def test_create_from_diameter():
    c = Circle.create_from_diameter(10)

    assert type(c) == Circle
    assert c.radius == 5


def test_add_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2

    assert Circle(6).radius == c3.radius


def test_multiply_circles():
    c1 = Circle(4)
    c2 = c1 * 3

    assert Circle(12).radius == c2.radius


def test_compare_greater_true():
    c1 = Circle(7)
    c2 = Circle(5)

    assert (c1 > c2) == True


def test_compare_greater_false():
    c1 = Circle(4)
    c2 = Circle(5)

    assert (c1 > c2) == False


def test_compare_lesser_true():
    c1 = Circle(4)
    c2 = Circle(5)

    assert (c1 < c2) == True


def test_compare_lesser_false():
    c1 = Circle(7)
    c2 = Circle(5)

    assert (c1 < c2) == False


def test_compare_equal_true():
    c1 = Circle(5)
    c2 = Circle(5)

    assert (c1 == c2) == True


def test_compare_equal_false():
    c1 = Circle(7)
    c2 = Circle(5)

    assert (c1 == c2) == False

# Sphere tests:


def test_sphere_radius():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10


def test_sphere_from_diameter():
    s = Sphere.create_from_diameter(10)

    assert type(s) == Sphere
    assert s.radius == 5
    assert s.diameter == 10
