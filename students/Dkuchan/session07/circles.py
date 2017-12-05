#circles.py
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.diameter

    @property
    def diameter(self):  # Getter has to return a variable
        return (2 * self.radius)

    @property
    def area(self):
        return(2 * math.pi * self.radius)



c = Circle(3)
c.diameter = 3
print(c.radius)
print(c.diameter)
