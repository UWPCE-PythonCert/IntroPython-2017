""" 
Print a grid
"""

def print_line_plus():
    print('+', end='')
    for i in range(2):
        print('- ' * 4, '+', end='')

def print_line_pipe():
    print('|', end='')
    for i in range(2):
        print(' ' * 8, '|', end='')

def print_plus_5_pipe():
    print_line_plus()
    for n in range(5):
        print()
        print_line_pipe()
    print()

def print_grid():
    for n in range(2):
        print_plus_5_pipe()
    print_line_plus()

print_grid()    

