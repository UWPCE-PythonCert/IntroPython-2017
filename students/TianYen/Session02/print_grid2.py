def print_columns(gridsize, cellsize):
    for i in range(cellsize):
        for n in range(gridsize):
            print('|', '  ' * cellsize, end = '')
        print('|')

def print_row(gridsize, cellsize):
    for i in range(gridsize):
        print('+', '- ' * cellsize, end = '')
    print('+')

def print_grid2(gridsize, cellsize):
    for i in range(gridsize):
        print_row(gridsize, cellsize)
        print_columns(gridsize, cellsize)
    print_row(gridsize, cellsize)


print_grid2(5, 3)
