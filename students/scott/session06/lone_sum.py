#!/usr/bin/env python3

'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.
'''

def lone_sum(a, b, c):
    if (a != b) and (b != c) and (a != c):
        return (a + b + c)
    elif (a == b) and (b != c):
        return c
    elif (a == c) and (b != c):
        return b
    elif (b == c) and (a != b):
        return a
    else:
        return 0
