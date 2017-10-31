def fibonacci(n):
	fib = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#	fib[0] = 0
#	fib[1] = 1
	for i in range(2, nth+1):
		fib[i]=fib[i-2]+fib[i-1]
	print('Fibonacci #:', fib[nth-1])

def lucas(n):
	luc = [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(2, nth+1):
		luc[i]=luc[i-2]+luc[i-1]
	print('Lucas #:', luc[nth-1])

nth = int(input('Enter the number # value in the series: '))
fibonacci(nth)
lucas(nth)