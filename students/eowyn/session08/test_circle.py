'''
test for circle class
'''

from circle import Circle
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
    assert c.diameter == 10


def test_change_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 10
    assert c.radius == 5


def test_area():
    c = Circle(10)
    assert c.area == pi*10**2


def test_set_area():
    c = Circle(10)
    with pytest.raises(AttributeError):
        c.area = 100


def test_delete_diameter():
    c = Circle(10)
    with pytest.raises(AttributeError):
        del c.diameter


def test_add_circles():
    assert Circle(2) + Circle(4) == Circle(6)


def test_mult_circles():
    assert Circle(2)*10 == Circle(20)

def test_div_circles():
    assert Circle(10)/2 == Circle(5)


def test_compare_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert not (c1 > c2)
    assert c1 < c2
    assert not(c1 == c2)
    assert c2 == c3
    assert c2 >= c3
    assert c3 >= c1
    assert c1 <= c2
    assert c2 <= c3


def test_sort_circles():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4),
               Circle(0), Circle(2), Circle(3), Circle(5),
               Circle(9), Circle(1)]
    expected = [Circle(0), Circle(1), Circle(2), Circle(3),
                Circle(4), Circle(5), Circle(6), Circle(7),
                Circle(8), Circle(9)]
    circles.sort() # returns None; does in-place sorting
    assert circles == expected


def test_multiply():
    c1 = Circle(2)
    assert c1*3 == 3*c1
    assert c1*3 == Circle(6)


def test_subtract_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c2 - c1 == c1
    # This checks that abs() works when radius < 0
    assert c1 - c2 == c1


def test_floordiv():
    c1 = Circle(5)
    assert c1//3 == Circle(1)
    assert 5//c1 == Circle(1)


def test_truediv():
    c1 = Circle(4)
    c2 = Circle(2)
    assert c1/2 == c2
    assert 4/c2 == c2


def test_augmented_assignments():
    c1 = Circle(4)
    c2 = Circle(2)
    c1 += c2
    assert c1.radius == 6
    c1 -= c2
    assert c1.radius == 4
    c1 *= 2
    assert c1.radius == 8
    c1 /= 2
    assert c1.radius == 4


def test_unary_arithmetic():
    c1 = Circle(-3)
    assert abs(c1) == Circle(3)


def test_modulo_circles():
    c1 = Circle(5)
    c2 = Circle(2)
    assert c1%c2 == Circle(1)



