#!/usr/bin/env python3


def fibonnaci(n):
    '''
    Generate the nth item of the Fibonnaci serie
    Fibonnaci serie has n1 = 0 and n2 = 1 with
    s(n) = s(n - 2) - s(n - 1)
    '''
    return sum_series(n)


def lucas(n):
    '''
    Return the nth item of the Lucas Serie
    Lucas serie has n1 = 2 and n2 = 1 with
    s(n) = s(n - 2) - s(n - 1)
    '''
    return sum_series(n, 2, 1)


def sum_series(n, n_1=0, n_2=1):
    '''
    Generate the nth value of a serie of the type s(n) = s(n - 2) + s(n - 1)
    with n1 and n2 known. By default n1 = 0 and n2 = 2, the first 2 values of
    the Fibonnaci serie
    '''
    if n == 1:
        n_elem = n_1
    elif n == 2:
        n_elem = n_2
    else:
        n_elem = sum_series(n - 2, n_1, n_2) + sum_series(n - 1, n_1, n_2)

    return n_elem


if __name__ == '__main__':
    n = 15
    function_list = [fibonnaci, lucas]
    m = len(function_list)
    list_n = [i for i in range(1, n + 1)]

    for j in range(m):
        print(repr(function_list[j].__name__))
        print(repr(function_list[j].__doc__))
        serie_lst = [function_list[j](i) for i in list_n]
        serie_str = ', '.join(map(str, serie_lst))
        print(serie_str)
        print()

    # Assert
    assert fibonnaci(3) != fibonnaci(2) - fibonnaci(1), 'this is wrong'
