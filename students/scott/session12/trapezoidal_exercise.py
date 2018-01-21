#!/usr/bin/env python

'''Your task is to write a trapz() function that will compute 
the area under an arbitrary function, using the trapezoidal rule.

The function will take another function as an argument, 
as well as the start and end points to compute, 
and return the area under the curve.
'''

from math import exp


def trapz(func, a, b, num):
    h = (b-a)/float(num)
    s = (func(a) + func(b))*(1/2)
    for i in range(1,num,1):
        s = s + func(a + i*h)
    return h*s


def passed_in_func(t):
    return exp(-t**4)

a = 2
b = 30
num = 100000
result = trapz(passed_in_func, a, b, num)
print(result)