#!/usr/bin/env python

'''Your task is to write a trapz() function that will compute 
the area under an arbitrary function, using the trapezoidal rule.

The function will take another function as an argument, 
as well as the start and end points to compute, 
and return the area under the curve.
'''

from math import exp


def trapz(func, a, b, num):
    first_part = (b-a)/float(num)
    second_part = (func(a) + func(b))*(1/2)
    for i in range(1,num,1):
        second_part = second_part + func(a + i * first_part)
    
    return first_part * second_part


def passed_in_func(t):
    return exp(t**3)

a = 2
b = 30
num = 100000
result = trapz(passed_in_func, a, b, num)
print(result)