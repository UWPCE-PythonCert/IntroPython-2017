def fibonacci(n):
    """ Print the fibonacci series nth value. """
    return sum_series(n)
    
def lucas(n):
    """ Print the lucas series nth value."""
    return sum_series(n, x=2, y=1)

def sum_series(n, x=0, y=1):
    """ Perform series calculation for implemented Lucas and Fibonacci series.
        Indicate to the user if the series is not implemented. n is the nth value
        in the series. x=0, y=1 indicates a Fibonacci series, x=2, x=1 indicates 
        Lucas series. """
    if n == 0:
        return x
    if n == 1:
        return y
    sum = sum_series(n-2, x, y) + sum_series(n-1, x, y)
    return sum


# Test for various values and also test for unimplemented series

assert fibonacci(0) == 0                              # 
assert lucas(0) == 2
assert fibonacci(4) == 3
assert lucas(4) == 7
assert fibonacci(1) == 1
assert lucas(1) == 1





