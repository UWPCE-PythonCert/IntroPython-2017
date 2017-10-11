#! /usr/bin/env python

"""
Print a grid
"""

plus = "+"
minus = "-"
pipe = "|"
space = " "

def print_grid(n):
    line1 = plus+(n*(space+minus+space))
    line2 = pipe+(n*(space+space+space))
    for i in range(n):
        print(line1*n + plus)
        for i in range(n):
            print(line2*n + pipe)
    print(line1*n + plus)

print_grid(1)

def print_multi_grid(m,n):
    line1 = plus+(n*(space+minus+space))
    line2 = pipe+(n*(space+space+space))
    for i in range(m):
        print(line1*m + plus)
        for i in range(n):
            print(line2*m + pipe)
    print(line1*m + plus)


print_multi_grid(2,5)

