#! /usr/bin/env python

fib_cache= {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        fib_cache[n] = value
        return value


for i in range(50):
    print(i, ":" , fibonacci(i))