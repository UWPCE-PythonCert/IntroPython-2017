#! /usr/bin/env python

import trapezoidal_rule as tr


def area_under_function(func):
    def trapz_area_under_curve(func, n, a, b, step):
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
        area1 = tr.b_minus_a_div_n(n, a, b)
        area2 = tr.func_a_plus_func_n_div_2(func, n, a)
        area3 = tr.sigma(func, n, a, b, step)

        area = area1 + area2 + area3
        return area
    return trapz_area_under_curve



