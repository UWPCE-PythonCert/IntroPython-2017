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
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop
    def __iter__(self):
        self.current = -1
        return self
    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(IterateMe_1):
    """ Override IterateMe_1 and give it range like behavior
    """
    def __init__(self, start, stop=None, step=1):
        real_stop = None

        if stop is None:
            real_stop = start
        else:
            real_stop = stop

        super(IterateMe_2, self).__init__(real_stop)

        if stop is not None:
            self.current = (step * -1) + start

        self.step = step

    def __next__(self):
        self.current += self.step

        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)

    print("Testing IterateMe_2")
    for i in IterateMe_2(2, 20, 2):
        print(i)

    print("Testing IterateMe_2 with one value")
    for i in IterateMe_2(20):
        print(i)

    print("Testing IterateMe_2 with two values")
    for i in IterateMe_2(3,6):
        print(i)
