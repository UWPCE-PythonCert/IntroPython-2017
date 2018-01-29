import pytest

from generators import soi, doubler, fib, primes, ecount

def test_soi():
    '''
    Tests the Sum of Integers function
    '''
    start_value = 0
    stop_value = 10
    x = soi(start_value, stop_value)
    y = next(x)
    for i in range(stop_value-1):
        z = next(x)
        print(z)
    assert y == 0
    assert z == 45

def test_doubler():
    '''
    Tests the Doubler function
    '''
    start_value1 = 1
    start_value2 = 0
    stop_value = 10
    x = doubler(start_value1, stop_value)
    y = next(x)
    for i in range(stop_value-2):
        z = next(x)
#    a = doubler(start_value2, stop_value)
#    for i in range(stop_value-2):
#        b = next(a)
    assert y == 1
    assert z == 256
#    assert b == ValueError

def test_fib():
    '''
    Tests the Fibonacci Numbers function
    '''
    x = fib()
    for i in range(10):
        y = next(x)
    assert y == 34

    a = fib()
    for i in range(1):
        z = next(a)
    assert z == 0

    b = fib()
    for i in range(4):
        c = next(b)
        print(c)
    assert c == 2

def test_primes():
    '''
    Tests the Prime Number function
    '''
    x = primes()
    for i in range(10):
        y = next(x)
    assert y == 29
    a = primes(10000)
    b = next(a)
    assert b == 10007

def test_ecount():
    '''
    Tests the Ecount function
    '''
    x = ecount()
    for i in range(10):
        y = next(x)
    assert y == 1048576
    a = ecount(3,7)
    b = next(a)
    assert b == 2187
