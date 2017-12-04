'''
Circle class, exercise
'''

from math import pi

class Circle:
    def __init__ (self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return pi * self.radius**2

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with a radius of {}".format(self.radius)

    def create__from_diameter(self, dia):
        self.radius = dia/2 * pi

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__ (self, other):
        return Circle(self.radius * other)

    def __gt__ (self, other):
        return self.radius > other.radius

    def __lt__ (self, other):
        return self.radius < other.radius

    def __eq__ (self, other):
        return self.radius == other.radius