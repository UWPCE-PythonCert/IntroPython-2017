#!/usr/bin/env python

"""
Print a grid
"""

def print_grid():
    
    for i in range(11):
        if i%5==0:
            print("+ - - - - + - - - - +")
        else:
            print("|         |         |")


def print_grid2(n):

    print ('+', n*' - ', '+', n* ' - ', '+')
    for i in range(n):
        if n//2 == 0:
            print ('+', n*' - ', '+', n* ' - ', '+')
        else:
            print ('|', n*'   ', '|', n*'   ', '|')
    print ('+', n*' - ', '+', n* ' - ', '+')

print_grid2(10)