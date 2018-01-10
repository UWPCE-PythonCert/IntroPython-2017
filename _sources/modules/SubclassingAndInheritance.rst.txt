.. _subclassing_inheritance:

###########################
Subclassing and Inheritance
###########################

How to put the pieces together to build a complex system without repeating code.

Inheritance
===========

In object-oriented programming (OOP), inheritance is a way to reuse the code
of existing objects, or to establish a subtype from an existing object.

Objects are defined by classes. Classes can inherit attributes and behavior
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

Same thing, but with methods (remember, a method *is* an attribute in Python)

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


all the instances will have the new method.


Here's a program design suggestion:

Whenever you override a method, the interface of the new method should be the same as the old.  It should take the same parameters, return the same type, and obey the same preconditions and postconditions.

If you obey this rule, you will find that any function designed to work with an instance of a superclass, like a Deck, will also work with instances of subclasses like a Hand or PokerHand.  If you violate this rule, your code will collapse like (sorry) a house of cards.

Overriding \_\_init\_\_
-----------------------

``__init__`` is a common method to override.

You often need to call the super class ``__init__``  as well.

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


Exception to: "don't change the method signature" rule.


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


Note that there is nothing special about ``__init__``  except that it gets called automatically when you instantiate an instance. Otherwise, it is the same as any other method -- it gets ``self`` as the first argument, it can or can not call the superclasses methods, etc.


"Favor Object Composition Over Class Inheritance"
-------------------------------------------------

That is a quotation from the "Design Patterns" book -- kind of one of the gospels of OO programming.

But what does it mean?

There are essentially two ways to add multiple functionalities to a class:

Subclassing

and

Composition

As we have just learned about subclassing, you might be tempted to do it a lot. But you need to be careful of over-using subclassing:

https://en.wikipedia.org/wiki/Composition_over_inheritance

Composition is when your classes have attributes of various types that they use to gain functionality -- "delegate" functionality to -- "Delegation" is a related concept in OO.


"Is a" vs "Has a"
.................

Thinking about "is a" vs "has a" can help you sort this out.

For example, you may have a class that needs to accumulate an arbitrary number of objects.

A list can do that -- so maybe you should subclass list?

To help decide -- Ask yourself:

-- **Is** your class a list (with some extra functionality)?

or

-- Does you class **have** a list?

You only want to subclass list if your class could be used anywhere a list can be used. In fact this is a really good way to think about subclassing in general -- subclasses should be specialized versions of the superclass. "Kind of" the same, but with a little different functionality.


Attribute Resolution Order
--------------------------

When you access an attribute:

``an_instance.something``

Python looks for it in this order:

  * Is it an instance attribute ?
  * Is it a class attribute ?
  * Is it a superclass attribute ?
  * Is it a super-superclass attribute ?
  * ...

It can get more complicated, particularly when there are multiple superclasses (multiple inheritance), but when there is a simple inheritance structure (the usual case) -- it's fairly straightforward.

If you want to know more of the gory details -- here's some reading:

https://www.python.org/download/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html


What are Python classes, really?
--------------------------------

Putting aside the OO theory...

Python classes feature:

  * Namespaces

    * One for the class object
    * One for each instance

  * Attribute resolution order -- how do you find an attribute.
  * Auto tacking-on of ``self`` when methods are called
  * automatically calling ``__init__`` when the class object is called.

That's about it -- really!

(Well, not really, there is more fancy stuff going on under the hood -- but this basic structure will get you far).

Type-Based Dispatch
-------------------

You'll see code that looks like this:

.. code-block:: python

      if isinstance(other, A_Class):
          Do_something_with_other
      else:
          Do_something_else

When it's called for, Python provides these utilties:

    * ``isinstance()``
    * ``issubclass()``

But it is very rarely called for! Between Duck typing, polymorphism, and EAFP, you rarely need to check for type directly.

Wrap Up
-------

Thinking OO in Python:

Think about what makes sense for your code:

* Code re-use
* Clean APIs
* Separation of Concerns
* ...

OO can be a very powerful approach, but don't be a slave to what OO is *supposed* to look like.

Let OO work for you, not *create* work for you.

