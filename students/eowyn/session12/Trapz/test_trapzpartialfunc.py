"""
test_trapz.py
test trapezoidal integral calculation using various forms
of functions
"""
import trapz
import math
from functools import partial


def line(x):
    '''a very simple straight horizontal line at y = 5'''
    return 5


def sloped_line(x, m=1, B=0):
    ''' sloped line with slope m, intercept B'''
    return m * x + B


def quadratic(x, A=0, B=0, C=0):
    ''' quadratic eqn with x and coefficients defined every time'''
    return A * x**2 + B * x + C


def test_line_area():
    area = trapz.trapz(line, 0, 10)
    assert area == 50


def test_sloped_line_area():
    m, B = 0.5, 2  # coefficients of line
    lb, ub = 0, 10  # upper and lower bounds of integration
    this_line = partial(sloped_line, m=0.5, B=2)
    area = trapz.trapz(this_line, lb, ub)
    shouldbe = 0.5 * m * (ub**2 - lb**2) + B * (ub - lb)
    assert math.isclose(area, shouldbe)

def test_quadratic_area():
    A, B, C = 2, 1, 1
    lb, ub = 0, 2
    quad_curve = partial(quadratic, A=2, B=1, C=1)
    area = trapz.trapz(quad_curve, lb, ub)
    shouldbe = (A/3)*(ub**3 - lb**3) + (B/2)*(ub**2 - lb**2) + C*(ub - lb)
    assert math.isclose(area, shouldbe, rel_tol = 1e-2)


def test_sloped_line_area_kwargs():
    coef = {'m' : 0.5, 'B' : 2}
    lb, ub = 0, 10  # upper and lower bounds of integration
    this_line = partial(sloped_line, **coef)
    area = trapz.trapz(this_line, lb, ub)
    shouldbe = 0.5 * coef['m'] * (ub**2 - lb**2) + coef['B'] * (ub - lb)
    assert math.isclose(area, shouldbe)
