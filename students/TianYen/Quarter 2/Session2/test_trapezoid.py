import math
from trapezoid import trapz, frange

def line(x):
    return 5

def quad(x):
    return x**2

def quad2(x, A=0,B=0,C=0):
    return A * x**2 + B * x + C

def test_line():
    assert trapz(line, 0, 10) == 50

def test_quad():
    assert math.isclose(trapz(quad, 0, 3), 9, rel_tol=.0001)

def test_sin():
    assert math.isclose(trapz(math.sin, 0, math.pi/2), 1, rel_tol=.0001)

def test_quad_with_coefficents():
    assert math.isclose(trapz(quad2, 0, 3, 1), 9, rel_tol=.0001)

def test_quad2():
    coef = {'A':1, 'B':3, 'C': 2}
    assert math.isclose(trapz(quad2, 2, 20, 1,1,1), 2880, rel_tol=.0001)
    assert math.isclose(trapz(quad2, 2, 20, 1,B=3,C=2), 3294, rel_tol=.0001)
    assert math.isclose(trapz(quad2, 2, 20, 1,3,C=2), 3294, rel_tol=.0001)
    assert math.isclose(trapz(quad2, 2, 20, **coef), 3294, rel_tol=.0001)

#def test_sin_with_key():
#    assert math.isclose(trapz(math.sin, 0, math.pi/2, A=4, w=2), 2(math.cos(2*0) - math.cos(pi)))
