#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1():
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

class IterateMe_2():
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_2(2,25,4):
        print(i)


# I was able to get the iterator to act like range for 2 or 3 arguments, but couldn't figure out how to do it for 1 argument
