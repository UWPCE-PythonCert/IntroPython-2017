#!/usr/bin/env python3

"""
slicing lab

"""

my_string = "Expecto Patronum"

def switch(seq):
    """with the first and last items exchanged"""
    return seq[-1:] + seq[1:-1] + seq[:1]
print(switch('Ollivander'))


def remove(seq):
    """With every other item removed"""
    return seq[::2]
print(remove("Expecto Patronum"))
print(remove(my_string))
