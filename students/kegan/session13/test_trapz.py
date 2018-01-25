"""
Kathryn Egan
"""

import trapz
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
    assert area == 50

    line = trapz.line(m=.5)
    area = trapz.trapz(line, 0, 10)
    print(area)
    assert False
