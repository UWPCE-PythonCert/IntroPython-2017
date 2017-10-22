#!/usr/bin/env python

def reformat(a, b, c, d):
    """ reform input strings in certain format """

    a = 'file_' + f'{a:03}' + ':'
    b = ' {:.2f}'.format(b)
    c = ' {:.2e}'.format(c)
    d = ' {:.2e}'.format(d)

    return a+b+c+d

def formatter(t):
    """ Creating string dynamically with different length """

    # Check the input length first
    l = len(t)

    # Building string
    tstring = '{:d}, ' * l

    if l <= 1:
        rstring = 'The number is: ' + tstring[:-2]
    else:
        rstring = 'The ' + str(l) + ' numbers are: ' + tstring[:-2]

    return rstring.format(*t)



if __name__ == '__main__':
    """ some tests """

    print(reformat(2, 123.4567, 10000, 12345.67))
    print(reformat(77, 3.14159, 7654321, 88888.88888))

    print(formatter((7, )))
    print(formatter((1, 2, 3)))
    print(formatter((8, 16, 32, 64, 128, 256)))
    