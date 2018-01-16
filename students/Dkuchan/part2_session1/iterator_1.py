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
    def __init__(self, begin, stop, steps):
        self.current = begin
        self.stop = stop
        self.steps = steps  # creates attribute steps
    def __iter__(self):
        return self
    def __next__(self):
        self.current += self.steps
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    print("Testing the iterator")
    daniterable = IterateMe_1(1, 1000, 1)


for i in daniterable:
    if i > 10 : break
    print(i)
for i in daniterable:
    print(i)

testiteratorthing = range(1,1000,1)
for i in testiteratorthing:
    if i > 10 : break
    print(i)
for i in testiteratorthing:
    print(i)
