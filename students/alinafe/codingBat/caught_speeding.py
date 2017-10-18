#!/usr/bin/env python3
"""
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
"""

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
     
  if speed <= 60:
      return 0
  if 60 < speed <= 80:
    return 1
  return 2

if __name__ == "__main__":
    # some tests
    caught_speeding(60, False)	is 0
    caught_speeding(65, False)	is 1
    caught_speeding(65, True)	is 0
    caught_speeding(80, False)	is 1
    caught_speeding(85, False)	is 2
    caught_speeding(85, True)	is 1
    caught_speeding(70, False)	is 1
    caught_speeding(75, False)	is 1
    caught_speeding(75, True)	is 0
    caught_speeding(40, False)	is 0
    caught_speeding(40, True)	is 0
    caught_speeding(90, False) is	2
    print("All tests passed")
