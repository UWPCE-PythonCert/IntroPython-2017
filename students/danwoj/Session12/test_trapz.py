import pytest, math

from trapz import trapz, quadratic

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

    def ssline2(x, m=1, B=1):
        return (m * x) + B

    area = trapz(ssline, 0, 4)
    area2 = trapz(ssline2, 0, 4)
    assert math.isclose(area, 8, rel_tol=0.01, abs_tol=0.0)
    assert math.isclose(area2, 12, rel_tol=0.01, abs_tol=0.0)

#def test_quadratic():

#    def quadratic(x, *args, **kwargs):
#        result = A * x**2 + B * x + C
#        return result

#    area = trapz(quadratic, 2, 20, A=1, B=3, C=2)
#    assert area == 14

def test_quadratic_1():
    """
    one set of coefficients
    """
    assert quadratic(x, A=1, B=1, C=1) == y