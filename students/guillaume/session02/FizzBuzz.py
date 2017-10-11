#!/usr/bin/env python3
def FizzBuzz(n=100):
    '''
    '''
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def FizzBuzz_2(n=100):
    '''
    '''
    for i in range(1, n + 1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if not output:
            output = i
        print(output)


if __name__ == '__main__':
    FizzBuzz()
    FizzBuzz_2()
