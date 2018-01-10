#! /usr/bin/env python
# circle.py
# A Circle can be defined by either specifying the radius or the diameter,
# and the user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare to see if there are equal
# (follows from above) be able to put them in a list and sort them

import math


class Circle():
    def __init__(self, radius):
        self.radius = radius
    # _diameter = 0
    # _area = 0

    @property
    def diameter(self):
        self._diameter = 2 * self.radius
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self.radius = self._diameter / 2

    @property
    def area(self):
        self._area = math.pi * self.radius**2
        return self._area

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return 'Circle with radius:{}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        result = Circle(self.radius + other.radius)
        return result

    def __mul__(self, other):
        result = Circle(self.radius * other)
        return result

    def __rmul__(self, other):
        result = Circle(self.radius * other)
        return result

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius:{}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        self._volume = (4 / 3) * math.pi * self.radius**3
        return self._volume

    @property
    def area(self):
        self._area = 4 * math.pi * self.radius**2
        return self._area

