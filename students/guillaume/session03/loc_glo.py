#!/usr/bin/env python3


def test_loc():
    boolean = True
    return locals()


def test_loc_2():
    for i in range(4):
        print(i)
    return locals()


if __name__ == '__main__':
    print(test_loc())
    print(test_loc_2())
    globals()
