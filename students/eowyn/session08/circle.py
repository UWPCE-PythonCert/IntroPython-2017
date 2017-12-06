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

#  ---------------- NUMERIC OPERATORS --------------------------

    def __add__(self, other):
        # Add circles by adding their radii
        newrad = self.radius + other.radius
        return Circle(newrad)

    def __mul__(self, factor):
        newrad = self.radius * factor
        return Circle(newrad)

    def __rmul__(self, factor):
        # reflective multiply... repeats code??
        newrad = self.radius * factor
        return Circle(newrad)

    def __truediv__(self, factor):
        newrad = self.radius / factor
        return Circle(newrad)

    def __rtruediv__(self, factor):
        # reflective division... repeats code??
        newrad = factor / self.radius
        return Circle(newrad)

    def __floordiv__(self, factor):
        newrad = self.radius // factor
        return Circle(newrad)

    def __rfloordiv__(self, factor):
        # reflective division... repeats code??
        newrad = self.radius // factor
        return Circle(newrad)

    def __sub__(self, other):
        # Subtract circles by subtracting their radii
        # Do NOT allow negative radii
        newrad = self.radius - other.radius
        return abs(Circle(newrad))

    def __mod__(self, other):
        newrad = self.radius - other.radius*(self.radius//other.radius)
        return abs(Circle(newrad))

#  ---------------- COMPARE OPERATORS --------------------------

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

#  ---------------- AUGMENTED ASSIGNMENT OPERATORS --------------------

    def __iadd__(self, other):
        newrad = self.radius + other.radius
        return Circle(newrad)

    def __isub__(self, other):
        # Do NOT allow negative radii
        newrad = self.radius - other.radius
        return abs(Circle(newrad))

    def __imul__(self, factor):
        newrad = self.radius * factor
        return Circle(newrad)

    def __idiv__(self, factor):
        newrad = self.radius / factor
        return Circle(newrad)


#  ---------------- UNARY ARITHMETIC OPERATORS -----------------------

    def __abs__(self):
        if self.radius < 0:
            newrad = self.radius * -1
            return Circle(newrad)
        else:
            return self
