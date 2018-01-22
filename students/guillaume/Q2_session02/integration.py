#!/usr/bin/env python
from math import cos
from numpy import linspace
from itertools import islice


def trapz(func, a, b, precision=10, **func_args):
    '''
    This function uses a more generic approach to trapeziodal numerical
    integration in order to allow non constant size of the sub integration
    sectors hence it is less efficient but more versatile
    '''
    # Test order of a & b
    if a > b:
        a, b = b, a

    def loc_f(x):
        nonlocal func_args
        return func(x, **func_args)

    values, band = sectors(lambda x: x, lambda x, y: y - x, a, b, precision)
    f_values, f_band = sectors(loc_f,
                               lambda x, y: 0.5 * (x + y), a, b, precision)
    integral = sum([x * y for x, y in zip(band, f_band)])
    return integral


def sectors(*args):
    '''
    Define the sub integration sections
    it currently uses an constant steps but will be improve in the future
    it takes function as an argument but does not use it yet
    '''
    func1, func2, a, b, precision = args
    values = linspace(a, b, abs(b - a) * precision)
    l_v = len(values)
    bands = [func2(func1(x1), func1(x2))
             for x1, x2 in zip(islice(values, 0, l_v - 1),
                               islice(values, 1, l_v))]
    return values, bands


def test():
    args = {'a': 1, 'b': 2}

    def inner():
        nonlocal args
        for x, y in args.items():
            print('{} {}'.format(x, y))
    inner()


def f_b(x, A, B, C=0):
    return C * x + A + B


def test_f_b(x):
    args = {'A': 1, 'B': 2}

    def inner(x):
        nonlocal args
        return f_b(x, **args)
    return inner(x)


if __name__ == "__main__":
    area = trapz(lambda x: 2 * x, 0, 5, 10)
    # primitive of 2 * x is x**2 hence area value should be 25
    assert area == 25
    print(area)
    test()
    print(test_f_b(0))
    area_2 = trapz(f_b, 0, 5, **{'A': 1, 'B': 2})
    print(area_2)
    area_3 = trapz(f_b, 0, 5, 10, A=1, B=2, C=1)
    print(area_3)

