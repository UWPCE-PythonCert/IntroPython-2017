
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


Issues that came up during the week.
====================================

"private" attributes and dunders
--------------------------------

``_something`` vs ``__something`` vs ``__something__``

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






