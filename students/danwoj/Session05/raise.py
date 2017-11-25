'''
Raising exceptions
'''

def fun(x):
	if x < 0:
		raise ValueError('You must use a positive number.')
	else:
		try:
			45 / x
		except ZeroDivisionError as err:
			print('Do something')
			print(err.args)
			err.args = (err.args[0] + '--a custom message')
			raise
		return 'Success'

for a in [3, 6, -2, 4, 0, 34]:
	try:
		print(fun(a))
	except ValueError:
		pass