# Fibonacci series exercise
# Python 3.6


def fib(n): 
    """ Returns fibonacci result for given input """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-2) + fib(n-1)


def lucas(n):
    """ Returns the lucas result for given input """
    if n is 0:
        return 2
    elif n is 1:
        return 1

    return lucas(n-2) + lucas(n-1)


def sum_series(n, first=0, second=1):
    """
    Returns a generalized result with option to define the first
    two values. Default values will produce fibonacci sequence.
    """
    if n is 0:
        return first
    elif n is 1:
        return second

    return sum_series(n-2, first, second) + sum_series(n-1, first, second)