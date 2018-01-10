.. _multiple_inheritance:


####################
Multiple Inheritance
####################


Inheriting from more than one class.
====================================

The mechanics of multiple inheritance
-------------------------------------

Simply provide more than one parent.

.. code-block:: python

    class Combined(Parent1, Parent2, Parent3):
        def __init__(self, something, something else):
            # some custom initialization here.
            Parent1.__init__(self, ......)
            Parent2.__init__(self, ......)
            Parent3.__init__(self, ......)
            # possibly more custom initialization

Calls to the parent class ``__init__``  are optional and case dependent. (and maybe you can use super()...stay tuned)

The Combined class now has ALL the attribute and methods of the multiple parent classes. You can bring a lot of functionality into a class that way.


Purpose
-------

What was the purpose behind inheritance?

*Code reuse.*

What is the purpose behind multiple inheritance?

*Code reuse.*

What wasn't the purpose of inheritance?

*Building massive class hierarchies for their own sake.*

What isn't the purpose of multiple inheritance?

*Building massive class hierarchies for their own sake.*

Mix-ins
-------

Why would you want to do this?

Hierarchies are not always simple:

* Animal

  * Mammal

    * give_birth()

  * Bird

    * lay_eggs()

Where do you put a Platypus or Spiny Anteater?
[http://www.ucmp.berkeley.edu/mammal/monotreme.html]

"mix-ins" can solve this problem. A mix-in is a class that can't do anything by itself, but rather, provides functionality that can be mixed into other classes.

In the above contrived example, we could put "give_birth" (and associated methods) in a BirthGiver mixin, and lay_eggs in an EggLayer mixin, and then make our mammals, birds and platypi from them:

.. code-block:: python

    class Platypus(Animal, EggLayer):
        ...

    class Cat(Animal, BirthGiver):
       ...

    class Duck(Animal, EggLayer):
       ...

But this is pretty darn contrived .. where do you use these for real?

Real World Example: The wxPython FloatCanvas:

https://github.com/wxWidgets/Phoenix/blob/master/wx/lib/floatcanvas/FCObjects.py

I had read about mixins quite a while ago, and I thought they were pretty cool. But I couldn't imagine where I might actually use them.

Then I set out to write FloatCanvas  -- a scalable, pan-able, object-persistent drawing canvas for the wxPython toolkit.

What I discovered is that the draw objects were not in a clean hierarchy -- some objects had a line (like a poly line), some had just a fill (like a dot), some had a fill and outline (polygon), some were defined by a single point (a dot again), some by a bunch of points (polygon), etc....

In order to not write a lot of repeated code -- remember, "classes are for code re-use", I put all the individual bits of functionality into mixin classes, and then simply put them together in different ways.

Once the system was set up, all you needed to write was a ``__init__`` and a draw method to make a whole new graphic object.

FloatCanvas has a lot of complications with handling mouse events, and managing pens and brushes, and what have you, so a very trimmed down version, using the Python Imaging Library, is here to check out and modify:

:download:`object_canvas.py <../examples/object_oriented/object_canvas.py>`
and
:download:`test_object_canvas.py <../examples/object_oriented/test_object_canvas.py>`


Python's Multiple Inheritance Model
===================================

Cooperative Multiple Inheritance

Emphasis on cooperative!

* Play by the rules and everybody benefits (parents, descendants).
* Play by the rules and nobody gets hurt (yourself, mostly).
* We're all adults here.

What could go wrong?

The Diamond Problem
-------------------

In Python, everything is descended from 'object'.  Thus, the moment you invoke multiple inheritance you have the diamond problem.

https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem


``super()``
-----------

``super()`` can help.

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


What does super() do?
----------------------

.. code-block:: python

    class ChildB(Base):
        def __init__(self):
            mro = type(self).mro()
            for next_class in mro[mro.index(ChildB) + 1:]: # slice to end
                if hasattr(next_class, '__init__'):
                    next_class.__init__(self)
                    break

http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

``super`` returns a "proxy object" that delegates method calls.

It's not returning the object itself -- but you can call methods on it.

It runs through the method resolution order (MRO) to find the method
you call.

Key point: the MRO is determined *at run time*

https://docs.python.org/3.6/library/functions.html#super

Not the same as calling one superclass method: ``super()`` will call all the sibling superclass methods:

.. code-block:: python

    class D(C, B, A):
        def __init__(self):
           super().__init__()

same as:

.. code-block:: python

    class D(C, B, A):
        def __init__(self):
           C.__init__()
           B.__init__()
           A.__init__()

You may not want that ...

But if you do, it's kind of handy.


.. Dependency Injection
.. --------------------

.. Super() is the right way to do dependency injection.

.. https://en.wikipedia.org/wiki/Dependency_injection

.. Compare with Monkey Patching as done in other languages.

.. https://en.wikipedia.org/wiki/Monkey_patch

.. This "Dependency_injection" works, because the MRO is defined at run time --ao anything you add to a superclass will take effect the moment it is there.

.. Read Hettinger's "super() considered super" (below) to get an idea about that


Using ``super()``
=================

The rules:
----------

Raymond Hettinger's rules for ``super()``

1. The method being called by super() needs to exist

2. The caller and callee need to have a matching argument signature

3. Every occurrence of the method needs to use super()

(1) is pretty obvious :-)

(2) we'll get into in a moment

(3) This is a tricky one -- you jsut need to remember it. What it means is that, for isntance, if you are using super() to call __init__ in the superclass(s), then all teh superclasses __init__ methods msut ALSO call it:

.. code-block:: python

    def __init__(self, *args, **kwargs)
        ...
        super().__init__(*args, **kwargs)
        ...

Failure to do that will cause odd errors!

This is a bit weird -- it means that if you have a method that may get called with a super call, it needs to use super itself, EVEN if it doesn't need to call the superclass' method!

See the example later for this...


Matching Argument Signature
---------------------------

Remember that super does not only delegate to your superclass, it delegates to any class in the MRO.

Therefore you must be prepared to call any other class's method in the hierarchy and be prepared to be called from any other class's method.

The general rule is to pass all arguments you received on to the super function.

That means that all the methods with the same name need to be able to accept the same arguments. In some cases, that's straightforward -- they are all the same. But sometimes it gets tricky.

Remember that if you write a function that takes:

``def fun(self, *args, **kwargs)``

It can accept ANY arguments. But if you find yourself needing to do that -- maybe super isn't the right thing to use??

But a really common case, particularly for an ``__init__``, is for it to take a bunch of keyword arguments. And a subclass may take one or two more, and then want to pass the rest on. So a common pattern is:

.. code-block:: python

    class Subclass(Superclass):
        def __init__(self, extra_arg1, extra_arg2, *args, **kwargs):
            super().__init__(*args, **kwargs)

Now your subclass doesn't really need to think about all the arguments the superclass can take.


Two seminal articles
--------------------

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"Super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

https://youtu.be/EiOglTERPEo

Both perspectives worth your consideration. In fact, they aren't that different...

Both actually say similar things:

* The method being called by super() needs to exist
* Every occurrence of the method needs to use super():

  - Use it consistently, and document that you use it, as it is part
    of the external interface for your class, like it or not.

If you follow these rules, then it really can be *super*

Example:
--------







