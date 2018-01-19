# Sum of the integers:
# keep adding the next integer
# 0 + 1 + 2 + 3 + 4 + 5 + …
# 0, 1, 3, 6, 10, 15 …..

def intsum():
    total = 0
    for i in range(100):
        if i < 1:
            yield 0
        else:
            total = total + i
            yield total

# Doubler:
# Each value is double the previous value:

# 1, 2, 4, 8, 16, 32,

def doubler():
    for i in range(1,100):
        if i == 1:
            yield 1
        yield 2**i

# Fibonacci sequence:
# The fibonacci sequence as a generator:

# f(n) = f(n-1) + f(n-2)

# 1, 1, 2, 3, 5, 8, 13, 21, 34…

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def fib():
    for i in range(1,500):
        yield recur_fibo(i)
    

# Prime numbers:
# Generate the prime numbers (numbers only divisible by them self and 1):

# 2, 3, 5, 7, 11, 13, 17, 19, 23…

def prime():
    for num in range(2,500):
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            yield num


# Others to try:
# Try x^2, x^3, counting by threes, x^e, counting by minus seven, …