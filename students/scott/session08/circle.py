#!/usr/bin/env python3

"""
circle stuff
"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self): #'string' method
        return  "Circle with radius: {}".format(self.radius)

    def __repr__(self): #'represent' method
        return "Circle({})".format(self.radius)


    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return pi * self.radius**2
