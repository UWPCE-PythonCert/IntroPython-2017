#!/usr/bin/env python3
# 2, 123.4567, 10000, 12345.67)

#and produce:

#'file_002 :   123.46, 1.00e+04, 1.23e+04'

print("file{:=03}".format(2))
file002
print("{:03.2f}".format(123.4567))
123.46

print("{:e}".format(10000))
1.000000e+04
print("{:03.2e}".format(10000))
1.00e+04

print("{:03.2e}".format(12345.67))
1.23e+04

t = (1,2,3)
"the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
'the 3 numbers are: 1, 2, 3'

def formatter(t):
    num = len(t)
    fs = "The {} number are: "
    fs += ",".join(["{}"]*num)
    print(fs.format(num, *t))