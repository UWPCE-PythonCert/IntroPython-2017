"""
Kathryn Egan

Computes Fibonacci, Lucas, and arbitrary series with
a given first and second base case to the nth value.
N is an ordinal starting at 1.
"""


def fibonacci(n):
    """ Returns the nth value in the Fibonacci series.
    Args:
        n (int) : nth value to compute
    Returns:
        int : current value
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """ Returns the nth value in the Lucas series.
    Args:
        n (int) : nth value to compute
    Returns:
        int : current value
    """
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n - 2) + lucas(n - 1)


def sum_series(n, base0, base1):
    """ Returns the nth value in an arbitrary series with
    given base cases.
    Args:
        n (int) : nth value to compute
        base0 (int) : value of first in series
        base1 (int) : value of second in series
    Returns:
        int : current value
    """
    if n == 1:
        return base0
    if n == 2:
        return base1
    return (
        sum_series(n - 2, base0, base1) +
        sum_series(n - 1, base0, base1))


def test(module, solutions, **kwargs):
    """ Tests given module against a solution.
    Assumes kwargs will have base0 and base1 if
    sum_series is passed.
    Args:
        module (function) : module to test
        solutions (list ints) : solutions as a list of ints
        kwargs (dict) : optional base0 and base1 args for sum_series
    """
    if not kwargs:
        for i in range(len(solutions)):
            assert module(i + 1) == solutions[i]
    elif 'base0' in kwargs and 'base1' in kwargs:
        for i in range(len(solutions)):
            answer = module(i + 1, kwargs['base0'], kwargs['base1'])
            assert answer == solutions[i]
    print('Could not test ' + str(module))


real_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
real_lucas = [2, 1, 3, 4, 7, 11, 18, 29]

test(fibonacci, real_fib)
test(lucas, real_lucas)
test(sum_series, real_fib, base0=0, base1=1)
test(sum_series, real_lucas, base0=2, base1=1)

print("Passed all tests")
