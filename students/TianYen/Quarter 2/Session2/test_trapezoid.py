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

#def test_quad_with_coefficents():
#    assert math.isclose(trapz(quad, 0, 3, 1), 9, rel_tol=.0001)
