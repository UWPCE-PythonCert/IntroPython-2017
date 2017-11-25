#!/usr/bin/env python

"""
The squirrels in Palo Alto spend most of the day playing.
In particular, they play if the temperature is between 60 and 90 (inclusive).
Unless it is summer, then the upper limit is 100 instead of 90.
Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
"""

from squirrel_play import squirrel_play

def test_1():
    assert squirrel_play(70, False) is True

def test_2():
    assert squirrel_play(95, False) is False

def test_3():
    assert squirrel_play(95, True) is True

def test_4():
    assert squirrel_play(55, False) is False

def test_5():
    assert squirrel_play(30, True) is False

def test_6():
    assert squirrel_play(115, True) is False

def test_7():
    assert squirrel_play(85, False) is True

def test_8():
    assert squirrel_play(70, True) is True

def test_9():
    assert squirrel_play(100, True) is True

def test_10():
    assert squirrel_play(120, False) is False
