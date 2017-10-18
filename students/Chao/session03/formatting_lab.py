#!/usr/bin/env python

def reformat(a, b, c, d):
    a = 'file_' + f'{a:03}'
    b = '{:.2f}'.format(b)
    c = '{:.2e}'.format(c)
    d = '{:.2e}'.format(d)

    print(a, ': ', b, c, d)


if __name__ == '__main__':
    reformat(2, 123.4567, 10000, 12345.67)