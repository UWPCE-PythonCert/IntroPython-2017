"""
Kathryn Egan

"""


def pad(integer, length):
    """ Pads given integer as string with 0s up to given length.
    Args:
        integer (int) : integer to pad
        length (int) : length of final integer string
    Returns:
        str : integer as string padded with leading 0s
    """
    integer = str(integer)
    while len(integer) < length:
        integer = '0' + integer
    return integer


def format_tuple(tup):
    """ Formats given tuple as string for easy print-out.
    Args:
        tup (tuple) : tuple to format
    Returns:
        str : tuple as string
    """
    result = 'file_{} :   {:.2f}, {:.2e}, {:.2e}'.format(
        pad(tup[0], 3), tup[1], tup[2], tup[3])
    return result


def dynamic_build(tup):
    """ Returns a string stating the contents
    of the given tuple.
    Args:
        tup (tuple) : tuple to print statement about
    Returns:
        str : statement regarding contents of tuple
    """
    if not tup:
        return 'no numbers'
    output = 'the {:d} numbers are: ' + ', '.join(['{:d}'] * len(tup))
    return output.format(len(tup), *tup)


tuple1 = (2, 123.4567, 10000, 12345.67)
tuple2 = (999, 3, 100000, 1030405050)
print(format_tuple(tuple1))
print(format_tuple(tuple2))

assert format_tuple(tuple1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert format_tuple(tuple2) == 'file_999 :   3.00, 1.00e+05, 1.03e+09'

tuple3 = (1, 2, 3)
tuple4 = (1, 2, 3, 4, 7, 2, 6, 4, 4)
tuple5 = tuple([])

print(dynamic_build(tuple3))
print(dynamic_build(tuple4))
print(dynamic_build(tuple5))

assert dynamic_build(tuple3) == 'the 3 numbers are: 1, 2, 3'
assert dynamic_build(tuple4) == 'the 9 numbers are: 1, 2, 3, 4, 7, 2, 6, 4, 4'
assert dynamic_build(tuple5) == 'no numbers'
