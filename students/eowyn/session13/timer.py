"""
Record how long something takes to run. Print result and write to file,
if a file object is provided. Otherwise print to stdout (screen). An
optional name argument allows for the function being timed to be
given a name which is logged.
"""

import sys
import contextlib


class Timer():
    def __init__(self, fileobj=sys.stdout, name=""):
        if name:
            self.name = name
        else:
            self.name = "This code"
        self.fileobj = fileobj

    def __enter__(self):
        from time import clock
        self.starttime = clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        from time import clock
        self.endtime = clock()
        self.elapsed = self.endtime - self.starttime
        result = "{} took {:.4f} seconds.\n".format(self.name, self.elapsed)
        self.fileobj.write(result)


"""
Refactor as a generator
"""


@contextlib.contextmanager
def timer(fileobj=sys.stdout):
    from time import clock
    starttime = clock()
    yield object()
    elapsed = clock() - starttime
    result = 'This code took {:.4f} seconds.\n'.format(elapsed)
    fileobj.write(result)
