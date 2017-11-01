#!/usr/bin/env python

def fibonacci(n):
    """return the nth value of the fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    print(fibonacci(26))




def lucas(n):
    """returns the nth value of the Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)



def sum_series(n, y, z):
    """returns the nth value of the series, with the default starting values of 0 and 1"""
    y = 0
    z = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum_series(n-1, y, z) + sum_series(n-2, y, z)

