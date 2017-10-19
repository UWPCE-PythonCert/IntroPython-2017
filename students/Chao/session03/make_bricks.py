#!/usr/bin/env python

def make_bricks(sb, lb, goal):
    """ Function to make bricks
        sb = small brick, lb = large brick
        do_large = how many large bricks can be used
        do_small = how many small bricks are needed after large bricks are used
    """
    do_large = goal//5
    do_small = goal - lb*5
    if lb >= do_large:
        left = goal%5
        if sb >= left:
            return True
        else:
            return False
    elif do_small > sb:
        return False
    else:
        return True
        

if __name__ == '__main__':
    """ Some tests """
    assert make_bricks(3, 1, 8) == True
    assert make_bricks(2, 1000000, 100003) == False
    assert make_bricks(22, 2, 33) == False
    assert make_bricks(40, 2, 47) == True
    assert make_bricks(20, 4, 39) == True

    print('passed!')
