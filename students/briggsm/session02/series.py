def fib(n):
    '''This is the fib series'''
    if n ==0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(10):
    print (fib(i))

if __name__ == '__main__':
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3