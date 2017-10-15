#!/usr/bin/env python

"""
Print a grid
"""

def print_grid():
	print('this will be a grid')

print_grid()


def plus_line(y, x):
	print('+' + y * ' - ' + ' + ' + (' - ' * y + '+') * x)

def line_line(y, x):
	print ('|' + y * '   ' + ' | ' + ('   ' * y + '|') * x)


def extend(y, x):
	"""
	this extends the square vertically, x definitions 
	"""
	for i in range(x):
		line_line(y,x)
	plus_line(y, x)

def print_grid_final(y,x):
	plus_line(y, x)
	for i in range(x):
		extend(y,x)
	

def print_grid_true(x):
	plus_line()
	for i in range(4):
		line_line()
	plus_line()
	for i in range(4):
		line_line()
	plus_line

print_grid_final(2,5)

