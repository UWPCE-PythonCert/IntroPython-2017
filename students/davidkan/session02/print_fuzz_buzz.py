#!/usr/bin/env python
# Description: Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.
# Comment: Execute in Python3.6
# Last modified: 10/10/2017 by davidkan@


def fuzz_buzz(n):

    for num in range(1, (n + 1)):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


if __name__ == "__main__":

    fuzz_buzz(100)
