#!/usr/bin/env python

def make_bricks(small, big, goal):
    if goal - (big*5) > small:
        return False
    elif goal == small:
        return True



assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(0, 2, 8) is False
assert make_bricks(10, 1, 12) is True