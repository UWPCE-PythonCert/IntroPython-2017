# FizzBuzz exercise
# Python 3.6


def fizzbuzz():
    """
    From an inclusive range from 1 - 100, print whether the number is a
    multiple of 3, 5, or both and print the associated Fizz/Buzz words.
    """
    for cycle in range(1, 101):
        if cycle % 3 is 0 and cycle % 5 is 0:
            print('FizzBuzz')
        elif cycle % 3 is 0:
            print('Fizz')
        elif cycle % 5 is 0:
            print('Buzz')
        else:
            print(cycle)
