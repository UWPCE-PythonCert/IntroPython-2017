#!/usr/bin/env python

import time

class Timer:
    def __init__(self, name=""):
        self.name = name if name else ""


    def __enter__(self):
        self.start_time = time.clock()


    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.clock() - self.start_time
        print("Function {} took {} seconds.".format(self.name, elapsed_time))


if __name__ == "__main__":
    with Timer():
        range(1000)


    with Timer(name="sum range 1000"):
        sum(range(1000))
