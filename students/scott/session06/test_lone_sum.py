#!/usr/bin/env python3

'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.
'''

from lone_sum import lone_sum

def test1():
    assert lone_sum(1, 2, 3) is 6

def test2():
    assert lone_sum(3, 2, 3) is 2

def test3():
    assert lone_sum(3, 3, 3) is 0