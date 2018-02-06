import time

class Timer():
    """
Time to read the number of seconds.
    """

    def __enter__(self):
        self.start = time.clock()
        return self.start

    def __exit__(self, *args):
        self.end = time.clock()
        self.duration = self.start - self.end


with Timer() as t:
    for i in range(100000):
        i = i **20
    print("This code took {} to run.".format(t))
