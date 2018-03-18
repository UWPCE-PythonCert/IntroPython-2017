#!/usr/bin/env python

'''
The number 6 is a truly great number. Given two int values, a and b, 
return True if either one is 6. Or if their sum or difference is 6. Note: 
the function abs(num) computes the absolute value of a number.
'''

def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif a-b == 6 or b-a == 6:
    return True
  elif a+b == 6:
    return True
  else:
    return False