#!/usr/bin/env python

'''
The number 6 is a truly great number. Given two int values, a and b, 
return True if either one is 6. Or if their sum or difference is 6. Note: 
the function abs(num) computes the absolute value of a number.
'''

from love6 import love6

import pytest

def test_1():
    assert love6(6, 4) is True


def test_2():
    assert love6(4, 5) is False


def test_3():
    assert love6(1, 5) is True


def test_4():
    assert love6(1, 6) is True


def test_5():
    assert love6(1, 8) is False


def test_6():
    assert love6(1, 7) is True


def test_7():
    assert love6(7, 5) is False


def test_8():
    assert love6(8, 2) is True


def test_9():
    assert love6(6, 6) is True


def test_10():
    assert love6(-6, 2) is False


def test_11():
    assert love6(-4, -10) is True


def test_12():
    assert love6(-7, 1) is False


def test_13():
    assert love6(7, -1) is True


def test_14():
    assert love6(-6, 12) is True


def test_15():
    assert love6(-2, -4) is False


def test_16():
    assert love6(7, 1) is True


def test_17():
    assert love6(0, 9) is False


def test_18():
    assert love6(8, 3) is False


def test_19():
    assert love6(3, 3) is True


def test_20():
    assert love6(3, 4) is False