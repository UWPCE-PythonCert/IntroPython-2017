#!/usr/bin/env python

def fibu():
    for i in range(100):
        x = i+1
        if x%15 == 0:
            print('FizzBuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x%5 == 0:
            print('Buzz')
        else:
            print(x)

# Test time
if __name__ == "__main__":
    fibu()