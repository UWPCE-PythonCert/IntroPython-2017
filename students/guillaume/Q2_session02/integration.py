#!/usr/bin/env python
from math import exp, isclose
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


def trapz_p(func, a, b, precision=10, **func_args):
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

    x_l, f_x_l = sectors_precisions(loc_f, a, b, precision)

    def band_f(lst, func):
        l_v = len(lst)
        return [func(x1, x2)
                for x1, x2 in zip(islice(lst, 0, l_v - 1),
                                  islice(lst, 1, l_v))]

    band = band_f(x_l, lambda x1, x2: x2 - x1)
    f_band = band_f(f_x_l, lambda x1, x2: 0.5 * (x1 + x2))
    integral = sum([x * y for x, y in zip(band, f_band)])

    return integral


def sectors_precisions(*args):
    '''
    Assuming that f meets Riemann criterions for integration
    default size of an integration sub domain is (1/20 x |b - a|)
    for a sub dommain [x1, x2], where x2 >x 1
    Z = |f(x2) - f(x1)| will be compared to a precision value
    if Z bigger than precision x2 size will be decrease until the inequation
    is accurate.
    There is a test to avoid that calculations would run for too long
    '''
    func, a, b, precision = args

    def prec(func, precision):

        def alpha(x, step):
            f_x = func(x), func(x + step)
            results = x + step, f_x[1]
            if (abs(f_x[1] - f_x[0]) <= precision) or step < precision / 100:
                return results
            else:
                return alpha(x, step / 2)
        return alpha

    prec_x = prec(func, precision)
    x = a
    x_l = [a]
    f_x_l = [func(a)]
    step = abs(b - a) / 20

    while x <= b:
        xdx, fxdx = prec_x(x, step)
        x_l.append(xdx)
        f_x_l.append(fxdx)
        x = xdx + step

    if x_l[-1] != b:
        x_l.append(b)
        f_x_l.append(func(b))

    return x_l, f_x_l


def test():
    args = {'a': 1, 'b': 2}

    def inner():
        nonlocal args
        for x, y in args.items():
            print('{} {}'.format(x, y))
    inner()


def f_b(x, A, B, C=0):
    return C * x + A + B


def continuous_fonction(x, a, b, c):
    # if x < 5:
    #    return a * x
    pass


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
    
    print('\ntrapz_p_Test\n')

    area = trapz_p(lambda x: 2 * x, 0, 5, 0.1)
    print(area)

    area_2 = trapz_p(f_b, 0, 5, **{'A': 1, 'B': 2})
    print(area_2)

    area_3 = trapz_p(f_b, 0, 5, 10, A=1, B=2, C=1)
    print(area_3)