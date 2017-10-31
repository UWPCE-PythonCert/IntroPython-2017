def print_grid(num):
	plus = '+'
	minus = '-'
	space = ' '
	pipe = '|'
	print(plus, end=' ')
	for i in range(num//2):
		print(minus, end=' ')
	print(plus, end=' ')
	for i in range(num//2):
		print(minus, end=' ')
	print(plus)
	for i in range(num//2):
		print(pipe, end='')
		for i in range(num):
			print(space, end='')
		print(pipe, end='')
		for i in range(num):
			print(space, end='')
		print(pipe)
	print(plus, end=' ')
	for i in range(num//2):
		print(minus, end=' ')
	print(plus, end=' ')
	for i in range(num//2):
		print(minus, end=' ')
	print(plus)
	for i in range(num//2):
		print(pipe, end='')
		for i in range(num):
			print(space, end='')
		print(pipe, end='')
		for i in range(num):
			print(space, end='')
		print(pipe)
	print(plus, end=' ')
	for i in range(num//2):
		print(minus, end=' ')
	print(plus, end=' ')
	for i in range(num//2):
		print(minus, end=' ')
	print(plus)

num = int(input('Enter the size of the grid: '))
print_grid(num)