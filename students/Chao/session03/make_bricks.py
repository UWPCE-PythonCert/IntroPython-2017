#!/usr/bin/env python

def make_bricks(sb, lb, goal):
    do_large = goal//5
    do_small = goal - lb*5
    if do_large >= lb:
        left = goal%5
        if sb >= left:
            return True
        else:
            return False
    elif do_small >= sb:
        return False
    else:
        return True
        


