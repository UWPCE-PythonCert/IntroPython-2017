import pytest, math

from trapz import trapz

def test_line():
    '''
    This test the Trapazoidal Function against a straight line
    '''
    def line(x):
        return 5

    area = trapz(line, 0, 10)
    assert math.isclose(area, 50, rel_tol=0.05, abs_tol=0.0)

def test_slopped_straight():
    '''
    This test the Trapazoidal Function against a slopped straight line
    '''
    def ssline(x, m=1, B=0):
        return (m * x) + B

    area = trapz(ssline, 0, 4)
    assert area == 8

#def test_quadratic(x, A=0, B=0, C=0):
#    return A * x**2 + B * x + C