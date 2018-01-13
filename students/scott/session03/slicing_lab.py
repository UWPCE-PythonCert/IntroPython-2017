#!/usr/bin/env python


'''with the first and last items exchanged'''


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


'''with every other item removed'''


def rem(seq):
    return seq[::2]


'''with the first and last 4 items removed, and every other item in between'''


def rem_diff(seq):
    return seq[4:-4:2]


'''with the elements reversed (just with slicing)'''


def reversed(seq):
    return seq[::-1]


'''with the middle third, last third, the first third in the new order'''


def thirds(seq):
    i = len(seq) // 3
    return seq[i:-1] + seq[-1:] + seq[:i]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
