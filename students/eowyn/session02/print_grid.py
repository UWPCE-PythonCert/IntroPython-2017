#!/usr/bin/env python

''' Construct grid that is composed of ndim boxes in 
    either direction, and each box is composed of ndash 
    lines both horizontally and vertically '''

### First method uses global vars and functions for lines and verts
### then a caller function to print it all

# define global varaibles
plus = "+"
minus = "-"
space = " "
dash = '|'

def make_line(ndim,ndash):
    line = ''
    for n in range(ndim):
        line += plus + ndash*minus
    line += plus
    return line

def make_vert(ndim,ndash):
    vert = ''
    for n in range(ndim):
        vert += dash + ndash*space
    vert += dash
    return vert

def print_grid1(ndim,ndash):
    for i in range(ndim):
        print(make_line(ndim,ndash))
        for j in range(ndash):
            print(make_vert(ndim,ndash))
    print(make_line(ndim,ndash))

### Second method uses just one general construction function
### and a caller function to print it all

def make_row(ndim,ndash,char1,char2):
    row = ''
    for n in range(ndim):
        row += char1 + ndash*char2
    row += char1
    return row

def print_grid(ndim,ndash):
    for i in range(ndim):
        print(make_row(ndim,ndash,'+','-'))
        for j in range(ndash):
            print(make_row(ndim,ndash,'|',' '))
    print(make_row(ndim,ndash,'+','-'))

### Now try the simple case where ndim is always 2
### This is not producing the expected result for n = 11

def roundno(no):
    ''' round to nearest whole integer '''
    return int(no//1 + ((no%1)/0.5)//1)

def print_grid0(n):
    ## handle odd n by rounding to nearest int
    (ndim,ndash) = (2,roundno((n-1)/2))
    print_grid(ndim,ndash)


if __name__=="__main__":
    print_grid(3,4)
    print_grid(5,3)
    print_grid(2,1)
    print_grid(2,7)
    print_grid(2,4)
    print_grid0(3)
    print_grid0(15)
    print_grid0(11)
