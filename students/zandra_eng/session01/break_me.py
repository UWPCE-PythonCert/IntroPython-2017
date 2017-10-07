"""
    Task 1: Explore Errors

    Create a new directory in your working dir for the class:

    $ mkdir session01
    $ cd session01

    Add a new file to it called break_me.py

    In the break_me.py file write four simple Python functions:
        Each function, when called, should cause an exception to happen
        Each function should result in one of the four most common exceptions you’ll find.
        for review: NameError, TypeError, SyntaxError, AttributeError

"""

def name_error():
    x = unknown

def type_error():
    a = 5
    a += "aa"

def syntax_error():
    a 5 .. ;;;;

def attribute_error():
    a = "string"
    a.whatever()

