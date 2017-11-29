#!/usr/bin/env python

'''
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 
1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 
or more, the result is 2. Unless it is your birthday -- on that day, your 
speed can be 5 higher in all cases.
'''

from caught_speeding import caught_speeding

import pytest

def test_1():
    assert caught_speeding(60, False) is 0


def test_2():
    assert caught_speeding(65, False) is 1


def test_3():
    assert caught_speeding(65, True) is 0


def test_4():
    assert caught_speeding(80, False) is 1


def test_5():
    assert caught_speeding(85, False) is 2


def test_6():
    assert caught_speeding(85, True) is 1


def test_7():
    assert caught_speeding(70, False) is 1


def test_8():
    assert caught_speeding(75, False) is 1


def test_9():
    assert caught_speeding(75, True) is 1


def test_10():
    assert caught_speeding(40, False) is 0


def test_11():
    assert caught_speeding(40, True) is 0


def test_12():
    assert caught_speeding(90, False) is 2