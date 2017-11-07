#!/usr/bin/env python3


fb = [[str(i), 'Fizz', 'Buzz', 'FizzBuzz'][(i % 3 == 0) + 2 * (i % 5 == 0)] for i in range(1, 101)]

print('\n'.join(fb))
