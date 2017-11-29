"""
Kathryn Egan
"""
from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @radius.setter
    def radius(self, value):
        self._radius = value

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    def __str__(self):
        return 'Circle, r={}'.format(self._radius)

    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __add__(self, other):
        try:
            return Circle(self.radius + other.radius)
        except AttributeError:
            return Circle(self.radius + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            return Circle(self.radius - other.radius)
        except AttributeError:
            return Circle(self.radius - other)

    def __rsub__(self, other):
        try:
            return Circle(other.radius - self.radius)
        except AttributeError:
            return Circle(other - self.radius)

    def __mul__(self, other):
        try:
            return Circle(self.radius * other.radius)
        except AttributeError:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            return Circle(self.radius / other.radius)
        except AttributeError:
            return Circle(self.radius / other)

    def __rtruediv__(self, other):
        try:
            return Circle(other.radius / self.radius)
        except AttributeError:
            return Circle(other / self.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius
