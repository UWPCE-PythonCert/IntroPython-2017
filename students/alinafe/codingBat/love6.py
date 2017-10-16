#!/usr/bin/env python3
"""
The number 6 is a truly great number. Given two int values, a and b, return True if either 
one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the 
absolute value of a number.
"""
def love6(a, b):
  return a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6
What, this looks ugly you say? I completely agree, and there is a much more pleasant solution:

def love6(a, b):
  return 6 in [a, b, a + b, abs(a - b)]
