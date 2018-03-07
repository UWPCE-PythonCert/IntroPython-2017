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
    def __init__(self, start, stop=None, step=1):
        
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
            
        self.step = step
        self.current = self.start - step
        

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
    for i in IterateMe_1(2, 20, 2):

        print(i)
    print("do the thing")
    
    for i in IterateMe_1(5):
        print(i)
        

