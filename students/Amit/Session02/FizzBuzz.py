#! /usr/bin/env python

def FizzBuzz(n):
    for i in range(1, (n+1)):
        output=""
        if (i % 3) == 0:
            output += "Fizz"
        if (i % 5) == 0:
            output += "Buzz"
        if not output:
            output = i
        print(output)


if __name__ == "__main__":
    FizzBuzz(31)

