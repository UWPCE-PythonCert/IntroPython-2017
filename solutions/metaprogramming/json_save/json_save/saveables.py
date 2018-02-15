#!/usr/bin/env python

"""
The Saveable objects used by both the metaclass and decorator approach.
"""
import json

__all__ = ['Bool',
           'Dict',
           'Float',
           'Int',
           'List',
           'Saveable',
           'String',
           'Tuple',
           ]


class Saveable():
    """
    Base class for all saveable types
    """
    default = None
    ALL_SAVEABLES = {}

    @staticmethod
    def to_json_compat(val):
        """
        returns a json-compatible version of val

        should be overridden in saveable types that are not json compatible.
        """
        return val

    @staticmethod
    def to_python(val):
        """
        convert from a json compatible version to the python version

        Must be overridden if not a one-to-one match

        This is where validation could be added as well.
        """
        return val


class String(Saveable):
    """
    A Saveable string

    Strings are the same in JSON as Python, so nothing to do here
    """
    default = ""


class Bool(Saveable):
    """
    A Saveable boolean

    Booleans are pretty much the same in JSON as Python, so nothing to do here
    """
    default = False


class Int(Saveable):

    """
    A Saveable integer

    Integers are a little different in JSON than Python. Strictly speaking
    JSON only has "numbers", which can be integer or float, so a little to
    do here to make sure we get an int in Python.
    """

    default = 0

    @staticmethod
    def to_python(val):
        """
        Convert a number to a python integer
        """
        return int(val)


class Float(Saveable):
    """
    A Saveable floating point number

    floats are a little different in JSON than Python. Strictly speaking
    JSON only has "numbers", which can be integer or float, so a little to
    do here to make sure we get a float in Python.
    """

    default = 0.0

    @staticmethod
    def to_python(val):
        """
        Convert a number to a python float
        """
        return float(val)

# Container types: these need to hold  Saveable objects.

class Tuple(Saveable):
    """
    This assumes that whatever is in the tuple is Saveable  or a "usual"
    type: numbers, strings.
    """
    default = ()

    @staticmethod
    def to_python(val):
        """
        Convert a list to a tuple -- json only has one array type,
        which matches to a list.
        """
        # simply uses the List to_python method -- that part is the same.
        return tuple(List.to_python(val))


class List(Saveable):
    """
    This assumes that whatever is in the list is Saveable or a "usual"
    type: numbers, strings.
    """
    default = []

    @staticmethod
    def to_json_compat(val):
        lst = []
        for item in val:
            try:
                lst.append(item.to_json_compat())
            except AttributeError:
                lst.append(item)
        return lst

    @staticmethod
    def to_python(val):
        """
        Convert an array to a list.

        Complicated because list may contain non-json-compatible objects
        """
        # try to reconstitute using the obj method
        new_list = []
        for item in val:
            try:
                obj_type = item["__obj_type"]
                obj = Saveable.ALL_SAVEABLES[obj_type].from_json_dict(item)
                new_list.append(obj)
            except TypeError:
                new_list.append(item)
        return new_list


class Dict(Saveable):
    """
    This assumes that whatever in the dict is Saveable as well,
    or a basic type.
    """
    default = {}

    @staticmethod
    def to_json_compat(val):
        d = {}
        for key, item in val.items():
            try:
                d[key] = item.to_json_compat()
            except AttributeError:
                d[key] = item
        return d

    @staticmethod
    def to_python(val):
        """
        Convert a json object to a dict

        Complicated because object may contain non-json-compatible objects
        """

        # try to reconstitute using the obj method
        new_dict = {}
        for key, item in val.items():
            try:
                obj_type = item["__obj_type"]
                obj = Saveable.ALL_SAVEABLES[obj_type].from_json_dict(item)
                new_dict[key] = obj
            except TypeError:
                new_dict[key] = item
        return new_dict


