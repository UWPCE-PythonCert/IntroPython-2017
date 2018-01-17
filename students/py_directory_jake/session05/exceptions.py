"""
raise exceptions
"""

def fun(x):
	if x < 0:
		raise ValueError("You must have a positive number.")
	else:
		try:
			45/x
		except ZeroDivisionError as err:
			print("doing something")
			print(err.args)
			err.args = (err.args[0] + "--A Custom Message",)
			# print(dir(err))
			raise
		return 'Success'

for a in [3, 6, -2, 5]:
	try:
		print(fun(a))
	except ValueError:
		pass
