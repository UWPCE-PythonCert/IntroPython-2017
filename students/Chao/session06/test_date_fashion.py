#!/usr/bin/env python

"""
You and your date are trying to get a table at a restaurant.
The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes.
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
If either of you is very stylish, 8 or more, then the result is 2 (yes).
With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
"""

from date_fashion import date_fashion

def test_1():
    assert date_fashion(8, 9) == 2

def test_2():
    assert date_fashion(2, 1) == 0

def test_3():
    assert date_fashion(9, 1) == 0

def test_4():
    assert date_fashion(5, 7) == 1

def test_5():
    assert date_fashion(0, 10) ==0

def test_6():
    assert date_fashion(6, 4) == 1

def test_7():
    assert date_fashion(0, 2) == 0

def test_8():
    assert date_fashion(8, 3) == 2

def test_9():
    assert date_fashion(5, 2) == 0

def test_10():
    assert date_fashion(4, 4) == 1
