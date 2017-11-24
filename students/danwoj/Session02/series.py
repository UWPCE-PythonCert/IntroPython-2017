def fibonacci(n):
	fib = [0, 1]
	if n == 1:
		f_result = fib[0]
	elif n == 2:
		f_result = fib[1]
	else:
		for i in range (2, n):
			fib.append(fib[i-1] + fib[i-2])
			f_result = fib[i]
	print('Fibonacci #:', f_result)

def lucas(n):
	luc = [2, 1]
	if n == 1:
		l_result = luc[0]
	elif n == 2:
		l_result = luc[1]
	else:
		for i in range (2, n):
			luc.append(luc[i-1] + luc[i-2])
			l_result = luc[i]
	print('Lucas #:', l_result)

nth = int(input('Enter the place number in the series: '))
fibonacci(nth)
lucas(nth)