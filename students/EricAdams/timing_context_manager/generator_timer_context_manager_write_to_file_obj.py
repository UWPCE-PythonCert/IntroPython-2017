#! /usr/bin/env python
'''
Implement a simple timer context manager as a generator to take a file
object and write to it. Wrap it all in the contextlib.contextmanager
'''
import time
import sys
from contextlib import contextmanager


class Timer:
    def __init__(self, file_object=sys.stdout):
        self.file_object = file_object

    @contextmanager
    def process_it(self):
        self.start = time.clock()
        self.name = 'wrapped_timer_writing_to_file'
        yield self.name
        self.process_time = time.clock() - self.start
        self.file_object.write(
            '{1}: This code took {0} seconds'.format(self.process_time,
                                                     self.name))


if __name__ == '__main__':
    time_it = Timer()
    with time_it as t:
        for i in range(100000):
            i = i ** 20

    with open('timer.txt', 'w') as fopen:
        with time_it(fopen) as t:
            for i in range(100000):
                i = i ** 20
