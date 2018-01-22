"""
test_trapzargs.py
test trapezoidal integral calculation using various forms
of functions
"""
import trapz
import math


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
    area = trapz.trapzargs(line, 0, 10)
    assert area == 50


def test_sloped_line_area():
    m, B = 0.5, 2  # coefficients of line
    lb, ub = 0, 10  # upper and lower bounds of integration
    area = trapz.trapzargs(sloped_line, lb, ub, m, B)
    shouldbe = 0.5 * m * (ub**2 - lb**2) + B * (ub - lb)
    assert math.isclose(area, shouldbe)

def test_quadratic_area():
    A, B, C = 2, 1, 1
    lb, ub = 0, 2
    area = trapz.trapzargs(quadratic, lb, ub, A, B, C)
    shouldbe = (A/3)*(ub**3 - lb**3) + (B/2)*(ub**2 - lb**2) + C*(ub - lb)
    assert math.isclose(area, shouldbe, rel_tol = 1e-2)

def test_keyword_args():
    coef = {'A':1, 'B':3, 'C': 2}
    lb, ub = 0, 2
    area = trapz.trapzargs(quadratic, lb, ub, **coef)
    shouldbe = (coef['A']/3)*(ub**3 - lb**3) + (coef['B']/2)*(ub**2 - lb**2) + coef['C']*(ub - lb)
    assert math.isclose(area, shouldbe, rel_tol = 1e-2)

def test_keyword_and_args():
    coef = {'A':1, 'B':3}
    lb, ub = 0, 2
    area = trapz.trapzargs(quadratic, lb, ub, C=2, **coef)
    shouldbe = (coef['A']/3)*(ub**3 - lb**3) + (coef['B']/2)*(ub**2 - lb**2) + 2*(ub - lb)
    assert math.isclose(area, shouldbe, rel_tol = 1e-2)

def test_keyword_and_posargs():
    coef = {'C':2, 'B':3}
    lb, ub = 0, 2
    area = trapz.trapzargs(quadratic, lb, ub, 1 , **coef)
    shouldbe = (1/3)*(ub**3 - lb**3) + (coef['B']/2)*(ub**2 - lb**2) + coef['C']*(ub - lb)
    assert math.isclose(area, shouldbe, rel_tol = 1e-2)
