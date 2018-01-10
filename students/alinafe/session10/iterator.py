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
        return self
    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)


class IterateMe_2:
    """
    add three input parameters: iterator_2(start, stop, step=1)

    """

    def __init__(self, start, stop=None, step=1):
        self.current = -1
        self.start = start

    def __iter__(self):
        self.current = -1
        print("in __iter__")
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_2(2, 10, 2)

    for i in IterateMe_2(20):
        print(i)
 
