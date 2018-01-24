

from classes import Circle, Sphere
import math
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
    c.diameter = 8

    assert c.radius == 4
    assert c.diameter ==8

def test_circle_area():
    c = Circle(4)


    assert c.area == (4**2 * math.pi)

def test_set_area():
    c = Circle(10)
    with pytest.raises(AttributeError):
        c.area =100

def test_delete_diameter():
    c = Circle(10)
    with pytest.raises(AttributeError):
        del c.diameter


def test_sphere_radius():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_from_diameter():
    s = Sphere.from_diameter(10)

    assert type(s) == Sphere
    assert s.radius == 5
    assert s.diameter == 10
    

def test_sphere_volume():
    s = Sphere.from_diameter(20)

    assert s.volume == 4188.79







