#!/usr/bin/env python
from math import cos
from numpy import linspace
from itertools import islice


def trapz(func, a, b, precision=10):
    '''
    This function uses a more generic approach to trapeziodal numerical
    integration in order to allow non constant size of the sub integration
    sectors hence it is less efficient but more versatile
    '''
    # Test order of a & b
    if a > b:
        a, b = b, a
    print('u\222B')
    values, band = sectors(lambda x: x, lambda x, y: y - x, a, b, precision)
    f_values, f_band = sectors(func,
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


def function_val(func, values):
    '''
    return a list of avg f_values for each sub integration sectors
    '''
    f_values = [func(x) for x in values]


    pass


def func_values_np(func, a, b, precision):
    input_f = linspace(a, b, abs(b - a) * 15)
    f_input = [func(x) for x in input_f]
    f_precision = [(abs(x2 - x1) / precision) for x1, x2 in zip(f_input[:-1], f_input[1:])]
    # print(f_precision)
    return input_f, f_input, f_precision


def func_values(func, a, b, precision):
    input = [a]
    while input[-1] < b:
        input.append(input[-1] + precision)
    input[-1] = b
    return input


if __name__ == "__main__":
    # print(func_values(cos, 0, 10, 0.01))
    # print(linspace(0, 10, 100))
    #print(func_values_np(cos, 0, 10, 0.01))
    area = trapz(lambda x: 2, 0, 5)
    print(area)



