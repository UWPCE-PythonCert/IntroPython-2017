#!/usr/bin/python

def print_line(intersection_char, fill_char, ticks, count=2):
    fill = "{} ".format(fill_char)

    for i in range(count):
        print(intersection_char, end=' ')
        print(fill * ticks, end='')

    print(intersection_char)


def print_grid(n):
    limit = n + 1
    ticks = n//2

    if n % 2 != 0:
        limit = n

    for i in range(limit):
        if i % ticks == 0:
            print_line('+', '-', ticks)
        else:
            print_line('|', ' ', ticks)


def print_grid2(grid_count, size):
    limit = (grid_count * size) + grid_count + 1

    for i in range(limit):
        if i % (size + 1) == 0:
            print_line('+', '-', size, count=grid_count)
        else:
            print_line('|', ' ', size, count=grid_count)



if __name__ == "__main__":
    print("print_grid(10)")
    print_grid(10)

    print("print_grid(11)")
    print_grid(11)

    print("print_grid(15)")
    print_grid(15)

    print("print_grid2(3,4)")
    print_grid2(3,4)

    print("print_grid2(5,3)")
    print_grid2(5,3)
