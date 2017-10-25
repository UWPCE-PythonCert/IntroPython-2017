#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

'''
Fibonacci
'''


def fib(n):
    ''' Calculates the Fibonacci series from the n parameter. '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    print()

    # for i in range(1,n+1):
    #     fib(n) = fib(n-2) + fib(n-1)

    # print(fib(n))


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    print(fib(20))
