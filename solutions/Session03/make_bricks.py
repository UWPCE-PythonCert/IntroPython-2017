# make a row that is goal inches long
# 1" bricks and 5" bricks

def make_bricks(num_small, num_big, goal):
    #if num_small * 1 + num_big * 5 < goal:
    #    return False

    if goal % 5 > num_small:
        return False
    if goal - (num_big * 5) > num_small:
        return False
    return True


    # needed_large = goal // 5
    # if goal % 5 <= num_small and goal // 5  <= num_big:
    #     return True
    # # elif num_small > 5:
    # if needed_large <= num_big:
    #     diff = goal - needed_large*5
    #     if diff <= num_small:
    #         return True
    # else:
    #     leftover = goal - num_big*5
    #     if leftover <= num_small:
    #         return True
    # return False

    # if needed_large > num_big:
    #     return False
    # needed_small = goal % 5
    # if needed_small > num_small:
    #     return False

    print("needed_large:", needed_large)
    print("needed_small:", needed_small)

    return True

assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(0, 2, 8) is False
assert make_bricks(10, 1, 12) is True




