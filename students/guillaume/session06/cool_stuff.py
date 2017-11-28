#!/usr/bin/env python3
from random import choice
from os import system, path
from string import ascii_lowercase


def return_random_keys(dict):
    return choice(list(dict.keys()))


if __name__ == '__main__':

    dict_a = dict()
    for cha in ascii_lowercase:
        dict_a[cha] = ord(cha)
    print(dict_a)
    key = return_random_keys(dict_a)
    print(key)
    print(dict_a[key])
    system('chmod +x {}'.format(path.basename(__file__)))
