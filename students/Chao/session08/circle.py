#!/usr/bin/env python

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

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    @classmethod
    def from_diameter(cls, val):
        """ An Alternate Constructor from diameter """
        self = cls(val / 2)
        return self

    def __add__(self, other):
        """ Overloading add method, add radius from input instances and return a new Circle instance """
        return Circle(self.radius + other.radius)

    # More operator overloading
    def __gt__(self, other):
        return self.radius > other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __ne__(self, other):
        return self.radius != other.radius

class Sphere(Circle):

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    @property
    def area(self):
        return 4 * pi * self.radius**2

    @property
    def volume(self):
        return (4/3) * pi * self.radius**3