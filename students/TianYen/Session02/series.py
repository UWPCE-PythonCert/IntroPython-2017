def fibonacci(n):
    """return the nth value in the fibonacci sequence"""
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """return the nth value in the lucas series"""
    if n < 0:
        return None
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, value1 = 0, value2 = 1):
    """return the nth value of the given series
     where value1 and value2 are the first two values in the series"""
    if n < 0:
        return None
    if n == 0:
        return value1
    if n == 1:
        return value2
    else:
        return sum_series(n - 2, value1, value2) + sum_series(n - 1, value1, value2)



def lucas2(n):
    """return the nth number of the lucas numbers using the function sum_series"""
    return sum_series(n, 2, 1)

def fibonacci2(n):
    """return the nth number of the fibonacci sequence using the function sum_series"""
    return sum_series(n, 0, 1)

if __name__ == "__main__":
    # run some tests

    assert fibonacci(-1) is None
    assert fibonacci(-23) is None

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(-1) is None
    assert lucas(-23) is None

    # do these with a loop:
    tests = [(0, 2),
             (1, 1),
             (2, 3),
             (3, 4),
             (4, 7),
             (5, 11),
             (6, 18),
             (7, 29),
             ]
    for input, output in tests:
        assert lucas(input) == output

    # test if sum_series matched Fibonacci
    for n in range(0, 10):
        assert sum_series(n) == fibonacci(n)

    # test if sum_series matched lucas
    for n in range(0, 10):
        assert sum_series(n, 2, 1) == lucas(n)

    # test if lucas1 matched lucas
    for n in range(0, 10):
        assert lucas2(n) == lucas(n)

    # test if fibonacci2 matched fibonacci
    for n in range(0, 10):
        assert fibonacci2(n) == fibonacci(n)

    print("tests passed")
