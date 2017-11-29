#! /usr/bin/env python
from decimal import Decimal


def string_format(tup):
    file = "file_{0:0>3}".format(tup[0])
    deci = "%.2f" % tup[1]
    sci = '{:.2e}'.format(tup[2])
    sci2 = '%.2e' % Decimal(tup[3])
    result = file + ":" + " " + str(deci) + ',' + " "+sci + ',' + " "+ sci2
    return result




print(string_format(( 2, 123.4567, 10000, 12345.67)))


def formatter(tup):
    size = len(tup)
    fs = "The {} numbers are: "
    fs += ", ".join(["{}"]*size)

    return fs.format(len(tup),*tup)

print(formatter((11,2,3,4,5)))
