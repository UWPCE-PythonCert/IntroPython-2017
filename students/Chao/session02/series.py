#!/usr/bin/env python

"""
IntroPython-2017
Session02
Fibonacci and Lucas Series Exercises
"""

def fib(n):
    """
    nth Fibonacci number implementation with recursion
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def new_fib(n):
    """
    A new Fibonacci number implementation
    Calling sum series function with start numbers 0 and 1
    No optional parameter input here since default sum series function works as fib
    """
    return(sum(n))


def luc(n):
    """
    nth Lucas number implementation with recursion
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return luc(n-1) + luc(n-2)

def new_luc(n):
    """
    A new Lucas number implementation
    Calling sum series function with start numbers 2 and 1
    """
    return(sum(n, 2, 1))

def sum(n, a=0, b=1):
    """
    Sum series implementation
    One required parameter n
    Two optional parameters a and b
    The default a == 0 and b == 1 which will compute nth Fibonacci number
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    return sum(n-1, a, b) + sum(n-2, a, b)


if __name__ == '__main__':
    """
    Some tests for "old" Fibonacci and Lucas functions
    """
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(10) == 55
    assert luc(1) == 1
    assert luc(5) == 11
    assert luc(10) == 123

    """
    tests for Sum series function
    """
    assert sum(1) == 1
    assert sum(5) == 5
    assert sum(10) == 55
    assert sum(1, 2, 1) == luc(1)
    assert sum(5, 2, 1) == luc(5)
    assert sum(10, 2, 1) == luc(10)

    """
    tests for new Fibonacci and Lucas functions
    """
    assert new_fib(1) == 1
    assert new_fib(5) == 5
    assert new_fib(10) == 55
    assert new_luc(1) == 1
    assert new_luc(5) == 11
    assert new_luc(10) == 123

    print('Pass!')