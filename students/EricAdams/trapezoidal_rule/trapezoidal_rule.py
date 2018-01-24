#! /usr/bin/env python


def f(x, a=1, b=1, c=1):
    return a * (x**2) + b * x + c


def sigma(func, n, a, b):
    '''
    calculate the sigma portion of the trapezoidal rule for the area
    under a curve
    :func = the function that defines the curve
    :func = function type
    :n = the number of steps in the integration
    :n = integer type
    :a = the starting point on the x axis for the integration
    :a = numeric type
    :b = the end point on the x axis for the integration
    :b = numeric type
    :step = float type
    '''
    # value of the sigma portion of the trapez. rule
    step = float((b - a) / n)
    # use a listcomp to calculate each element of sigma
    # sigma_list = [func(a + i * step) for i in range(1, n)]
    # return sum(sigma_list)
    # use a genexp to calculate each element of sigma
    result = 0
    sigma_gen = (func(a + i * step) for i in range(1, n))
    for i in sigma_gen:
        result += i
    return result


def func_a_plus_func_b_div_2(func, a, b):
    '''
    2nd part of area under a curve (f(x_0) + f(x_n)) /2
    '''
    # nth value of func = func(b)
    result = (func(a) + func(b)) / 2
    return result


def b_minus_a_div_n(n, a, b):
    '''
    1st part of area under a curve
    '''
    result = (b - a) / n
    return result


def trapz_area_under_curve(func, n, a, b):
    '''
    Calculate the area under a curve using the
    trapezoidal rule.
    :func = the function that defines the curve
    :func = function type
    :n = the number of trapezoids under the curve
    :n = integer type
    :a = the starting point on the x axis for calculations
    :a = numeric type
    :b = the end point on the x axis for calculations
    :b = numeric type
    :step = the width of the trapezoid.
    :step = float type
    '''
    # (b-a)/n
    area1 = b_minus_a_div_n(n, a, b)
    area2 = func_a_plus_func_b_div_2(func, a, b)
    area3 = sigma(func, n, a, b)

    area = area1 * (area2 + area3)
    return area










