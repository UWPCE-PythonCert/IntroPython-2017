#!/usr/bin/env python

plus = '+'
dash = '-'
pipe = '|'


def print_grid2(row_col, cell_size):
    a = (((plus + (dash*cell_size))*row_col) + plus)
    
    for i in range(row_col):
        print(a)
        for i in range(cell_size):
            print(((pipe + (" "*cell_size))*row_col) + pipe)
    print(a)


print_grid2(3 , 2)