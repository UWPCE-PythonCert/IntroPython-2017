#!/usr/bin/env python

"""
json_save implemented as a decorator
"""

import json

from .json_save_meta import *
from .json_save_meta import ALL_SAVABLES


# assorted methods that will need to be added:
def to_json_compat(self):
    """
    converts this object to a json-compatible dict.

    returns the dict
    """
    # add and __obj_type attribute, so it can be reconstructed
    dic = {"__obj_type": self.__class__.__qualname__}
    for attr, typ in self._attrs_to_save.items():
        dic[attr] = typ.to_json_compat(getattr(self, attr))
    return dic


def __eq__(self, other):
    """
    default equality method that checks if all of the saved attributes
    are equal
    """
    for attr in self._attrs_to_save:
        try:
            if getattr(self, attr) != getattr(other, attr):
                return False
        except AttributeError:
            return False
    return True

@classmethod
def from_json_dict(cls, dic):
    """
    creates an instance of this class populated by the contents of
    the json compatible dict

    the object is created with __new__ before setting the attributes

    NOTE: __init__ is not called.
    There should not be any extra initialization required in __init__
    """
    # create a new object
    obj = cls.__new__(cls)
    for attr, typ in cls._attrs_to_save.items():
        setattr(obj, attr, typ.to_python(dic[attr]))
    # make sure it gets initialized
    # obj.__init__()
    return obj


def to_json(self, fp=None, indent=4):
    """
    Converts the object to JSON

    :param fp=None: an open file_like object to write the json to.
                    If it is None, then a string with the JSON
                    will be returned as a string

    :param indent=4: The indentation level desired in the JSON
    """
    if fp is None:
        return json.dumps(self.to_json_compat(), indent=indent)
    else:
        json.dump(self.to_json_compat(), fp, indent=indent)


# now the actual decorator
def json_save(cls):
    """
    json_save decorator

    makes decorated classes savable to json
    """
    # make sure this is decorating a class object
    if type(cls) is not type:
        raise TypeError("json_save can only be used on classes")

    # find the saveable attributes
    # these will the attributes that get saved and reconstructed from json.
    # each class object gets its own dict
    attr_dict = vars(cls)
    cls._attrs_to_save = {}
    for key, attr in attr_dict.items():
        if isinstance(attr, Savable):
            cls._attrs_to_save[key] = attr
    # register this class so we can re-construct instances.
    ALL_SAVABLES[cls.__qualname__] = cls

    # add the methods:
    cls.to_json_compat = to_json_compat
    cls.__eq__ = __eq__
    cls.from_json_dict = from_json_dict
    cls.to_json = to_json

    return cls
