"""
test_trapz.py
test trapezoidal integral calculation using various forms
of functions
"""
import trapz
import math


def line(x):
    '''a very simple straight horizontal line at y = 5'''
    return 5


def get_sloped_line(m, B):
    ''' sloped line with slope m, intercept B'''
    def sloped_line(x):
        return m * x + B
    return sloped_line


def get_quadratic_eqn(A, B, C):
    ''' quadratic equation with coefficients A, B, C'''
    def quadratic(x):
        return A*(x**2) + B*x + C
    return quadratic


def test_line_area():
    area = trapz.trapz(line, 0, 10)
    assert area == 50


def test_sloped_line_area():
    m, B = 0.5, 2  # coefficients of line
    lb, ub = 0, 10  # upper and lower bounds of integration
    sloped_line = get_sloped_line(m, B)
    area = trapz.trapz(sloped_line, lb, ub)
    shouldbe = 0.5 * m * (ub**2 - lb**2) + B * (ub - lb)
    assert math.isclose(area, shouldbe)

def test_quadratic_area():
    A, B, C = 2, 1, 1
    lb, ub = 0, 2
    quad_curve = get_quadratic_eqn(A, B, C)
    area = trapz.trapz(quad_curve, lb, ub)
    shouldbe = (A/3)*(ub**3 - lb**3) + (B/2)*(ub**2 - lb**2) + C*(ub - lb)
    assert math.isclose(area, shouldbe, rel_tol = 1e-2)

