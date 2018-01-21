#!/usr/bin/env python

#generators

import math


#0, 1, 3, 6, 10, 15
def intsum():
    a = 0
    b = 0
    while True:
        yield b
        a += 1
        b = b + a


def intsum2():
    pass


#1, 2, 4, 8, 16, 32, 64
def doubler():
    a = 1
    while True:
        yield a
        a = a * 2


#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fib():
    a = 0
    b = 1
    yield a
    while True:
        yield b
        a,b = b, a+b


#2, 3, 5, 7, 11, 13, 17, 19, 23
##only divisible by itself and 1 ( so would have no remainder)
#start at 2
def prime():
    start = 2



#X^2
#1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121
def squared():
    a = 1
    while True:
        yield a
        a = a ** 2
# this doesn't pass yet, of course....not sure how to set a to the **, yet still have a be the basis of the next **
## so if a=2 and I square it, then a =4, and I can't have a=3 to square that next time around....

