#!/usr/bin/python


def fun(x):
    if x < 0:
        raise ValueError('something')
    else:
        try:
            45 / x
        except ZeroDivisionError:

            return 'division'

for a in [3, 6, -2, 4, 0]:
    try:
        print(fun(a))
    except ValueError:
        pass