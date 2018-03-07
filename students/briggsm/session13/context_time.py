import time

class Timer():
    """
Time to read the number of seconds.
    """

    def __init__ (self):
        self.start = 0.0
        self.end = 0.0
        self.duration = 0.0

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, type, value, traceback):
        self.end = time.clock()
        self.duration = self.end - self.start
        return False


with Timer() as t:
    for i in range(100000):
        i = i **20

print("This code took {} to run.".format(t.duration))