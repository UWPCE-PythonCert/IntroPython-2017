#!/usr/bin/env python3
"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
"""
def date_fashion(you, date):
    if (you <= 2) or (date <= 2):
      return 0
    elif (you >= 8) or (date >= 8):
      return 2
    else:
      return 1

print(date_fashion(10,5))

if __name__ == "__main__":
    # some tests

    assert date_fashion(5, 10) is 2
    assert date_fashion(5, 2) is 0
    assert date_fashion(5, 5) is 1
    assert date_fashion(3, 3) is 1
    assert date_fashion(10, 2) is 0
    assert date_fashion(2, 9) is 0
    assert date_fashion(9, 9) is 2
    assert date_fashion(10, 5) is 2
    assert date_fashion(2, 2) is 0
    assert date_fashion(3, 7) is 1
    assert date_fashion(2, 7) is 0
    assert date_fashion(6, 2) is 0

    print("All tests passed")
