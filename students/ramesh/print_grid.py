#!/usr/bin/env python

"""
print a grid

"""
def plus_line(x):
	print ('+' + x * ' - ' + '+' + x * ' - ' + '+')

def line_line(x):
	print ('|' + x * '   ' + '|' + x * '   ' + '|')

#print ('+' + 4 * ' - ' + '+' + 4 * ' - ' + '+')
def print_grid(x):
	plus_line(x)
	for i in range(x):
		line_line(x)
	plus_line(x)
	for i in range(x):
		line_line(x)
	plus_line(x)

print_grid(10)
print_grid(14)