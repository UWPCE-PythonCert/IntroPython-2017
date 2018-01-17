"""
Kathryn Egan

QUESTIONS:
- How would you recommend documenting that a paramater
can be either an integer or a float? E.g. radius.setter


"""
from math import pi


class Circle:
    """ Provides functionality for a Circle."""

    def __init__(self, radius):
        """ Initializes Circle with given radius.
        Args:
            radius (int) : radius of circle
        """
        if radius <= 0:
            raise ValueError('Radius must be >0')
        self._radius = radius

    @property
    def radius(self):
        """ Returns radius of circle.
        Returns:
            int : circle radius
        """
        return self._radius

    @property
    def diameter(self):
        """ Returns diameter of circle.
        Returns:
            int : circle diameter
        """
        return self._radius * 2

    @property
    def area(self):
        """ Returns area of circle.
        Returns:
            float : area of circle
        """
        return pi * self._radius ** 2

    @radius.setter
    def radius(self, radius):
        """ Sets radius of circle.
        Args:
            radius (int) : circle radius
        """
        if radius <= 0:
            raise ValueError('Radius must be >0')
        self._radius = radius

    @diameter.setter
    def diameter(self, diameter):
        """ Sets radius of circle using diameter.
        Args:
            diameter (int) : diameter of radius
        """
        if diameter <= 0:
            raise ValueError('Diameter must be >0')
        self._radius = diameter / 2

    @classmethod
    def from_diameter(cls, diameter):
        """ Returns new Circle object using given diameter.
        Args:
            diameter (int) : diameter of circle
        Returns:
            Circle : Circle object with given diameter
        """
        return cls(diameter / 2)

    def __str__(self):
        """ Returns circle as string.
        Return:
            str : circle as string
        """
        return 'Circle, r={:.1f}'.format(self._radius)

    def __repr__(self):
        """ Returns representation of circle.
        Returns:
            str : representation of circle
        """
        return 'Circle({:.1f})'.format(self._radius)

    def __int__(self):
        """ Returns this Circle's radius as an integer.
        Returns:
            int : radius of circle
        """
        return int(self._radius)

    def __float__(self):
        """ Returns this Circle's radius as a float.
        Returns:
            float : radius of circle
        """
        return float(self._radius)

    def __add__(self, other):
        """ Returns a new Circle with a radius equal to
        this Circle's radius plus the given integer or
        given Circle's radius.
        Args:
            other (int or Circle) : integer or another Circle
        Returns:
            Circle :
                Circle object with a radius equal to this Circle's radius
                plus given integer/radius of given Circle
        """
        return Circle(float(self) + float(other))

    def __radd__(self, other):
        """ Adds commutative functionality for adding Circles and integers. """
        return self.__add__(other)

    def __sub__(self, other):
        """ Returns a new Circle with a radius equal to
        this Circle's radius minus the given integer or
        given Circle's radius. Raises ValueError if self-other
        results in a Circle with a radius <= 0.
        Args:
            other (int or Circle) : integer or another Circle
        Returns:
            Circle :
                Circle object with a radius equal to this Circle's radius
                minus given integer/radius of given Circle
        """
        return Circle(float(self) - float(other))

    def __rsub__(self, other):
        """ Adds commutative functionality for subtracting
        Circles and integers. """
        return Circle(float(other) - float(self))

    def __mul__(self, other):
        """ Returns a new Circle with a radius equal to
        this Circle's radius times the given integer or
        given Circle's radius.
        Args:
            other (int or Circle) : integer or another Circle
        Returns:
            Circle :
                Circle object with a radius equal to this Circle's radius
                times given integer/radius of given Circle
        """
        return Circle(float(self) * float(other))

    def __rmul__(self, other):
        """ Adds commutative functionality for multiplying
        Circles and integers. """
        return self.__mul__(other)

    def __truediv__(self, other):
        """ Returns a new Circle with a radius equal to
        this Circle's radius divided by the given integer or
        given Circle's radius.
        Args:
            other (int or Circle) : integer or another Circle
        Returns:
            Circle :
                Circle object with a radius equal to this Circle's radius
                divided by given integer/radius of given Circle
        """
        return Circle(float(self) / float(other))

    def __rtruediv__(self, other):
        """ Adds commutative functionality for dividing
        Circles and integers. """
        return Circle(float(other) / float(self))

    def __eq__(self, other):
        """ Returns whether this Circle's radius is equal
        to another Circle's radius.
        Args:
            other (Circle) : Circle to compare against
        Returns:
            bool : True if this Circle's radius = other's, False otherwise
        """
        return self.radius == other.radius

    def __lt__(self, other):
        """ Returns whether this Circle's radius is less than
        another Circle's radius.
        Args:
            other (Circle) : Circle to compare against
        Returns:
            bool : True if this Circle's radius < other's, False otherwise
        """
        return self.radius < other.radius

    def __le__(self, other):
        """ Returns whether this Circle's radius is less than
        or equal to another Circle's radius.
        Args:
            other (Circle) : Circle to compare against
        Returns:
            bool : True if this Circle's radius <= other's, False otherwise
        """
        return self.radius <= other.radius

    def __gt__(self, other):
        """ Returns whether this Circle's radius is greater than
        another Circle's radius.
        Args:
            other (Circle) : Circle to compare against
        Returns:
            bool : True if this Circle's radius > other's, False otherwise
        """
        return self.radius > other.radius

    def __ge__(self, other):
        """ Returns whether this Circle's radius is greater than
        or equal to another Circle's radius.
        Args:
            other (Circle) : Circle to compare against
        Returns:
            bool : True if this Circle's radius >= other's, False otherwise
        """
        return self.radius >= other.radius


class Sphere(Circle):

    @property
    def volume(self):
        """ Returns volume of sphere.
        Returns:
            float : volume of sphere
        """
        return (4 / 3) * pi * self.radius ** 3

    @property
    def area(self):
        """ Returns surface area of sphere.
        Returns:
            float : surface area of sphere
        """
        return 4 * super().area

    @classmethod
    def from_volume(cls, volume):
        """ Returns new Sphere with given volume.
        Args:
            volume (int) : volume of sphere
        Returns:
            Sphere : sphere with given volume
        """
        radius = (volume * 3 / (4 * pi)) ** (1 / 3)
        return cls(radius)
