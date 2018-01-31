
import math
import functools

@functools.total_ordering
class Circle(object):
    def __init__ (self, radius):
        self.radius = radius
        
    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)

    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2
    @property
    def area(self):
        return  (self.radius**2 * math.pi)

    def __repr__(self):
        return "Circle({})".format(self.radius)
    def __str__(self):
        return "Circle with radius {}".format(self.radius)

    def __add__(self, value):
            x = self.radius + value.radius
            return Circle(x)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __rmul__(self, value):
        return Circle(self.radius * value)


    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    @property
    def sort(self, things):
        return sorted(things, key = things.radius)


class Sphere(Circle):

    @property
    def volume(self):
        x = (4/3)*math.pi*(self.radius**3)
        return round(x, 2)


circles = [Circle(5), Circle(4), Circle(3), Circle(2), Circle(1)]