import math

def soi(start, stop):
    '''
    This is my Sum of Integers generator function
    '''
    i = start
    for j in range(stop):
        yield i
        if j == 0:
            i += 1
        else:
            i += j+1

def doubler(start, stop):
    '''
    This is my Doubler generator function
    '''
    if start == 0:
        raise ValueError('Cannot use the value 0.')
    i = start
    for j in range(1,stop):
        yield i
        i = i * 2

def fib():
    '''
    This is my Fibonacci Sequence function
    '''
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i + j

def primes(start=2):
    '''
    This is my Prine Number function
    '''
    value = start
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(value) + 1)):
            if not value % x: 
                isprime = False
                break
        if isprime:
            yield value
        value += 1

def ecount(start=2, step=2):
    '''
    This generator function returns a exponential numeric sequence based 
    on a specified base number and step. If none if provided, the 
    function defaults with base value 2 with a step of 2.
    '''
    value, exponent = start, step
    while True:
        yield value ** exponent
        exponent += step