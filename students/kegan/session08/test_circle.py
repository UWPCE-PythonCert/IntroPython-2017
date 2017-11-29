"""
Kathryn Egan
"""
from math import pi
from circle import Circle


def test_radius_property():
    c = Circle(5)
    assert c.radius == 5


def test_diameter_property():
    c = Circle(2)
    assert c.diameter == 4


def test_diameter_setter():
    c = Circle(3)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5


def test_area_property():
    c = Circle(4)
    assert c.area == pi * 4 ** 2


def test_str():
    c = Circle(1)
    assert str(c) == 'Circle, r=1'


def test_repr():
    c = Circle(5)
    assert repr(c) == 'Circle(5)'


def test_add1():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    assert c3.radius == 5


def test_add2():
    c1 = Circle(2)
    c2 = c1 + 3
    assert c2.radius == 5


def test_add3():
    c1 = Circle(2)
    c2 = 3 + c1
    assert c2.radius == 5


def test_multiply1():
    c1 = Circle(3)
    c2 = c1 * 4
    assert c2.radius == 12


def test_multiply2():
    c1 = Circle(3)
    c2 = 4 * c1
    assert c2.radius == 12


def test_multiply3():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 12


def test_operators():
    assert Circle(3) < Circle(5)
    assert Circle(4) == Circle(4)
    assert Circle(2) >= Circle(2)
    assert Circle(2) >= Circle(1)
    assert Circle(3) != Circle(5)


def test_sort():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    c4 = Circle(4)
    l1 = [c4, c2, c1, c3]
    l1.sort()
    assert l1 == [c1, c2, c3, c4]


def test_reflected():
    c = Circle(3)
    assert c * 5 == 5 * c


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
    c4 = 6 - c2
    assert c4.radius == -2


def test_augmented():
    c1 = Circle(3)
    c2 = Circle(4)
    c1 += c2
    assert c1.radius == 7
