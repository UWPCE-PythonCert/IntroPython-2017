"""
generator_solution.py lab
Generators for the following:
Sum of integers
Doubler
Fibonacci sequence
Prime numbers

"""
# class intsum():
#     def __init__(self):
#         self.sum = 0
#         self.current = 0
#     def __next__(self):
#         self.sum =

import math

def intsum(start=0, step=1):
    i = start
    total = start
    while True:
        yield total
        i += 1
        total += i


def doubler(start = 1, step = 1):
    i = start
    while True:
        yield i
        i = i * 2


def fib(a = 0, b = 1):
    x = a
    y = b
    yield y
    while True:
        x,y = y, x+y
        yield y

def fib2(a = 0, b = 1, limit = 10):
    count = 0
    x,y = a,b
    yield y
    while count <= limit:
        x,y = y, x+y
        yield y
        count += 1

def fib3(a = 0, b = 1, limit = 10):
    count = 0
    x,y = a,b
    yield y
    for count in range(limit-1):
        x,y = y, x+y
        yield y
        count += 1

def prime(start=2):
    i = start
    if i == 2:
        yield i
    while True:
        i += 1
        endofrange = int(math.sqrt(i))
        if endofrange < 2:
            endofrange = 2
        nums = (n for n in range(2, endofrange+1) if n == 2 or n % 2 != 0)
        for ints in nums:
            if i % ints == 0:
                break
        else:
            yield i

def prime2():
    primes = []
    a = 2
    while True:
        primes.append(a)
        yield a
        p = False
        while not p:
            # some stuff



