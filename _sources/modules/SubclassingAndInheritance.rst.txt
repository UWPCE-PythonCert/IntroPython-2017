Subclassing and Inheritance
===========================

Inheritance
-----------

In object-oriented programming (OOP), inheritance is a way to reuse code
of existing objects, or to establish a subtype from an existing object.

Objects are defined by classes, classes can inherit attributes and behavior
from pre-existing classes called base classes or super classes.

The resulting classes are known as derived classes or subclasses.

(http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29)

Subclassing
-----------

A subclass "inherits" all the attributes (methods, etc) of the parent class.

You can then change ("override") some or all of the attributes to change the behavior.

You can also add new attributes to extend the behavior.

The simplest subclass in Python:

.. code-block:: python

    class A_subclass(The_superclass):
        pass

``A_subclass``  now has exactly the same behavior as ``The_superclass``

Overriding attributes
---------------------

Overriding is as simple as creating a new attribute with the same name:

.. code-block:: python

    class Circle:
        color = "red"

    ...

    class NewCircle(Circle):
        color = "blue"
    >>> nc = NewCircle
    >>> print(nc.color)
    blue


all the ``self``  instances will have the new attribute.

Overriding methods
------------------

Same thing, but with methods (remember, a method *is* an attribute in python)

.. code-block:: python

    class Circle:
    ...
        def grow(self, factor=2):
            """grows the circle's diameter by factor"""
            self.diameter = self.diameter * factor
    ...

    class NewCircle(Circle):
    ...
        def grow(self, factor=2):
            """grows the area by factor..."""
            self.diameter = self.diameter * math.sqrt(2)


all the instances will have the new method

.. nextslide::

Here's a program design suggestion:

Whenever you override a method, the interface of the new method should be the same as the old.  It should take the same parameters, return the same type, and obey the same preconditions and postconditions.

If you obey this rule, you will find that any function designed to work with an instance of a superclass, like a Deck, will also work with instances of subclasses like a Hand or PokerHand.  If you violate this rule, your code will collapse like (sorry) a house of cards.

Overriding \_\_init\_\_
-----------------------

``__init__`` common method to override

You often need to call the super class ``__init__``  as well

.. code-block:: python

    class Circle:
        color = "red"
        def __init__(self, diameter):
            self.diameter = diameter
    ...
    class CircleR(Circle):
        def __init__(self, radius):
            diameter = radius*2
            Circle.__init__(self, diameter)


exception to: "don't change the method signature" rule.

Using the superclasses' methods
-------------------------------

You can also call the superclass' other methods:

.. code-block:: python

    class Circle:
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2


    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)

There is nothing special about ``__init__``  except that it gets called
automatically when you instantiate an instance.

When to Subclass
----------------

"Is a" relationship: Subclass/inheritance

"Has a" relationship: Composition

.. nextslide::

"Is a" vs "Has a"

You may have a class that needs to accumulate an arbitrary number of objects.

A list can do that -- so should you subclass list?

Ask yourself:

-- **Is** your class a list (with some extra functionality)?

or

-- Does you class **have** a list?

You only want to subclass list if your class could be used anywhere a list can be used.

Attribute resolution order
--------------------------

When you access an attribute:

``an_instance.something``

Python looks for it in this order:

  * Is it an instance attribute ?
  * Is it a class attribute ?
  * Is it a superclass attribute ?
  * Is it a super-superclass attribute ?
  * ...

It can get more complicated...

https://www.python.org/download/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html

What are Python classes, really?
--------------------------------

Putting aside the OO theory...

Python classes are:

  * Namespaces

    * One for the class object
    * One for each instance

  * Attribute resolution order
  * Auto tacking-on of ``self`` when methods are called

That's about it -- really!

Type-Based dispatch
-------------------

You'll see code that looks like this:

.. code-block:: python

      if isinstance(other, A_Class):
          Do_something_with_other
      else:
          Do_something_else

When it's called for:

    * ``isinstance()``
    * ``issubclass()``
