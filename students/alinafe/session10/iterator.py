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
        if stop == None:

            self._start = 0
            self._stop = start
            self._step = step
        else:
            self._start = start
            self._stop = stop
            self._step = step

    def __iter__(self):
        return _RangeIter(self._start, self._stop, self._step)


class _RangeIter:
    def __init__(self, start, stop, step):
        self._stop = stop
        self._step = step
        self._next_value = self._start

    def __next__(self):
        if self._tend():
            raise StopIteration()
        else:
            result = self._next_value
            self._next_value += self._step
            return result

    def __iter__(self):
        return self

    def _tend(self):
        return (self._step > 0 and self._next_value >= self._stop) or (
                self._step < 0 and self._next_value <= self._stop)


if __name__ == "__main__":

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)

    for i in it:
        print(i)

    print("Testing the iterator")
    it = IterateMe_2(2, 10, 2)

    for i in IterateMe_2(20):
        print(i)
