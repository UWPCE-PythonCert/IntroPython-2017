#!/usr/bin/env python3
import pytest
from circle import Circle

def test_radius_initialization():
    c = Circle(4)
    assert c.radius == 4


def test_diameter_setter():
    c = Circle(4)
    c.diameter = 12
    assert c.radius == 6.0


def test_bad_initialization():
    with pytest.raises(ValueError) as excinfo:
        c = Circle(None)
    assert "invalid radius" in str(excinfo.value)


def test_set_bad_radius_string():
    with pytest.raises(ValueError) as excinfo:
        c = Circle(2)
        c.radius = "Bad stuff"
    assert "invalid radius" in str(excinfo.value)


def test_set_bad_radius_none():
    with pytest.raises(ValueError) as excinfo:
        c = Circle(1)
        c.radius = None
    assert "invalid radius" in str(excinfo.value)


def test_set_bad_radius_negative():
    with pytest.raises(ValueError) as excinfo:
        c = Circle(1)
        c.radius = -1
    assert "invalid radius" in str(excinfo.value)


def test_set_bad_diameter_string():
    with pytest.raises(ValueError) as excinfo:
        c = Circle(1)
        c.diameter = "bad value"
    assert "invalid radius" in str(excinfo.value)


def test_cannot_set_area():
    with pytest.raises(AttributeError) as excinfo:
        c = Circle(2)
        c.area = 32
    assert "can't set attribute" in str(excinfo.value)


def test_missing_radius_on_init():
    with pytest.raises(TypeError) as excinfo:
        c = Circle()
    assert "missing 1 required positional argument" in str(excinfo.value)


def test_circle_repr():
    c = Circle(2)
    assert repr(c) == "Circle(2)"


def test_circle_str(capfd):
    c = Circle(4)
    print(c)
    out, err = capfd.readouterr()
    assert out == "Circle with radius: 4\n"


def test_adding_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    assert repr(c) == "Circle(6)"


def test_multiplying_circle():
    c = Circle(5)
    c1 = c * 2
    assert repr(c1) == "Circle(10)"


def test_initialize_via_diameter():
    c = Circle.from_diameter(10)
    assert c.radius == 5.0


def test_bad_init_via_diameter_string():
    with pytest.raises(ValueError) as excinfo:
        c = Circle.from_diameter("Bad")
    assert "invalid diameter" in str(excinfo.value)


def test_bad_init_via_diameter_none():
    with pytest.raises(ValueError) as excinfo:
        c = Circle.from_diameter(None)
    assert "invalid diameter" in str(excinfo.value)


def test_bad_init_via_diameter_negative():
    with pytest.raises(ValueError) as excinfo:
        c = Circle.from_diameter(-1)
    assert "invalid diameter" in str(excinfo.value)


def test_bad_init_via_diameter_no_value():
    with pytest.raises(TypeError) as excinfo:
        c = Circle.from_diameter()
    assert "missing 1 required positional argument" in str(excinfo.value)


def test_equality():
    c1 = Circle(1)
    c2 = Circle(1)
    assert c1 == c2


def test_inequality():
    c1 = Circle(2)
    c2 = Circle(1)
    assert c1 != c2


def test_greater_than():
    c1 = Circle(2)
    c2 = Circle(1)
    assert c1 > c2


def test_less_than():
    c1 = Circle(2)
    c2 = Circle(1)
    assert c2 < c1


def test_reflected_multiplication():
    c1 = Circle(2)
    c2 = 3 * c1
    assert repr(c2) == "Circle(6)"


def test_augmented_addition():
    c1 = Circle(1)
    c2 = Circle(2)
    c1 += c2
    assert repr(c1) == "Circle(3)"


def test_augmented_multiplication():
    c1 = Circle(3)
    c1 *= 5
    assert repr(c1) == "Circle(15)"
