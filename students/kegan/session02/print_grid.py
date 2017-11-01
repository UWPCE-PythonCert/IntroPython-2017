"""
Kathryn Egan

Prints a row x column grid consisting
of this square:
* - - - - *
|         |
|         |
|         |
|         |
* - - - - *
"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'rows', help='number of rows to print between 1 and 10',
        type=int, choices=range(1, 11))
    parser.add_argument(
        'columns', help='number of columns to print between 1 and 10',
        type=int, choices=range(1, 11))
    args = parser.parse_args()
    grid = build_grid(args.rows, args.columns)
    print(grid)


def build_grid(rows, columns):
    """ Builds row x column grid.
    Args:
        rows (int) : number of rows
        columns (int) : number of columns
    Returns:
        str : row x column grid
    """
    grid = []
    for __ in range(rows):
        grid.append(print_horizontal(columns))
        for __ in range(4):
            grid.append(print_vertical(columns))
    grid.append(print_horizontal(columns))
    grid = '\n'.join(grid)
    return grid


def print_horizontal(columns):
    """ Returns a horizontal component of grid.
    Args:
        columns (int) : number of columns
    Returns;
        str : horizontal component of grid
    """
    string = '*'
    for __ in range(columns):
        for __ in range(4):
            string += ' -'
        string += ' *'
    return string


def print_vertical(columns):
    """ Returns a vertical component of grid.
    Args:
        columns (int) : number of columns
    Returns;
        str : vertical component of grid
    """
    string = '|'
    for __ in range(columns):
        for __ in range(9):
            string += ' '
        string += '|'
    return string


if __name__ == '__main__':
    main()
