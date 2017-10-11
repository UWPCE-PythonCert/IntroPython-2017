#!/usr/bin/env python

# A fixed size grid
def print_grid():
    
    for i in range(11):
        if i%5==0:
            print("+ - - - - + - - - - +")
        else:
            print("|         |         |")

# 2x2 grid with a size variable
def print_grid2(n):
    for i in range(2):
        print('+' + n*' -' + ' +' + n* ' -' + ' +')
        for i in range(n):
            print('|' + n*'  ' + ' |' + n* '  ' + ' |')
    print('+' + n*' -' + ' +' + n* ' -' + ' +')

# 2 size variables now
def print_grid3(n, m):
    row = (('+ ' + m*'- ')*n + '+' + '\n')
    column = ((('| ' + m*'  ')*n + '|' + '\n')*m)
    block = row+column
    print(block*n + row)

# Some tests
if __name__ == "__main__":
    print_grid()
    print_grid2(6)
    print_grid3(3, 5)
