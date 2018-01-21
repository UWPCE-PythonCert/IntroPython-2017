"""
generator_solution.py

Solutions for the generator lab excercises.

"""


def intsum():
    '''sum using generator
    '''
    x = list(range(0, 1000))
    total = 0
    for y in x:
        total = total + y
        yield total


def doubler():
    '''Double the previous value using a generator
    '''
    x = list(range(1, 1000))
    for i, y in enumerate(x):
        yield 2 ** i


def fib(n):
    '''fibonacci generator
    Thanks to https://www.python-course.eu/generators.php
    '''
    a, b, counter = 1, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


def prime():
    """ Generate an infinite sequence of prime numbers.
    This code is straight outta stackoverflow.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

