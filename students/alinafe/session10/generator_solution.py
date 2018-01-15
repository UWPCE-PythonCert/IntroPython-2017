# import mem_profile
# import time
# import random


def intsum():
    """Sum numbers generator"""
    lnum, hinum = 0, 7

    for i in range(1, hinum):
        yield lnum
        print('increment by last value')
        lnum += i


n = intsum()

for i in n:
    print(i, end=' : ')


def intsum2():
    return intsum()


# Doubler

# print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))
# Sum of integers

# doubler = (x * 2 for x in [1,2,3,4,5])
# t1 = time.clock()
# print(list(intsum))
# t2 = time.clock()
# t1 = time.clock()
# print(intsum)
# t2 = time.clock()


# print('Memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
# print('Took {} seconds'.format(t2 -t1))

def doubler():
    """Doubler numbers generator"""
    # nums = [1,2,3,4,5]
    # for t in nums:
    # yield (t * 2)

    lnum, hinum = 1, 20
    for i in range(hinum):
        yield lnum
        lnum *= 2


d = doubler()

print(next(d))
print(next(d))
print(next(d))
print(next(d))

for tx in d:
    print(tx, end=' : ')


# Fibonacci sequence

def fib():
    """Fib numbers generator"""
    a, b, n = 1, 1, 30
    for s in range(n):
        yield a
        a, b = b, a + b

# Prime numbers

def nprme():
    for i in range(2,8):
        for j in range(i*2, 50, i):
            yield j
            i += 1

def prime():
    for x in range(2,50):
        if x not in nprme():
            yield x
