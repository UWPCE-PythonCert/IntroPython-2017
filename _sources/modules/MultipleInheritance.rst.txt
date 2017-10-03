Multiple Inheritance
====================

Multiple inheritance: Inheriting from more than one class.

Simply provide more than one parent.

.. code-block:: python

    class Combined(Parent1, Parent2, Parent3):
        def __init__(self, something, something else):
            # some custom initialization here.
            Parent1.__init__(self, ......)
            Parent2.__init__(self, ......)
            Parent3.__init__(self, ......)
            # possibly more custom initialization

Calls to the parent class ``__init__``  are optional and case dependent.

Purpose
-------

What was the purpose behind inheritance?

Code reuse.

What is the purpose behind multiple inheritance?

Code reuse.

What wasn't the purpose of inheritance?

Building massive class hierarchies for their own sake.


What isn't the purpose of multiple inheritance?

Building massive class hierarchies for their own sake.

Python's Multiple Inheritance Model
-----------------------------------

Cooperative Multiple Inheritance

Emphasis on cooperative!

* Play by the rules and everybody benefits (parents, descendants).
* Play by the rules and nobody gets hurt (yourself, mostly).
* We're all adults here.

What could go wrong?

The Diamond Problem
-------------------

With Python "new style" classes everything is descended from 'object'.  Thus, the moment you invoke multiple inheritance you have the diamond problem.

https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem

``super()``
-----------

``super()``: use it to call a superclass method, rather than explicitly calling the unbound method on the superclass.

instead of:

.. code-block:: python

    class A(B):
        def __init__(self, *args, **kwargs)
            B.__init__(self, *argw, **kwargs)
            ...

You can do:

.. code-block:: python

    class A(B):
        def __init__(self, *args, **kwargs)
            super().__init__(*argw, **kwargs)
            ...

MRO: Method Resolution Order
----------------------------

.. code-block:: python

    class Combined(Super1, Super2, Super3)

Attributes are located bottom-to-top, left-to-right

* Is it an instance attribute ?
* Is it a class attribute ?
* Is it a superclass attribute ?

  - Is  it an attribute of the left-most superclass?
  - Is  it an attribute of the next superclass?
  - and so on up the hierarchy...

* Is it a super-superclass attribute ?
* ... also left to right ...

http://python-history.blogspot.com/2010/06/method-resolution-order.html

Super's Superpowers
-------------------

It works out -- dynamically at runtime -- which classes are in the delegation order.

Do not be afraid.  And be very afraid.

Dependency Injection
--------------------

Super() is the right way to do dependency injection.

https://en.wikipedia.org/wiki/Dependency_injection

Compare with Monkey Patching as done in other languages.

https://en.wikipedia.org/wiki/Monkey_patch

Argument Passing
----------------

Remember that super does not only delegate to your superclass, it delegates to any class in the MRO.

Therefore you must be prepared to call any other class's method in the hierarchy and be prepared to be called from any other class's method.

The general rule is to pass all arguments you received on to the super function.  If classes can take differing arguments, accept *args and **kwargs.

Two seminal articles
--------------------

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"Super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

https://youtu.be/EiOglTERPEo

Both perspectives worth your consideration.
