"""
Kathryn Egan
"""


def intsum():
    index = 1
    curr = 0
    while True:
        yield curr
        curr += index
        index += 1


def doubler():
    value = 1
    while True:
        yield value
        value *= 2


def fib():
    prev = 0
    curr = 1
    while True:
        yield curr
        temp = curr
        curr += prev
        prev = temp


def prime():
    curr = 1
    while True:
        # advance past last prime returned
        curr += 1
        while True:
            temp = 2
            prime = True
            # test divisors up to 1/2 current number
            while temp <= curr / 2:
                # current num is divisible - not prime
                if curr % temp == 0:
                    prime = False
                    break
                # not divisible - try another divisor
                temp += 1
            # end of divisors or non-prime reached
            if prime:
                yield curr
            # check next number
            curr += 1
