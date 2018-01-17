#circles.py
from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)

    @property
    def diameter(self):  # Getter has to return a variable
        return 2 * self.radius

    @diameter.setter    # Setter is mutable based on new data
    def diameter(self, d):
        self.radius = d / 2

    @property
    def area(self):
        return(pi * self.radius**2)

    @property
    def circumference(self):
        return(2 * pi * self.radius)

    @classmethod
    def from_diameter(cls, diam):
        return cls(diam / 2)


class Sphere(Circle):

    def volume(self):
        return (4 / 3 * pi * self.radius ** 3)

    def area(self):
        return (4 * pi * self.radius ** 2)



c = Circle(3)
d = Circle.from_diameter(6)
s = Sphere(5)
r = Sphere.from_diameter(6)
c.diameter = 17
print(c.radius)
print(c.diameter)
print(c.area)
print()
print(d.radius)
print(s.circumference)
print(s.area())
print("{:.2f}".format(r.area()))
