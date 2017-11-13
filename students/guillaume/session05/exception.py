#!/usr/bin/env python3
'''
raising exception
'''


def fun(x):
    if x < 0:
        raise ValueError
    else:
        return "Success"


