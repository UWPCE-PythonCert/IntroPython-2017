"""
Args and Kwargs Concepts
https://www.youtube.com/watch?v=762mFeD2SlU
"""

def normal(one, two):
	print(one)
	print(two)

normal('Argument One', 'Argument Two\n')

def arg_one(*args):
	for stuff in args:
		print(stuff)


my_list = ['Honda', 'BMW', 'Toyota', 'Ford', 'Chevy']

arg_one(*my_list)

arg_one('\nHonda', 'BMW', 'Toyota', 'Ford', 'Chevy\n')
#notice how you need to take your items out of a List object and just have them floating


def arg_three(one, two, *args):
	print(one)
	print(two)
	print(args)
	for stuff in args:
		print(stuff)

arg_three('Required 1', 'Required 2', *my_list)

#kwargs examples below

def kwarg_one(**kwargs):
	for key, value in kwargs.items():
		print(key)
		print(value)

d_example = {'\nKey1':'Value1', 'Key2':'Value2', 'Key3': 'Value3\n'}

kwarg_one(**d_example)

def kwarg_two(**kwargs):
	for key, value in kwargs.items():
		print(key)
		print(value)

kwarg_two(Keye1 = 'Value1e', Keye2 = 'Value2e', Keye3 = 'Value3e')





