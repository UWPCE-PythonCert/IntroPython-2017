# make a row that is goal inches log
# 1" bricks and 5" bricks

def make_bricks(num_small, num_big, goal):
    if num_small * 1 + num_big * 5 < goal:
        return False
    needed_large = goal // 5
    needed_small = goal % 5


    print("needed_small:", needed_small)
    print("needed_large:", needed_large)









assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(0, 2, 8) is False

