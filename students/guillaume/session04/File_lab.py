#!/usr/bin/env python3
from os import getcwd, listdir


def test_os():
    print(getcwd())
    print(listdir())


if __name__ == '__main__':
    test_os()