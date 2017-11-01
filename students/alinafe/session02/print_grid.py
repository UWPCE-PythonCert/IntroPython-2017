#!/usr/bin/env python3
"""
Grid Printer Exercise:
"""

def print_grid():

    print("+--------+-------+")
    for i in range(1,5):
        print ('|       ', end=' ')
        print ('|       |')
    print("+--------+-------+")
    for i in range(1,5):
        print ('|       ', end=' ')
        print ('|       |')
    print("+--------+-------+")
    print(locals())

print_grid()




