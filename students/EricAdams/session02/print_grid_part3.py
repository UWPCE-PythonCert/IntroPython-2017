""" 
Print a grid
"""

def print_line_plus(n, columns):           # n = number or "-" in one cell
    print('+', end='')
    for i in range(columns):               # columns = number of columns                                         
        print('- ' * n, '+', end='')
                                        
def print_line_pipe(n, columns):           # n = number of ' ' in one cell
    print('|', end='')
    for i in range(columns):               # columns = number of columns
        print('  ' * (n), '|', end='')

def print_plus_n_pipe(n, rows):
    print_line_plus(n, rows)
    for i in range(n):                     # n = how many rows of '|' in a cell
        print()
        print_line_pipe(n, rows)
    print()

def print_grid(cell_size,rows):
    for i in range(rows):                   # rows = how many rows
        print_plus_n_pipe(cell_size, rows)
    print_line_plus(cell_size, rows)

print_grid(4, 2)
print() 
print_grid(12, 3)   

