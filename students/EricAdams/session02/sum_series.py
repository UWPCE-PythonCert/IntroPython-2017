def fibonacci(n):
    """ Print the fibonacci series nth value. """
    return sum_series(n)
    
def lucas(n):
    """ Print the lucas series nth value."""
    return sum_series(n, 2, 1)

def sum_series(n, x=0, y=1):
    """ Return the nth element in a series similar to fibonacci
     The named parameters indicate the first and second element in the 
     series. 
     """
    if n == 0:
        return x
    if n == 1:
        return y
    sum = sum_series(n-2, x, y) + sum_series(n-1, x, y)
    return sum


# Test for various values()

assert fibonacci(0) == 0                              # 
assert lucas(0) == 2
assert fibonacci(4) == 3
assert lucas(4) == 7
assert fibonacci(1) == 1
assert lucas(1) == 1

# The sum_series by itself can be used

assert sum_series(4, 2, 1) == 7
assert sum_series(4) == 3





