MAX_ITERATION=50

def intsum():
    last = 0
    for i in range(1, MAX_ITERATION):
        yield last
        last += i



def intsum2():
    return intsum()


def doubler():
    last = 1
    for i in range(MAX_ITERATION):
        yield last
        last *= 2


def fib():
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    for i in range(MAX_ITERATION):
        yield fibonacci(i)


def prime():
    def is_prime(n):
        """ Just doing a quick check if a number is prime
        """
        if n in [2, 3, 5, 7]:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        if n % 5 == 0:
            return False
        if n % 7 == 0:
            return False
        return True

    for i in range(2, MAX_ITERATION):
        if is_prime(i):
            yield i
