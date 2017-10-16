""" 
Print a grid
"""

def print_line_plus(n):
    print('+', end='')
    for i in range(2):                 # n = size of one cell
        print('- ' * n, '+', end='')   # 4 cells in grid
                                        
def print_line_pipe(n):
    print('|', end='')
    for i in range(2):
        print(' ' * (n * 2), '|', end='')

def print_plus_n_pipe(n):
    print_line_plus(n)
    for increment in range(n):
        print()
        print_line_pipe(n)
    print()

def print_grid(n):
    for inc in range(2):
        print_plus_n_pipe(n)
    print_line_plus(n)

print_grid(12)    

