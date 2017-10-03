.. _booleans:

###################
Boolean Expressions
###################

Truthiness
----------

What is true or false in Python?

* The Booleans: ``True``  and ``False``

* "Something or Nothing"

*  http://mail.python.org/pipermail/python-dev/2002-April/022107.html


Determining Truthiness:

.. code-block:: python

    bool(something)


What is False?
--------------

* ``None``

* ``False``

* **Nothing:**

    - Zero of any numeric type: ``0, 0.0, 0j``.
    - Any empty sequence, for example, ``"", (), []``.
    - Any empty mapping, for example, ``{}`` .
    - Instances of user-defined classes, if the class defines a ``__nonzero__()`` or ``__len__()`` method, when that method returns the integer zero or bool value ``False``.

* http://docs.python.org/library/stdtypes.html

What is True?
-------------

Everything Else


Pythonic Booleans
-----------------

Any object in Python, when passed to the ``bool()`` type object, will
evaluate to ``True`` or ``False``.

When you use the ``if`` keyword, it automatically does this to the expression provided.

Which means that this is redundant, and not Pythonic:

.. code-block:: python

    if xx == True:
        do_something()
    # or even worse:
    if bool(xx) == True:
        do_something()

Instead, use what Python gives you:

    if xx:
        do_something()

``and``, ``or`` and ``not``
---------------------------

Python has three boolean keywords, ``and``, ``or`` and ``not``.

``and`` and ``or`` are binary expressions, and evaluate from left to right.

``and`` will return the first operand that evaluates to False, or the last
operand if none are True:

.. code-block:: ipython

    In [35]: 0 and 456
    Out[35]: 0

``or`` will return the first operand that evaluates to True, or the last
operand if none are True:

.. code-block:: ipython

    In [36]: 0 or 456
    Out[36]: 456

.. nextslide::

On the other hand, ``not`` is a unary expression and inverts the boolean value
of its operand:

.. code-block:: ipython

    In [39]: not True
    Out[39]: False

    In [40]: not False
    Out[40]: True

Shortcutting
------------

Because of the return value of these keywords, you can write concise
statements:

::

                      if x is false,
    x or y               return y,
                         else return x

                      if x is false,
    x and y              return  x
                         else return y

                      if x is false,
    not x                return True,
                         else return False

Chaining
--------

.. code-block:: python

    a or b or c or d
    a and b and c and d


The first value that defines the result is returned


    (demo)


Conditional Expressions
-----------------------

This is a fairly common idiom:

.. code-block:: python

    if something:
        x = a_value
    else:
        x = another_value

In other languages, this can be compressed with a "ternary operator"::

    result = a > b ? x : y;

(this is the syntax from the C family)

In python, the same is accomplished with the ternary expression:

.. code-block:: python

    y = 5 if x > 2 else 3

PEP 308:
(http://www.python.org/dev/peps/pep-0308/)


Boolean Return Values
---------------------

Remember this puzzle from the CodingBat exercises?

.. code-block:: python

    def sleep_in(weekday, vacation):
        if weekday == True and vacation == False:
            return False
        else:
            return True

Though correct, that's not a particularly Pythonic way of solving the problem.

Here's a better solution:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return not (weekday == True and vacation == False)


And here's an even better one:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return (not weekday) or vacation


bools are integers?
-------------------

In python, the boolean types are subclasses of integer:

.. code-block:: ipython

    In [1]: True == 1
    Out[1]: True
    In [2]: False == 0
    Out[2]: True


And you can even do math with them (though it's a bit odd to do so):

.. code-block:: ipython

    In [6]: 3 + True
    Out[6]: 4

(demo)



