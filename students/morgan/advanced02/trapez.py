import math
from iterator_1 import IterateMe_1






def trapezoid(func, start, end, **kwargs):
    intervals = end-start
    delta_x = (end - start) / intervals
    total = func(start) / 2

    floatrange = IterateMe_1(start, end-1)

    for i in floatrange:
        total += func(start + (delta_x * i))

    # for i in floatrange(1,intervals):
    #     total += func(start + (delta_x * i))




    # for i in range((1, intervals):
    #     # print(delta_x * i)
    #     total += func(start + (delta_x * i))
    total += func(end) / 2
    return total * delta_x

def line(x):
    return 5


def slope_line(x):
    return m*x+B






# print(trapezoid(line, 0, 10, 10))
print(trapezoid(line, 0, 10))
