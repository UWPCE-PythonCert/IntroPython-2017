#!/usr/bin/env python
# Description: Slicing lab in class exercise
# Comments: Execute in Python3.6
# Last modified on 10/22/2017 by davidkan@

def formatter(in_tuple):
    # do_something_here_to_make_a_format_string
    # 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    form_string = "file_{:0>3d}:   {:.2f}, {:.2e}, {:.3g}"

    return form_string.format(*in_tuple)


if __name__ == '__main__':

    result = formatter(( 2, 123.4567, 10000, 12345.67))
    print(result)
