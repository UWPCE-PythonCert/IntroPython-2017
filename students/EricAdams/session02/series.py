def fibonacci(n):
    """ Return the fibonacci series nth value. """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n - 1)
    

def fib_series(n):
    """ Print the nth value of the fibonacci series."""
    print ('fibonacci(',n,') = ', fibonacci(n))
    return 0

def lucas(n):
    """ Return the lucas series nth value."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-2) + lucas(n-1)

def lucas_series(n):
    """ Print the nth value of the fibonacci series."""
    print ('lucas(',n,') = ', lucas(n))

    


fib_series(2) 
fib_series(6)
lucas_series(0)
lucas_series(1)
lucas_series(7)
