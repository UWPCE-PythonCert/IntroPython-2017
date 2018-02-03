"""
nifty Circle class
"""
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return pi*self.radius**2

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    @classmethod
    def create_from_diameter(cls, dia):
        return cls(dia/2)

#  ---------------- NUMERIC OPERATORS ----------------------------

#  ---------------- COMPARE OPERATORS ----------------------------

#  ---------------- AUGMENTED ASSIGNMENT OPERATORS ---------------


# ---------------- SPHERE CLASS ----------------------------------
class Sphere(Circle):
    pass
    # Area should be surface area
    # repr and str should be different
    # Volume should be defined
    # The rest of it should work the same
