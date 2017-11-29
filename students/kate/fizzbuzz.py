#! /usr/bin/env python
"""
fizz buzz exersize
"""

def fizzbuzz(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
    return(num)

fizzbuzz(100)
