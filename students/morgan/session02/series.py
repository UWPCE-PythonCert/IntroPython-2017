def fib(n):
    """ fibonacci sequence , adds last two numbers to find next"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)  

def lucas(n):
    """ lucas number sequence. same as fib but starts with 2 and 1"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

def sum_series(n, b=0, c=1):
    """an ad-hoc version of fib and lucas, same math but with different seed values being optional
    if the optional values aren't used, default to the fibonacci seeds of 0 and 1"""

    if n == 0:
        return b
    if n == 1:
        return c
    return sum_series(n-1, b, c) + sum_series(n-2,b,c)

if __name__ == '__main__':

    assert fib(0) == 0
    assert fib(1) == 1
    print(fib(2))

    assert lucas(0) == 2
    assert lucas(1) == 1
    print(lucas(2))

    assert sum_series(0,3,8) == 3
    assert sum_series(1,3,8) == 8
    assert sum_series(2,3,8) == 11
    assert sum_series(3,3,8) == 19
    print(sum_series(4,3,8))


