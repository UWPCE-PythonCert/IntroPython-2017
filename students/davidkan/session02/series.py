#!usr/bin/env python
# Description: Write a program for fib exercise
# Comment: Execute in Python3.6
# Last modified: 10/17/2017 by davidkan@


def fib(n):
    # You can call a function within itself
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    # assert if fib is equal to 0
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    print(fib(10))

