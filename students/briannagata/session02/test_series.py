# Test for series
# Python 3.6


import pytest
import series


@pytest.mark.parametrize('n, expected', [(0, 0),
                                         (2, 1),
                                         (3, 2)])
def test_fib(n, expected):
    assert series.fib(n) is expected


@pytest.mark.parametrize('n, expected', [(0, 2),
                                         (2, 3),
                                         (3, 4)])
def test_lucas(n, expected):
    assert series.lucas(n) is expected
        

@pytest.mark.parametrize('n, first, second, expected', [(0, 0, 1, 0),
                                                        (3, 0, 1, 2),
                                                        (0, 2, 1, 2),
                                                        (3, 2, 1, 4)])
def test_sum_series(n, first, second, expected):
    assert series.sum_series(n, first, second) is expected
