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
        'row', help='number of rows to print between 1 and 10',
        type=int, choices=range(1, 11))
    parser.add_argument(
        'column', help='number of columns to print between 1 and 10',
        type=int, choices=range(1, 11))
    args = parser.parse_args()
    # print row by column grid
    for i in range(args.row):
        print_horizontal(args.column)
        for i in range(4):
            print_vertical(args.column)
    print_horizontal(args.column)


def print_horizontal(column):
    """ Prints a horizontal component of grid."""
    string = '*'
    for i in range(column):
        for i in range(4):
            string += ' -'
        string += ' *'
    print(string)


def print_vertical(column):
    """ Prints a vertical component of grid."""
    string = '|'
    for i in range(column):
        for i in range(9):
            string += ' '
        string += '|'
    print(string)


if __name__ == '__main__':
    main()
