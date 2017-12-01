from math import pi
class Circle():
    """class that deals with circles"""
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius**2

    @property
    def circumference(self):
        return 2 * pi * self.radius

    def __str__(self):
        """string representation of a Circle"""
        return "This is a Circle with radius: {:.5f}".format(self.radius)

    def __repr__(self):
        """official representation of a Circle"""
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        """add two circles together, new circle is sum of the two radi"""
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        """multiply a circle by a scalar"""
        return Circle(self.radius * other)

    def __rmul__(self, other):
        """multiply a scalar by a circle"""
        return Circle.__mul__(self, other)

    def __gt__(self, other):
        """compare whether a circle is bigger than another circle"""
        return self.radius > other.radius

    def __lt__(self, other):
        """compare whether a circle is less than another circle"""
        return self.radius < other.radius

    def __eq__(self, other):
        """compare whether a circle is equal to another circle"""
        return self.radius == other.radius
