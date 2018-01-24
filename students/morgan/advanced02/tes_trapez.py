import trapez
import math
from iterator_1 import IterateMe_1

def test_line4():
    area = trapez.trapezoid(trapez.line,0,10)

    assert area == 50

def test_sin():
    area = trapez.trapezoid(math.sin,0,10)
    print(area, 'area')

def test_floatrange():
    floatrange = IterateMe_1(0,10,1)
    for x in floatrange:
        temp = x
    assert temp == 9

def test_slope_line():
    area = trapez.trapezoid(trapez.slope_line,0,10)
    print(area, "slopeline")
