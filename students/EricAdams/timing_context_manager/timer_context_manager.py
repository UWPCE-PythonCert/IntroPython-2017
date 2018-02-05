#! /usr/bin/env python
'''
Create a simple timer context manager
'''
import time


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.process_time = time.clock() - self.start
        print('This code took {} seconds'.format(self.process_time))


if __name__ == '__main__':
    with Timer() as t:
        for i in range(100000):
            i = i ** 20
