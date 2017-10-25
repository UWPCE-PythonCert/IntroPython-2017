
"""
the make_bricks problem from coding bat

Make a row that is goal inches long

The small bricks are 1"
The big bricks are 5"

You are given a certain number of small and big bricks.

Is it possible to make a row of goal length?
"""


def make_bricks(num_small, num_big, goal):
    """
    This is a nice compact solution

    Just the amount of logic needed, and no more
    """
    # use all the big bricks, not enough small left to fill in
    if goal % 5 > num_small:
        return False
    # use the max number of big bricks that will fit, not enough small to fill in.
    if goal - (num_big * 5) > num_small:
        return False
    # good to go
    return True


# test the first solution
assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(0, 2, 8) is False
assert make_bricks(10, 1, 12) is True

def make_bricks2(num_small, num_big, goal):
    """
    A bit more complex than it needs to be, but it works
    """
    needed_big = goal // 5
    if goal % 5 <= num_small and needed_big <= num_big:
        return True
    if needed_big <= num_big:
        diff = goal - needed_big * 5
        if diff <= num_small:
            return True
    else:
        leftover = goal - num_big * 5
        if leftover <= num_small:
            return True
    return False


# test the second solution
assert make_bricks2(3, 1, 8) is True
assert make_bricks2(3, 1, 9) is False
assert make_bricks2(0, 2, 8) is False
assert make_bricks2(10, 1, 12) is True


def make_bricks3(num_small, num_big, goal):
    """perhaps the most compact"""
    # use either the number of big bricks that will fit,
    # or the number you have, not enough small to fill.
    if (goal - 5 * min(goal // 5, num_big)) > num_small:
        return False
    return True


# test the third solution
assert make_bricks3(3, 1, 8) is True
assert make_bricks3(3, 1, 9) is False
assert make_bricks3(0, 2, 8) is False
assert make_bricks3(10, 1, 12) is True
