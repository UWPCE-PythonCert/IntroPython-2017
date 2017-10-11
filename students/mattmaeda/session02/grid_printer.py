#!/usr/bin/python

def print_line(intersection_char, fill_char):
    fill = "{} ".format(fill_char)
    print(intersection_char, end=' ')
    print(fill * 4, end='')
    print(intersection_char, end=' ')
    print(fill * 4, end='')
    print(intersection_char)


for i in range(11):
    if i % 5 == 0:
        print_line('+', '-')
    else:
        print_line('|', ' ')
