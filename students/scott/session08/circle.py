#!/usr/bin/env python3

"""
circle stuff
"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return pi * self.radius**2

    def __str__(self): #'string' method
        return  "Circle with radius: {}".format(self.radius)

    def __repr__(self): #'represent' method
        return "Circle({})".format(self.radius)


    def __add__(self, another):  #add two circles together by adding the radius of one to the radius of the other
        sum_radius = self.radius + another.radius
        return Circle(sum_radius)

    def __mul__(self, mult):
        new_radius = self.radius*mult
        return Circle(new_radius)

    def __eq__(self, another):
        if self.radius == another.radius:
            return True
        else:
            return False

    def __ge__(self, another):
        if self.radius >= another.radius:
            return True
        else:
            return False

    def __le__(self, another):
        if self.radius <= another.radius:
            return True
        else:
            return False

    def __lt__(self, another):
        if self.radius < another.radius:
            return True
        else:
            return False

    def __gt__(self, another):
        if self.radius > another.radius:
            return True
        else:
            return False


