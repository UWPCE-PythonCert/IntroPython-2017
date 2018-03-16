#!/usr/bin/env python3
from os import listdir, rename, getcwd


def f(file, name, name_b):
    return '{}{}'.format(name, file[len(name_b):].replace('_', ':'))


if __name__ == "__main__":
    a = getcwd()
    b = listdir(a)
    d = 'card_data_'
    c = list(filter(lambda x: d in x, b))
    d = [f(file, d, d) for file in c]

    for file_old, file_new in zip(c, d):
        print('{} {}'.format(file_old, file_new))
        rename(file_old, file_new)

    print(listdir(a))
