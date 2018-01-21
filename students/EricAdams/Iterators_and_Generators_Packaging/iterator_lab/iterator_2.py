#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, *args):
        # self.current = -1
        if len(args) == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            print("Usage: must have at least 1 parameter but no more than 3 \
                   integers only please")
        self.current = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if (self.current < self.stop) and self.step > 0:
            return self.current
        elif (self.current > self.stop) and self.step < 0:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    # for i in IterateMe_1(10):
    #     print(i)

    for i in IterateMe_1(-5, 10, 1):
        print(i)

    for i in IterateMe_1(-10, -5, 1):
        print(i)

    for i in IterateMe_1(10):
        print(i)

    for i in IterateMe_1(10,,-1):
        print(i)
