#! /usr/bin/env python
'''
Create a simple timer context manager to take a file object and write to it
'''
import time
import sys


class Timer():

    def __init__(self, file_object=sys.stdout):
        self.file_object = file_object

    def __enter__(self):
        self.start = time.clock()
        self.name = 'timer_writing_to_file'
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.process_time = time.clock() - self.start
        self.file_object.write(
            '{1}: This code took {0} seconds'.format(self.process_time,
                                                     self.name))


if __name__ == '__main__':
    with Timer() as t:
        for i in range(100000):
            i = i ** 20

    with open('timer.txt', 'w') as fopen:
        with Timer(fopen) as t:
            for i in range(100000):
                i = i ** 20
