
:orphan:

.. _notes_session09:

####################
Notes for Session 09
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

James Takata

Katherine Marguerite Anderson

Matthew D Briggs

[Make sure you've got the right adapter....]


Issues that came up during the week.
====================================

"private" attributes and dunders
--------------------------------

``_something`` vs ``__something`` vs ``__something__``

Let's talk about that...

Adding parameters to a subclass __init__
----------------------------------------

In general, when you override a method in a subclass, you want the method signature to be the same. That is -- all the parameters should be the same.

However, sometimes, particularly with ``__init__``, you may need a couple extra parameters. To keep things clean and extensible, you want to put the extra parameters at the beginning, before the super class' parameters:

And this lets you use ``*args`` and ``**kwargs`` to pass along the usual ones.

.. code-block:: python

    class Base:
        def __init__(self, par1, par2, par3=something, par4=something):
            ...

    class Subclass(Base):
        def __init__(self, newpar1, newpar2, *args, **kwargs):
            self.newpar1 = newpar1
            self.newpar2 = newpar2
            super().__init__(*args, **kwarg)

Example: html_render Anchor tag:

.. code-block:: python

    class A(OneLineTag):
        """
        anchor element
        """
        tag = "a"

        def __init__(self, link, *args, **kwargs):
            kwargs['href'] = link
            super().__init__(*args, **kwargs)

This becomes particularly important with ``super()`` and subclassing...

which we will get more into today.

Any other html_render questions?
--------------------------------

Lightning Talks
===============

James Takata

Katherine Marguerite Anderson

Matthew D Briggs


New Topics
==========

sorting
-------

maybe it's a good idea to add a sort_key method to your classes?

let's try it on Circle....

classmethod
-----------

``classmethod`` is really pretty simple to use, not much to talk about. But it can be a bit challenging to "get".

The key point is that classmethods work for subclasses -- like for alternate constructors.

Let's look at that with my Circle solution.

(and answer any other questions about Circle, while we are at it)

multiple inheritance and super()
--------------------------------

``super()`` is a mixed bag --it's actually a pretty complex topic, but can be pretty easy to use -- at least in the easy cases.

To get the hang of multiple inheritance, mix-ins, and ``super()``, we'll play around with object canvas:

Object Oriented Mailroom
------------------------

One more time!

Yes, it's time to make mailroom Object oriented:

:ref:`exercise_mailroom_oo`







