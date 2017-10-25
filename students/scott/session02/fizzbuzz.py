#!/usr/bin/env python

for i in range (1,101):
    msg = ''
    if i%3 == 0:
        msg += "Fizz"
    if i%5 == 0:
        msg += "Buzz"
    if msg:
        print(msg)
    print(i)