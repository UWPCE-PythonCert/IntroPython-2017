#!/usr/bin/env python

""" Write a format string that will take the tuple:
( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""


def format_tuple(seq):
    print('file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}'.format(
        seq[0], seq[1], seq[2], seq[3]))


format_tuple((2, 123.4567, 10000, 12345.67))


def formatter(in_tuple):
    """Dynamically Build up format string
    """
    form_string = ''
    for x in in_tuple:
        form_string = form_string + '{} '
    temp = form_string.split()
    s = ','
    form_string = s.join(temp)
    form_string = 'the ' + str(len(in_tuple)) + ' numbers are: ' + form_string
    return form_string.format(*in_tuple)


print(formatter((4, 6, 8,10,12)))
