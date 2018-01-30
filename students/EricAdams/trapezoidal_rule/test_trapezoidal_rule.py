'''
test_trapezoidal_rule.py
Run pytest on trapezoidal_rule.py using
different functions
'''
from trapezoidal_rule import *


def test_sigma():
    result = sigma(f, 2, 0, 2)
    assert result == 3


def test_sigma2():
    result = sigma(f, 4, 4, 4)
    assert result == 63


def test_func_a_plus_func_b_div_2():
    result = func_a_plus_func_b_div_2(f, 0, 2)
    assert result == 4


def test_func_a_plus_func_b_div_2_2():
    result = func_a_plus_func_b_div_2(f, 4, 4)
    assert result == 21


def test_b_minus_a_div_n():
    result = b_minus_a_div_n(4, 4, 4)
    assert result == 0


def test_b_minus_a_div_n_2():
    result = b_minus_a_div_n(4, 2, 4)
    assert result == 0.5


def test_trapz_area_under_curve():
    result = trapz_area_under_curve(f, 1000, 0, 4)
    assert result > 33
    assert result < 34
