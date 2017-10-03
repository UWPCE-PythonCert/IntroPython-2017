***************************
Object Orientation Overview
***************************

In the Beginning there was the GOTO.

And in fact, there wasn't even that.


Programming Paradigms
=====================

https://en.wikipedia.org/wiki/Programming_paradigm

Software Design
---------------

Good software design is about code re-use, clean separation of concerns,
refactorability, testability, etc...

OO can help with all that, but:
  * It doesn't guarantee it
  * It can get in the way

What is Object Oriented Programming?

|
    "Objects can be thought of as wrapping their data
    within a set of functions designed to ensure that
    the data are used appropriately, and to assist in
    that use"

|

http://en.wikipedia.org/wiki/Object-oriented_programming

.. nextslide::

Even simpler:

"Objects are data and the functions that act on them in one place."

This is the core of "encapsulation"

The Dominant Model
------------------

OO is the dominant model for the past couple decades, but it is not the only model, and languages such as Python increasingly mix and blend among models.

Object Oriented Concepts
------------------------

.. rst-class:: medium centered

.. container::

  Classes

  Instances or Objects

  Encapsulation

  Class and instance attributes

  Subclassing

  Overriding methods

  Operator Overloading

  Polymorphism

  Dynamic Dispatch

Definitions
-----------

class
  A category of objects: particular data and behavior: A "circle" (same as a type in python)

instance
  A particular object of a class: a specific circle

object
  The general case of an instance -- really any value (in Python anyway)

attribute
  Something that belongs to an object (or class): generally thought of
  as a variable, or single object, as opposed to a ...

method
  A function that belongs to a class

Python and OO
-------------

Is Python a "True" Object-Oriented Language?

What are its strengths and weaknesses vis-a-vis OO?

It does not support full encapsulation, i.e., it does not require classes,  etc.

.. nextslide::

Folks can't even agree on what OO "really" means

See: The Quarks of Object-Oriented Development

  - Deborah J. Armstrong

http://agp.hx0.ru/oop/quarks.pdf

.. nextslide::

Think in terms of what makes sense for your project
 -- not any one paradigm of software design.

.. nextslide::

OO Buzzwords

  * data abstraction
  * encapsulation
  * modularity
  * polymorphism
  * inheritance

Python provides for all of this, though it doesn't enforce or require any of it.

Python's roots
--------------

|  C
|  C with Classes (aka C++)
|  Modula2
|

You can do OO in C
------------------

Which today is not considered an OO Language.

See the GTK+ project.

OO languages give you some handy tools to make it easier (and safer):

  * polymorphism (duck typing gives you this)
  * inheritance

You will need to understand OO
------------------------------

- It's a good idea for a lot of problems

- You'll need to work with OO packages

(Much of the standard library is object oriented)