#!/usr/bin/env python3

# make_bricks

def make_bricks(small, big, goal):
    if (goal - 5 * min(goal // 5, big)) > small:
        return False
    return True

assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(0, 2, 8) is False
assert make_bricks(10, 1, 12) is True


# lone_sum

# this is not a good solution, but it works

def lone_sum(a, b, c):
    if (a != b) and (b != c) and (a != c):
        return (a + b + c)
    elif (a == b) and (b != c):
        return c
    elif (a == c) and (b != c):
        return b
    elif (b == c) and (a != b):
        return a
    else:
        return 0


assert lone_sum(1, 2, 3) is 6
assert lone_sum(3, 2, 3) is 2
assert lone_sum(3, 3, 3) is 0


# lucky_sum

def lucky_sum(a, b, c):
    if a == 13:
        return c
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c

assert lucky_sum(1, 2, 3) is 6
assert lucky_sum(1, 2, 13) is 3
assert lucky_sum(1, 13, 3) is 1