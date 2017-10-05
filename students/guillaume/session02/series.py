
def fibonnaci(n):
	if n == 0: fib = 0
	elif n == 1: fib = 1
	else:
		fib = fibonnaci(n - 2) + fibonnaci(n - 1)

	return fib



if __name__ == '__main__':
	x = 10
	fib_lst = [ fibonnaci(n) for n in range(x) ]
	fib_str = ', '.join(map(str, fib_lst))
	print(fib_str)