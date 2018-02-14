#!/usr/bin/env python

"""
Simple iterator examples

Edited by Kathryn Egan
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, arg1, arg2=None, arg3=1):
        self.start = 0
        self.stop = None
        # only stop is given
        if arg2 is None:
            self.stop = arg1
        # at least start and stop are given
        else:
            self.start = arg1
            self.stop = arg2
        self.current = self.start
        self.step = arg3
        if self.step == 0:
            raise ValueError
        if self.step < 0:
            self.current = self.stop

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        temp = self.current
        self.current += self.step
        return temp


# if __name__ == "__main__":

#     print("Testing the iterator")
#     start = 1
#     stop = 10
#     step = 15

#     my_range = IterateMe_1(start, stop, step)
