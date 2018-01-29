#!/usr/bin/env python

"""
detect whether correct exception was thrown otherwise raise it
"""

## would like to throw specific error

class raises():

    def __init__(self, ErrType):
        self.ErrType = ErrType
        pass

    def __enter__(self):
        return self.ErrType

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self.ErrType:
            return True
        else:
            raise exc_type
            assert False, "Wrong error thrown"

