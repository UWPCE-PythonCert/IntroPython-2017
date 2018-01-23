#!/usr/bin/env python3


def fib():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    g = fib()  # Create a generator of fibonnaic number 
    print([next(g) for _ in range(25)])
