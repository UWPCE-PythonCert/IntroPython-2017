def fibonacci(n):
	"""This is my Fibonacci Series function"""
	fib = [0, 1]
	if n == 0:
		f_result = fib[0]
	elif n == 1:
		f_result = fib[1]
	else:
		for i in range (1, n):
			fib.append(fib[i-1] + fib[i-2])
			f_result = fib[i]
	print('Fibonacci #:', f_result)

def lucas(n):
	"""This is my Lucas Series function"""
	luc = [2, 1]
	if n == 0:
		l_result = luc[0]
	elif n == 1:
		l_result = luc[1]
	else:
		for i in range (1, n):
			luc.append(luc[i-1] + luc[i-2])
			l_result = luc[i]
	print('Lucas #:', l_result)

def sum_series(n, o, p):
	"""This is my Sum Series function"""
	ss = []
	ss.append(o)
	ss.append(p)
	if n == 0:
		result = ss[0]
	elif n == 1:
		result = ss[1]
	else:
		for i in range (1, n):
			ss.append(ss[i-1] + ss[i-2])
			result = ss[i]
	print('Sum Series #:', result)

nth = int(input('Enter the place number in the series: '))
place_one = int(input('Enter the value of the first place for Sum Series (default is 0): ') or 0)
place_two = int(input('Enter the value of the first place for Sum Series (default is 1): ') or 1)
if nth < 0:
	print('Invalid place number value')
else:
	fibonacci(nth)
	lucas(nth)
	sum_series(nth, place_one, place_two)

print('')

"""This test validates whether the Sum Series matches the Fibonacci Series"""
print('Fibonacci Test:')
for i in range(0, 10):
    assert sum_series(i, 0, 1) == fibonacci(i)


print('')

"""This test validates whether the Sum Series matches the Lucas Series"""
print('Lucas Test:')
for i in range(0, 10):
    assert sum_series(i, 2, 1) == lucas(i)

print('')
print('Testing complete')
