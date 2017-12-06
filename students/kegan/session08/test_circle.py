"""
Kathryn Egan
"""
from math import pi
from Circle import Circle
import pytest


def test_radius_property():
    c = Circle(5)
    assert c.radius == 5
    with pytest.raises(ValueError):
        c.radius = 0
    with pytest.raises(ValueError):
        c.radius = -2


def test_diameter_property():
    c = Circle(2)
    assert c.diameter == 2 * 2


def test_diameter_setter():
    c = Circle(3)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 10 / 2


def test_area_property():
    c = Circle(4)
    assert c.area == pi * 4 ** 2


def test_str():
    c = Circle(1)
    assert str(c) == 'Circle, r=1.0'
    c.radius = 3.5
    assert str(c) == 'Circle, r=3.5'
    c.radius = 5.69793829485950684
    assert str(c) == 'Circle, r=5.7'


def test_repr():
    c = Circle(5)
    assert repr(c) == 'Circle(5.0)'
    c.radius = 99.929292
    assert repr(c) == 'Circle(99.9)'


def test_add1():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    assert c3.radius == 2 + 3


def test_add2():
    c1 = Circle(2)
    c2 = c1 + 3
    assert c2.radius == 2 + 3


def test_add3():
    c1 = Circle(2)
    c2 = 3 + c1
    assert c2.radius == 2 + 3


def test_add4():
    c1 = Circle(2)
    c1 += 4
    assert c1.radius == 2 + 4


def test_multiply1():
    c1 = Circle(3)
    c2 = c1 * 4
    assert c2.radius == 3 * 4
    with pytest.raises(ValueError):
        c1 * -1
    with pytest.raises(ValueError):
        c1 * 0


def test_multiply2():
    c1 = Circle(3)
    c2 = 4 * c1
    assert c2.radius == 3 * 4


def test_multiply3():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 3 * 4


def test_multiply4():
    c1 = Circle(3)
    c1 *= 3
    assert c1.radius == 3 * 3


def test_operators():
    assert Circle(3) < Circle(5)
    assert not Circle(3) < Circle(2)
    assert Circle(3) <= Circle(5)
    assert Circle(3) <= Circle(3)
    assert not Circle(4) <= Circle(3)
    assert Circle(4) == Circle(4)
    assert Circle(3) != Circle(5)
    assert Circle(4) > Circle(3)
    assert not Circle(4) > Circle(5)
    assert Circle(2) >= Circle(2)
    assert Circle(2) >= Circle(1)
    assert not Circle(2) >= Circle(3)


def test_reflected():
    c1 = Circle(3)
    c1 = c1 * 3
    assert c1.radius == 3 * 3
    c2 = Circle(4)
    c2 = 4 * c2
    assert c2.radius == 4 * 4


def test_division1():
    c1 = Circle(15)
    c2 = c1 / 3
    assert c2.radius == 5


def test_division2():
    c1 = Circle(3)
    c2 = 9 / c1
    assert c2.radius == 3


def test_subtract():
    c1 = Circle(10)
    c2 = Circle(8)
    c3 = c1 - c2
    assert c3.radius == 2
    c1 -= 4
    assert c1.radius == 6
    with pytest.raises(ValueError):
        6 - c2


def test_augmented():
    c1 = Circle(3)
    c2 = Circle(4)
    c1 += c2
    assert c1.radius == 7
