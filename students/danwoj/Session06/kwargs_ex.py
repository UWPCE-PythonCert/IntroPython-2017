#!/usr/bin/env python3.6

'''
This is kwargs
'''
def fun(fore_color='blue', 
		back_color='red',
		link_color='yellow',
		visited_color='green',
		):
#	print('kwargs are: ', kwargs)
	return (fore_color, back_color, link_color, visited_color)

def fun2(*args, **kwargs):
	return (args, kwargs)

def print_fun():
	print('Hello World!')