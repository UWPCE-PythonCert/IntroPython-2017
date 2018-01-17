import math

class circle():
	# --------------------------------------------------------------
	# Initializer
	# --------------------------------------------------------------
    def __init__(self, radius = 0):
        self.radius = radius
        

    # --------------------------------------------------------------
    # Getters
    # --------------------------------------------------------------
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def radius(self):
        return self._radius

    @property
    def circumference(self):
        return self.radius *2 * math.pi

    @property 
    def area(self):
        return math.pow(self.radius,2)*math.pi

    # --------------------------------------------------------------
	# Setters
	# --------------------------------------------------------------
    
    @radius.setter
    def radius(self, value = None):
        self._radius = value

    @diameter.setter
    def diameter(self, value = None):
        self._radius = value / 2

    # --------------------------------------------------------------
    # From Diameter
    # --------------------------------------------------------------
    
    def from_diameter(value):
        return circle(value / 2)
    # --------------------------------------------------------------
    # Formatting with Dunder Methods
    # --------------------------------------------------------------
    
    #Strings
    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return f'Circle({self.radius})'

    #Numeric
    def __add__(self, other_circle):
        return circle(self.radius + other_circle.radius)

    def __sub__(self, other_circle):
        return circle(self.radius - other_circle.radius)

    def __mul__(self, other_circle):
        return circle(self.radius * other_circle.radius)

    def __floordiv__(self, other_circle):
        return circle(self.radius // other_circle.radius)

    def __truediv__(self, other_circle):
        return circle(self.radius / other_circle.radius)

    def __mod__(self, other_circle):
        return circle(self.radius % other_circle.radius)

    #Comparison
    def __lt__(self, other_circle):
        return self.radius < other_circle.radius

    def __le__(self, other_circle):
        return self.radius <= other_circle.radius

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __ne__(self, other_circle):
        return self.radius != other_circle.radius

    def __ge__(self, other_circle):
        return self.radius >= other_circle.radius

    def __gt__(self, other_circle):
        return self.radius > other_circle.radius

    #Sorting






a = circle(2)
print(a.radius)
print(a.diameter)
print(a.circumference)
print(a.area)
a.radius = 8
print(a)
print(a.radius)
print(a.diameter)
print(a.circumference)
print(a.area)
a.diameter = 16
print(a.radius)
print(a.diameter)
print(a.circumference)
print(a.area)
print(a)
print(repr(a))

b = circle(4)
print(a)
print(b)
c= a+b
print(repr(c))
print(a+b)
print(c)
print(a-b)
print(a//b)
print(a/b)
print(a%b)

print(a>b)
print(a>=b)
print(a==b)
print(a<=b)
print(a<b)
print(a!=b)

d = circle(20)

circles = [a, d, b, c]
print(circles)

f = circle.from_diameter(4)
print(f.diameter)
print(f.radius)
#print(circles.sort(key=lambda circle: float(circle.radius), reverse=True))

#print(a * 3)