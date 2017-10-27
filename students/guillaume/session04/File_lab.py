#!/usr/bin/env python3
from os import listdir
from pathlib import Path


def test_os():
    ''' '''
    abs_path = Path('./').absolute()
    list_files = listdir()

    for f in list_files:
        print(abs_path / f)


def copy_file(source, dest):
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        outfile.write(infile.read())


if __name__ == '__main__':
    copy_file('./IMG_0623.JPG', './IMG_0624.JPG')
    test_os()
