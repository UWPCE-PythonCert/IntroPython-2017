#!/usr/bin/env python3

# ( 2, 123.4567, 10000, 12345.67)

# 'file_002 :   123.46, 1.00e+04, 1.23e+04'


def format_number(tup):
    return 'file_{:0>3d} :   {:.2f},  {:.2e}, {:.2e}'.format(*tup)


def arb_long(tup):
    form = ', '.join(['{:d}'] * len(tup))
    # form *= len(tup)
    return form.format(*tup)


if __name__ == '__main__':
    print(format_number((2, 123.4567, 10000, 12345.67)))
    print(arb_long((2, 123, 10000, 12345, 9)))
