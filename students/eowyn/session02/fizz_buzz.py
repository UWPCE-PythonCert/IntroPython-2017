#!/usr/bin/env python
""" 
    Print number 1..100 unless number is divisible by 3
    then print Fizz, or if by 5, print Buzz, or if by 
    both 3 and 15, print FizzBuzz
    """
def fizz_buzz(n=100):
    for i in range(1,n+1):
        msg = "Fizz" if i%3==0 else ""
        msg += "Buzz" if i%5==0 else ""
        print(msg or i)

if __name__== "__main__":
    fizz_buzz(30)