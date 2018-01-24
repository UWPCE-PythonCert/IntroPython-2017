

def frange(start, stop, step):
    """range function that allows for floating point variables"""
    i = start
    while i < stop:
        yield i
        i += step

def trapz(func, a, b):
    """trapezoidal approximation of the area under a curve"""
    n = 100
    step = (b - a) / n
    return step * ((func(a) + func(b)) / 2 + sum([func(x) for x in frange(a + step, b - step, step)]))
