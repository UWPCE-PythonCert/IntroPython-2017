#! /usr/bin/env python

"""
Print a grid
"""

plus = "+"
minus = "-"
pipe = "|"
space = " "

def grid():
    line1 = plus+(3*(space+minus+space))
    line2 = pipe+(3*(space+space+space))
    for i in range(3):
        print(line1*3 + plus)
        for i in range(3):
            print(line2*3 + pipe)
    print(line1*3 + plus)


def print_grid(n):
    line1 = plus+(n*(space+minus+space))
    line2 = pipe+(n*(space+space+space))
    for i in range(n):
        print(line1*n + plus)
        for i in range(n):
            print(line2*n + pipe)
    print(line1*n + plus)


def print_multi_grid(m,n):
    line1 = plus+(n*(space+minus+space))
    line2 = pipe+(n*(space+space+space))
    for i in range(m):
        print(line1*m + plus)
        for i in range(n):
            print(line2*m + pipe)
    print(line1*m + plus)



if __name__ == "__main__":
    grid()
    print_grid(4)
    print_multi_grid(5,3)
