Python Classes
==============


.. rst-class:: left

    The ``class``  statement

    ``class``  creates a new type object:

    .. code-block:: ipython

        In [4]: class C:
            pass
           ...:
        In [5]: type(C)
        Out[5]: type

    A class is a type -- interesting!

    It is created when the statement is run -- much like ``def``

A simple class

About the simplest class you can write

.. code-block:: python

    >>> class Point:
    ...     x = 1
    ...     y = 2
    >>> Point
    <class __main__.Point at 0x2bf928>
    >>> Point.x
    1
    >>> p = Point()
    >>> p
    <__main__.Point instance at 0x2de918>
    >>> p.x
    1

Basic Structure of a class
--------------------------

.. code-block:: python

    class Point:
    # everything defined in here is in the class namespace

        def __init__(self, x, y):
            self.x = x
            self.y = y

    ## create an instance of the class
    p = Point(3,4)

    ## access the attributes
    print("p.x is:", p.x)
    print("p.y is:", p.y)


see: ``Examples/Session07/simple_classes.py``

The Initializer
---------------

The ``__init__``  special method is called when a new instance of a class is created.

You can use it to do any set-up you need

.. code-block:: python

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


It gets the arguments passed when you call the class object:

.. code-block:: python

    Point(x, y)

Self
----

What is this ``self`` thing?

The instance of the class is passed as the first parameter for every method.

"``self``" is only a convention -- but you DO want to use it.

.. code-block:: python

    class Point:
        def a_function(self, x, y):
    ...

Does this look familiar from C-style procedural programming?


.. nextslide::

Anything assigned to a ``self.``  attribute is kept in the instance
name space -- ``self`` *is* the instance.

That's where all the instance-specific data is.

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        def __init__(self, x, y):
            self.x = x
            self.y = y

Class Attributes
----------------

Anything assigned in the class scope is a class attribute -- every
instance of the class shares the same one.

Note: the methods defined by ``def`` are class attributes as well.

The class is one namespace, the instance is another.

.. code-block:: python

    class Point:
        size = 4
        color= "red"
    ...
        def get_color():
            return self.color
    >>> p3.get_color()
     'red'

class attributes are accessed with ``self``  also.


Typical methods
---------------

.. code-block:: python

    class Circle:
        color = "red"

        def __init__(self, diameter):
            self.diameter = diameter

        def grow(self, factor=2):
            self.diameter = self.diameter * factor


Methods take some parameters, manipulate the attributes in ``self``.

They may or may not return something useful.


Arity Gotcha
------------

.. code-block:: python

    ...
        def grow(self, factor=2):
            self.diameter = self.diameter * factor
    ...
    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

Huh???? I only gave 2

``self`` is implicitly passed in for you by python.

Functions (methods) are First Class
-----------------------------------

.. rst-class:: center

    Note that in python, functions are first class objects, so a method *is* an attribute

