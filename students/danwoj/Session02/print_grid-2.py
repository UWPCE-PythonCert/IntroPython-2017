def print_grid(col,row,size):
	dim=size-1//2
	print(dim)
	for i in range(row):
		#Draw the top row
		print('+ ' + (('- ' * dim) + '+ ') * col)
		for j in range(size):
			#Draw middle part of boxes
			print('| ' + ((' ' * 2 * dim) + '| ') * col)
	#Draw bottom line
	print('+ ' + (('- ' * dim) + '+ ') * col)

col = int(input('Enter the number of columns: '))
row = int(input('Enter the number of rows: '))
size = int(input('Enter the size of each box: '))
print_grid(col, row, size)