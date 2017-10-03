.. _documentation:

=============
Documentation
=============

It's often helpful to leave information in your code about what you were
thinking when you wrote it.

This can help reduce the number of `WTFs per minute <http://www.osnews.com/story/19266/WTFs_m>`_ in reading it later.

There are two approaches to this in python:

* Comments
* Docstrings

Comments in Python are much the same as any other programing language.

Docstrings are more unusual.

Comments
--------

Comments go inline in the body of your code, to explain reasoning:

.. code-block:: python

    if (frobnaglers > whozits):
        # borangas are shermed to ensure frobnagler population
        # does not grow out of control
        sherm_the_boranga()

You can use them to mark places you want to revisit later:

.. code-block:: python

    for partygoer in partygoers:
        for balloon in balloons:
            for cupcake in cupcakes:
                # TODO: Reduce time complexity here.  It's killing us
                #  for large parties.
                resolve_party_favor(partygoer, balloon, cupcake)

Comments about comments
-----------------------

 * Be judicious in your use of comments.

 * Use them when you need to.

 * Make them useful.

This is not useful:

.. code-block:: python

    for sponge in sponges:
        # apply soap to each sponge
        worker.apply_soap(sponge)

Note: Nothing special about Python here -- basic good programing practice.

Docstrings
----------

In Python, "docstrings" are used to provide in-line documentation in a number of places.

The first place we will see is in the definition of functions.

As you know, to define a function you use the ``def`` keyword.

If a "string literal" is the first thing in the function block following the
header, it is a "docstring":

.. code-block:: python

    def complex_function(arg1, arg2, kwarg1=u'bannana'):
        """Return a value resulting from a complex calculation."""
        # code block here

You can then read this in an interpreter as the ``__doc__`` attribute of the
function object.

A function docstring should:
............................

* Be a complete sentence in the form of a command describing what the function
  does.

  * """Return a list of values based on blah blah""" is a good docstring

  * """Returns a list of values based on blah blah""" is *not* as good..

* Have a useful single line.

  * If more description is needed, make the first line a complete sentence and
    add more lines below for enhancement.

* Be enclosed with triple-quotes.

  * This allows for easy expansion if required at a later date
  * Always close on the same line if the docstring is only one line.

For more information see `PEP 257: Docstring Conventions <http://legacy.python.org/dev/peps/pep-0257/>`_.
