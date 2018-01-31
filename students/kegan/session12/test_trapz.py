"""
Kathryn Egan
"""

import trapz
import math
import pytest


def test_line():
    line = trapz.line(m=2, b=1)
    assert line(1) == 3
    assert line(2) == 5
    assert line(3) == 7

    line = trapz.line(b=5)
    assert line(1) == 6
    assert line(2) == 7

    line = trapz.line(m=0, b=5)
    assert line(1) == 5
    assert line(100) == 5


def test_segment():
    seg = trapz.segment(0, 3, 3)
    assert next(seg) == 0
    assert next(seg) == 1
    assert next(seg) == 2
    assert next(seg) == 3
    with pytest.raises(StopIteration):
        next(seg)

    seg = trapz.segment(0, 10, 20)
    assert next(seg) == 0
    assert next(seg) == .5
    assert next(seg) == 1
    assert next(seg) == 1.5


def test_trapz():
    line = trapz.line(m=0, b=5)
    area = trapz.trapz(line, 0, 10)
    assert round(area, 5) == 50

    line = trapz.line(m=.5)
    area = trapz.trapz(line, 0, 10)
    assert round(area, 5) == 25

    area = trapz.trapz(math.sin, 0, 1)
    answer = math.cos(0) - math.cos(1)
    assert round(area, 2) == round(answer, 2)


def test_arbitrary_coeffs():
    def throwaway(x, y, z):
        return x ** y + z * 2

    area = trapz.trapz(throwaway, 0, 5, 2, 2)
    assert round(area, 2) == 61.67


def test_polynomial():
    A, B, C, D = 5, 4, 3, 2
    f = trapz.polynomial(A, B, C, D)
    x = 2
    assert f(x) == sum([A * x ** 3, B * x ** 2, C * x, D])
    A, B, C, D, E, F = 2, 0, 4, 1, 0, 0
    f = trapz.polynomial(A, B, C, D, E, F)
    x = 4
    assert f(x) == sum([A * x ** 5, C * x ** 3, D * x ** 2])


def test_quadtratic():
    f = trapz.polynomial(3, 2, 2)
    x = 5
    assert f(x) == sum([3 * x ** 2, 2 * x, 2])
