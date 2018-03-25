from datetime import datetime

class Timer():
    def __init__(self, outfile=None):
        self.start = 0
        self.end = 0
        self.total = 0
        self.path = outfile


    def __enter__(self):
        self.start = datetime.now()
        print(self.start,'start')

    def __exit__(self, *args):
        self.end = datetime.now()
        print(self.end,'end')
        delta = self.end - self.start
        self.total = delta.total_seconds()
        print(self.total, 'total')
        print("This code took {total} seconds".format(total=self.total))
        if self.path is not None:
            with open(self.path, 'w') as f:
                f.write("This code took {total} seconds".format(total=self.total))




with Timer('output.txt') as t:
    x = 0
    for i in range(100000):
        i = i ** 20
        x = i
    print(x, 'output')


