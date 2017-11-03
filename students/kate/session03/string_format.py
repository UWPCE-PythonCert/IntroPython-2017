#!/usr/bin/env python

"""
String formatting lab:
This version using the format() method
"""
#using format method
print("file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()

#using iteration method
change = (2, 123.4567, 10000, 12345.67)
print("file_%03i : %10.2f, %.2e, %.3g" % change)
print()

change_a = (2, 123.4567, 10000, 12345.67)
print("file_%05i : %10.2f, %.5e, %.5g" % change_a)
print()
# i --> pad
# f -->
# e -->
# g -->
