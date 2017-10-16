#!/usr/bin/env python3
def sorta_sum(a, b):
  if 10 <= a + b < 20:
    return 20
  return a + b

if __name__ == "__main__":
    assert sorta_sum(3, 4)	is 7
    assert sorta_sum(9, 4)	is 20
    assert sorta_sum(10, 11) is	21
    assert sorta_sum(12, -3) is	9
    assert sorta_sum(-3, 12) is	9
    assert sorta_sum(4, 5)	is 9
    assert sorta_sum(4, 6)	is 20
    assert sorta_sum(14, 7) is	21
    assert sorta_sum(14, 6) is	20
    print("All tests passed")
