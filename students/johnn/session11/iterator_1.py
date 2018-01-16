class IterateMe_1:
    def __init__(self, *args):
        start = 0
        step = 1
        # if there is only one parameter, it's stop
        if len(args) == 1:
            stop = args[0]
        else:
            # everything from here on out is optional, so get
            # what's there, and use defaults if not
            try:
                start = args[0]
            except IndexError:
                pass
            try:
                stop = args[1]
            except IndexError:
                pass
            try:
                step = args[2]
            except IndexError:
                pass
        self.current = start - step
        self.step = step
        self.stop = stop
        #print("start", start, "stop", stop, "step", step)
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration
