#!/usr/bin/env python3
"""
A function that calls itself is recursive; the process is called recursion.
As another example, we can write a function that prints a string n times.

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
"""
def print_n(s, n):
    while n > 0:
      print(s)
      n = n -1
