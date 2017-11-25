#!/usr/bin/env python

'''
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 
1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 
or more, the result is 2. Unless it is your birthday -- on that day, your 
speed can be 5 higher in all cases.
'''

def caught_speeding(speed, is_birthday):
  if is_birthday:
    x = 5
  else:
    x = 0
  if speed <= 60+x:
    return 0
  elif 61+x <= speed <= 80+x:
    return 1
  else:
    return 2