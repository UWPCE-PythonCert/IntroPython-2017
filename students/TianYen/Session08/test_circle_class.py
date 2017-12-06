from Circle_class_exercise import Circle
from math import pi
import pytest

def test_Circle():
    c = Circle(2)

def test_radius():
    c = Circle(2)
    assert c.radius == 2

def test_diameter():
    c = Circle(2)
    assert c.diameter == 4

def test_change_radius():
    c = Circle(4)
    c.radius = 6
    assert c.radius == 6
    assert c.diameter == 12

def test_set_diameter():
    c = Circle(2)
    assert c.diameter == 4

    c.diameter = 10
    assert c.radius == 5

def test_area():
    c = Circle(10)
    assert c.area == pi * 10**2

def test_set_area():
    c = Circle(10)
    with pytest.raises(AttributeError):
        c.area = 100

def test_delete_diameter():
    c = Circle(10)

    with pytest.raises(AttributeError):
        del c.diameter

def test_str():
    c = Circle(10)
    assert str(c) == "This is a Circle with radius: 10.00000"

def test_repr():
    c = Circle(10)
    assert repr(c) == 'Circle(10)'

def test_add_circle():
    c1 = Circle(10)
    c2 = Circle(5)
    c3 = c1 + c2
    assert c3.radius == 15
    assert c3.diameter == 30

def test_scale_circle():
        c1 = Circle(10)
        c2 = c1 * 3
        c3 = 2 * c1
        assert c2.radius == 30
        assert c3.radius == 20

def test_compare_circles():
    c1 = Circle(10)
    c2 = Circle(5)
    c3 = Circle(5)

    assert c1 > c2
    assert c2 == c3
    assert c3 < c1
    assert (c1 == c2) is False

def test_sort():
    c = [Circle(0), Circle(2), Circle(1), Circle(3)]
    c.sort()
    assert c[0].radius == 0
    assert c[1].radius == 1
    assert c[2].radius == 2
    assert c[3].radius == 3

def test_relflected_numerics():
    c = Circle(4)
    assert c * 2 == 2 * c

def test_circumference():
    c = Circle(4)
    assert c.circumference == 2 * pi *4

def test_augmented_addition():
    c = Circle(4)
    c += Circle(2)
    assert c.radius == 6

def test_augmented_multiplication():
    c = Circle(2)
    c *= 4
    assert c.radius == 8
