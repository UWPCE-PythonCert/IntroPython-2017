def fibonacci(n):
    """ Print the fibonacci series nth value. """
    return sum_series(n)

def series_not_implemented(n):
    return sum_series(n, x=4, y=5)
    

def lucas(n):
    """ Print the lucas series nth value."""
    return sum_series(n, x=2, y=1)

def sum_series(n, x=0, y=1):
    """ Perform series calculation for implemented Lucas and Fibonacci series.
        Indicate to the user if the series is not implemented. n is the nth value
        in the series. x=0, y=1 indicates a Fibonacci series, x=2, x=1 indicates 
        Lucas series. """
    if x == 0 and y == 1:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fibonacci_sum = sum_series(n-2) + sum_series(n-1)
            return fibonacci_sum
    if x ==2 and y == 1:
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            lucas_sum = sum_series(n-2, x=2, y=1) + sum_series(n-1, x=2,y=1)
            return lucas_sum
    else:
        # print("Series not implemented")
        return "Series not implemented"


# Test for various values and also test for unimplemented series

assert fibonacci(0) == 0                              # 
assert lucas(0) == 2
assert series_not_implemented(0) == "Series not implemented"
assert fibonacci(4) == 3
assert lucas(4) == 7
assert fibonacci(1) == 1
assert lucas(1) == 1





