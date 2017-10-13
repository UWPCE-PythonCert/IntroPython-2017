# Grid printer exercise
# Python 3.6


def print_grid(number):
    """ Print a grid expanded by number provided """
    half = int(number / 2)

    print('+', '- ' * half, '+', '- ' * half, '+')
    for item in range(half):
        print('|', '  ' * half, '|', '  ' * half, '|')
    print('+', '- ' * half, '+', '- ' * half, '+')
    for item in range(half):
        print('|', '  ' * half, '|', '  ' * half, '|')
    print('+', '- ' * half, '+', '- ' * half, '+')


def print_grid2(cell_size, scale):
    """ Print a grid with specific cell count and expanded by scale """
    top = ''.join(['+', ' - ' * scale])
    sides = ''.join(['|', '   ' * scale])

    for count in range(cell_size):
        print(top * cell_size, '+')
        for size in range(scale):
            print(sides * cell_size, '|')
    print(top * cell_size, '+')
