#!/usr/bin/env python3
"""
Circle example
"""
from math import pi

class Circle(object):
    """ Circle class
    """
    _radius = None

    def __init__(self, radius):
        """
        :param radius: radius of circle
        :type: int
        """
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """
        :param diameter: the circle's diameter
        :type: int or float
        """
        if Circle.is_valid_value(diameter):
            return Circle(diameter/2)
        raise ValueError("invalid diameter")


    @staticmethod
    def is_valid_value(value):
        """ Ensures radius or diameter value is an int or float
        :param value: the value to test
        :type: python primitive type

        :return: whether or not the value is a valid one for radius or diameter
        :rtype: boolean
        """
        if not isinstance(value, (int, float)):
            return False
        elif value < 0:
            return False

        return True


    def __repr__(self):
        return "Circle({})".format(self._radius)


    def __str__(self):
        return "Circle with radius: {}".format(self._radius)


    def __add__(self, other_circle):
        return Circle(self._radius + other_circle.radius)


    def __mul__(self, multiplier):
        return Circle(self._radius * multiplier)


    def __rmul__(self, multiplier):
        return Circle(self._radius * multiplier)


    def __eq__(self, other_circle):
        return self._radius == other_circle.radius


    def __ne__(self, other_circle):
        return self._radius != other_circle.radius


    def __lt__(self, other_circle):
        return self._radius < other_circle.radius


    def __gt__(self, other_circle):
        return self._radius > other_circle.radius


    def __inplaceadd__(self, other_circle):
        return Circle(self._radius + other_circle.radius)


    def __inplacemultiply__(self, multiplier):
        return Circle(self._radius * multiplier)


    def __int__(self):
        return self._radius


    def __float__(self):
        return self._radius


    @property
    def radius(self):
        """ radius getter """
        return self._radius


    @property
    def diameter(self):
        """ diameter getter """
        return self._radius * 2


    @property
    def area(self):
        """ area getter """
        return pi * self._radius**2


    @radius.setter
    def radius(self, radius_value):
        """ radius setter
        :param radius_value: radius value
        :type: int or float
        """
        if Circle.is_valid_value(radius_value):
            self._radius = radius_value
        else:
            raise ValueError("invalid radius")


    @diameter.setter
    def diameter(self, diameter_value):
        """ diameter setter
        :param diameter_value: radius value
        :type: int
        """
        if Circle.is_valid_value(diameter_value):
            self.radius = diameter_value / 2
        else:
            raise ValueError("invalid radius")
