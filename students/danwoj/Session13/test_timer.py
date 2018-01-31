import pytest, math

from timer import Timer

def test_timer():
    with Timer() as t:
        for i in range(90000):
            i = i ** 20

    assert math.isclose(t.interval, 0.05, rel_tol=0.00, abs_tol=0.1)