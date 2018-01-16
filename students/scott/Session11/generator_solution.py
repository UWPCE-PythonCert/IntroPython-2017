#!/usr/bin/env python

#generators

import math


def intsum():
    a = 0
    b = 0
    while True:
        yield b
        a += 1
        b = b + a

def intsum2():
    pass

def doubler():
    a = 1
    while True:
        yield a
        a = a * 2

def fib():
    a = 0
    b = 1
    while True:
        yield b
        a,b = b, a+b

def prime():
    

