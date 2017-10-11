#!/usr/bin/python

def fibonacci(n):
    """ Returns the nth value of the fibonacci sequence
    """
    return sum_series(n)


def lucas(n):
    """ Returns the nth value of the lucas numbers series
    """
    return sum_series(n, first_element=2, second_element=1)


def sum_series(n, first_element=0, second_element=1):
    """ Generates the appropriate series and returns the nth value of the series
    """
    if n == 1:
        return first_element
    else:
        next_element = first_element + second_element
        return sum_series(n-1, second_element, next_element)


if __name__ == "__main__":
    assert fibonacci(1) == 0    # fibonacci(1) == 0
    assert fibonacci(2) == 1    # fibonacci(2) == 1
    assert fibonacci(3) == 1    # fibonacci(3) == 1
    assert fibonacci(5) == 3    # fibonacci(5) == 3
    assert fibonacci(10) == 34  # fibonacci(10) == 34

    assert lucas(1) == 2        # lucas(1) == 2
    assert lucas(2) == 1        # lucas(2) == 1
    assert lucas(3) == 3        # lucas(3) == 3
    assert lucas(5) == 7        # lucas(5) == 7
    assert lucas(10) == 76      # lucas(10) == 76

    print("All tests passed.")
