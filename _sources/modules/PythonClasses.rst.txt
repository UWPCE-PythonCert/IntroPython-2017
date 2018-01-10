.. _python_classes:

##############
Python Classes
##############

"Classes" are the core of Object Oriented Programming.

They provide the tools for encapsulation (keeping the data with the functions) and subclassing and polymorphism.


How are classes made in Python?
===============================

The ``class`` statement
-----------------------

The ``class``  statement creates a new type object:

.. code-block:: ipython

    In [4]: class C:
        pass
       ...:
    In [5]: type(C)
    Out[5]: type

A class is a type -- interesting!

It is created when the statement is run -- much like ``def``.

So we now have a new type, or class -- it doesn't have any actual functionality, though by default all classes "inherit" from ``object``. In doing so they get some minimal functionality from that:

.. code-block:: ipython

    In [3]: issubclass(C, object)
    Out[3]: True

We can print it:

.. code-block:: ipython

    In [4]: print(C)
    <class '__main__.C'>

And look at all the methods it has!

.. code-block:: ipython

    In [5]: dir(C)
    Out[5]:
    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__']

Most of those don't do anything -- but they are there, so every class is guaranteed to have all the "stuff" Python expects objects to have.

In order for the class to do anything useful, it needs to be given attributes and methods.


A simple ``class``
------------------

About the simplest class you can write that is still useful:

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

This looks a lot like a "struct" in C -- Python doesn't have structures, so yes, a class with no methods (functions) is essentially a struct.

Basic Structure of a class
--------------------------

.. code-block:: python

    class Point:
    # everything defined in here is in the class namespace

        def __init__(self, x, y):
            self.x = x
            self.y = y

so this class has a method called "__init__" -- which is a Python special method.

see: :download:`simple_classes.py <../examples/classes/simple_classes.py>`

The Initializer
---------------

The ``__init__``  special method is called when a new instance of a class is created.

You can use it to do any set-up you need:

.. code-block:: python

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


It gets the arguments passed when you call the class object:

.. code-block:: python

    Point(x, y)

Once you have defined an __init__, you can create "instances" of the class:

.. code-block:: python

    p = Point(3,4)

And access the attributes:

.. code-block:: python

    print("p.x is:", p.x)
    print("p.y is:", p.y)


Self
----

What is this ``self`` thing?

The instance of the class is passed as the first parameter for every method.

The name "``self``" is only a convention -- but you *DO* want to use it.

.. code-block:: python

    class Point:
        def a_function(self, x, y):
    ...

Does this look familiar from C-style procedural programming?

Anything assigned to a ``self.``  attribute is kept in the instance
name space -- ``self`` *is* the instance.

That's where all the instance-specific data is.


Class Attributes
----------------

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        def __init__(self, x, y):
            self.x = x
            self.y = y

Anything assigned in the class scope is a class attribute -- every
instance of the class shares the same one.

Note: the methods defined by ``def`` are class attributes as well.

The class is one namespace, the instance is another.

.. code-block:: python

    class Point:
        size = 4
        color = "red"
    ...
        def get_color():
            return self.color
    >>> p3.get_color()
     'red'

So in this case, ``size`` and ``color`` are class attributes.

But note in ``get_color`` -- it accesses color from ``self``:

class attributes are accessed with ``self``  also.

So what is the difference?

 * class attributes are shared by ALL the instances of the class.
 * each instance has its own copy of each instance attribute.

Example:

.. code-block:: ipython

    In [6]: class C:
       ...:     x = [1,2,3] # class attribute
       ...:     def __init__(self):
       ...:         self.y = [4,5,6] # instance attribute
       ...:

    In [7]: c1 = C()

    In [8]: c2 = C()

    In [9]: c1.x is c2.x # does each instance see the same x?
    Out[9]: True

    In [10]: c1.y is c2.y # does each instance see the same y?
    Out[10]: False


Typical methods
---------------

.. code-block:: python

    class Circle:
        color = "red"

        def __init__(self, diameter):
            self.diameter = diameter

        def expand(self, factor=2):
            self.diameter = self.diameter * factor


Methods take some parameters, manipulate the attributes in ``self``.

They may or may not return something useful.


Gotcha !
--------

.. code-block:: python

    ...
        def grow(self, factor=2):
            self.diameter = self.diameter * factor
    ...
    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

Huh???? I only gave 2:

``self`` is implicitly passed in for you by Python. so it actually *did* get three!


Functions (methods) are First Class
-----------------------------------

Note that in Python, functions are first class objects, so a method *is* an attribute.

All the same rules apply about attribute access: note that the methods are defined in the class -- so they are class attributes. All the instances share the same methods.

But each method gets its own namespace when it is actually called, so there is no confusion-- just like when you call a regular function multiple times.


