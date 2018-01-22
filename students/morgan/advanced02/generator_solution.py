import math

def int_sum():
    a = 0
    b = 0
    while True:
        yield b
        a += 1
        b = b + a

def doubler():
    a = 1
    while True:
        yield a
        a = a * 2

def fib():
    a = 1
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a+b

def prime():
    a = 2
    while True:
        check = True
        for x in range(2,int((math.sqrt(a)+1))):
            if (a%x)==0:
                check = False
                break
        # if check == 0:
        #     pass
        if check == True:
            yield a
        a += 1

def exponents(value =2,exponent = 2, step = 1):
    while True:
        yield value ** exponent
        value += step

