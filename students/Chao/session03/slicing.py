#!/usr/bin/env python

def exchange_first_last(seq):
    """the first and last items exchanged"""
    return(seq[-1:] + seq[1:-1] + seq[:1])

def remove_every_other(seq):
    """every other item removed"""
    return(seq[::2])

def remove_more(seq):
    """the first and last 4 items removed, and every other item in between"""
    return(seq[4:-4:2])

def reverse(seq):
    """the elements reversed"""
    return(seq[::-1])

def first_third_last(seq):
    """the middle third, then last third, then the first third in the new order"""
    return(seq[(len(seq)//3):] + seq[:(len(seq)//3)])

if __name__ == '__main__':
    """some tests"""

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_more(a_string) == " sas"
    assert remove_more(a_tuple) == ()

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert first_third_last(a_string) == "is a stringthis "
    assert first_third_last(a_tuple) == (13, 12, 5, 32, 2, 54)

    print('passed!')