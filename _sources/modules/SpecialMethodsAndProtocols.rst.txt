Special Methods & Protocols
===========================

.. rst-class:: left
.. container::

    Special methods (also called *magic* methods) are the secret sauce to Python's Duck typing.

    Defining the appropriate special methods in your classes is how you make your class act like standard classes.

What's in a Name?
-----------------

We've seen at least one special method so far::

    __init__

It's all in the double underscores...

Pronounced "dunder" (or "under-under")

try: ``dir(2)``  or ``dir(list)``

Generally Useful Special Methods
--------------------------------

Most classes should at least have these special methods:

``object.__str__``:
  Called by the str() built-in function and by the print function to compute
  the *informal* string representation of an object.

``object.__repr__``:
  Called by the repr() built-in function to compute the *official* string representation of an object.

  (ideally: ``eval( repr(something) ) == something``)


Protocols
----------

.. rst-class:: build
.. container::

    The set of special methods needed to emulate a particular type of Python object is called a *protocol*.

    Your classes can "become" like Python built-in classes by implementing the methods in a given protocol.

    Remember, these are more *guidelines* than laws.  Implement what you need.

The Numerics Protocol
---------------------

Do you want your class to behave like a number? Implement these methods:

.. code-block:: python

    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)

The Container Protocol
----------------------

Want to make a container type? Here's what you need:

.. code-block:: python

    object.__len__(self)
    object.__getitem__(self, key)
    object.__setitem__(self, key, value)
    object.__delitem__(self, key)
    object.__iter__(self)
    object.__reversed__(self)
    object.__contains__(self, item)
    object.__getslice__(self, i, j)
    object.__setslice__(self, i, j, sequence)
    object.__delslice__(self, i, j)

An Example
----------

Each of these methods supports a common Python operation.

For example, to make '+' work with a sequence type in a vector-like fashion,
implement ``__add__``:

.. code-block:: python

    def __add__(self, v):
        """return the element-wise vector sum of self and v
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])

.. rst-class:: centered

[a more complete example may be seen :download:`here <../examples/vector.py>`]

Protocols in Summary
--------------------

Use special methods when you want your class to act like a "standard" class in some way.

Look up the special methods you need and define them.

There's more to read about the details of implementing these methods:

* https://docs.python.org/3.5/reference/datamodel.html#special-method-names

Emulating Standard types
=========================

.. rst-class:: medium

  Making your classes behave like the built-ins

Callable classes
-----------------

We've been using functions a lot:

.. code-block:: python

    def my_fun(something):
        do_something
        ...
        return something

And then we can call it:

.. code-block:: python

    result = my_fun(some_arguments)

.. nextslide::

But what if we need to store some data to know how to evaluate that function?

Example: a function that computes a quadratic function:

.. math::

    y = a x^2 + bx + c

You could pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

But what if you are using the same a, b, and c numerous times?

Or what if you need to pass this in to something
(like map) that requires a function that takes a single argument?

"Callables"
-----------

Various places in python expect a "callable" -- something that you can
call like a function:

.. code-block:: python

    a_result = something(some_arguments)

"something" in this case is often a function, but can be anything else
that is "callable".

What have we been introduced to recently that is "callable", but not a
function object?

Custom callable objects
------------------------

The trick is one of Python's "magic methods"

.. code-block:: python

    __call__(*args, **kwargs)

If you define a ``__call__`` method in your class, it will be used when
code "calls" an instance of your class:

.. code-block:: python

    class Callable:
        def __init__(self, .....)
            some_initilization
        def __call__(self, some_parameters)

Then you can do:

.. code-block:: python

    callable_instance = Callable(some_arguments)

    result = callable_instance(some_arguments)

Writing your own sequence type
------------------------------

Python has a handful of nifty sequence types built in:

 * lists
 * tuples
 * strings
 * ...

But what if you need a sequence that isn't built in?

A Sparse array
--------------

Example: Sparse Array

Sometimes we have data sets that are "sparse" -- i.e. most of the values are zero.

So you may not want to store a huge bunch of zeros.

But you do want the array to look like a regular old sequence.

So how do you do that?

The Sequence protocol
----------------------

You can make your class look like a regular python sequence by defining
the set of special methods you need:

https://docs.python.org/3/reference/datamodel.html#emulating-container-types

The key ones are:

+-------------------+-----------------------+
|  ``__len__``      | for ``len(sequence)`` |
+-------------------+-----------------------+
|  ``__getitem__``  | for  ``x = seq[i]``   |
+-------------------+-----------------------+
|  ``__setitem__``  | for ``seq[i] = x``    |
+-------------------+-----------------------+
|  ``__delitem__``  | for ``del seq[i]``    |
+-------------------+-----------------------+
|  ``__contains__`` | for ``x in seq``      |
+-------------------+-----------------------+
