#! /usr/bin/env python
"""
print a grid
"""

def print_grid(num):
    #this is a function to make a grid, it works okay
    vert = "|"
    horiz = "-"
    plus = "+"
    blank = " "
    picture_a = (plus + (horiz * num) + plus + (horiz * num) + plus)
    picture_b = (vert + (blank * num) + plus + (blank * num) + vert + "\n")
    print(picture_a)
    print(picture_b * num)
    print(picture_a)
    print(picture_b * num)
    print(picture_a)
    return(picture_a, picture_b)


def print_grid2(num):
    #this is a function to make a grid, it works better than original print_grid
    line1 = "+----+----+"
    line2 = "|    +    |"
    grid = line1 + ("\n" + (line2  + "\n") * num) + line1 + ("\n" + (line2  + "\n") * num) + line1
    print(grid)
    return(grid)

def print_grid3(numx, numy)

print_grid2(5)
print_grid(10)
print_grid(20)
