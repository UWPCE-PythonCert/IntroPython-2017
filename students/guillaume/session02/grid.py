
def example_grid():

	for _ in range(2):
		print('+', 4 * '-', '+', 4 * '-', '+')

		for _ in range(4):
			print('|', 4 * ' ', '|', 4 * ' ', '|')

	print('+', 4 * '-', '+', 4 * '-', '+')



def print_grid(n): #size of the grid
	''' n is the length of the line minus the plus on the side '''
	if n < 3: n = 3
	if n % 2 == 0: n += 1
	
	line_a = gene_line('+', '-', n)
	line_b = gene_line('|', ' ', n)

	lines = [line_a] + [line_b for _ in range(n)] + [line_a] 
	lines[(n + 1) // 2 ] = line_a #middle line

	for line in lines: print(line)

def print_grid2(m, n): #(m number of row / columns, n cell size)

	line_a = gene_line2('+', '-', m, n)
	line_b = gene_line2('|', ' ', m, n)

	lines = [line_b for _ in range(m * n + m  + 1)]
	for i in range(0,len(lines), n + 1): lines[i] = line_a

	for line in lines: print(line)


def gene_line(char_a, char_b, n):
	
	line = char_a + ' ' + ((n - 1) // 2) * (char_b + ' ') 
	line = line + char_a + line[::-1]
	return line

def gene_line2(char_a, char_b, m, n):

	sub_line =  char_a + ' ' + n * (char_b + ' ')
	line = sub_line * m + char_a
	return line

if __name__ == '__main__':
	example_grid()
	print()
	print_grid(8)
	print()
	print_grid2(1,1)
	print()
	print_grid2(2,3)
	print()
	print_grid2(3,4)
	print()
	print_grid2(5,3)

	


