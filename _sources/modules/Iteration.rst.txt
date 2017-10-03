.. _iteration:

#########
Iteration
#########

Repetition, Repetition, Repetition, Repe...


For Loops
=========

We've seen simple iteration over a sequence with ``for ... in``:

.. code-block:: ipython

    In [170]: for x in "a string":
       .....:         print(x)
       .....:
    a
    s
    t
    r
    i
    n
    g


No Indexing Required
--------------------

Contrast this with other languages, where you must build and use an ``index``:

.. code-block:: javascript

    for(var i = 0; i < arr.length; i++) {
        var value = arr[i];
        alert(i + ") " + value);

If you *do* need an index, you can use ``enumerate``:

.. code-block:: ipython

    In [140]: for idx, letter in enumerate('Python'):
       .....:     print(idx, letter, end=' ')
       .....:
    0 P 1 y 2 t 3 h 4 o 5 n


``range`` and ``for`` Loops
---------------------------

The ``range`` builtin is useful for looping a known number of times:

.. code-block:: ipython

    In [171]: for i in range(5):
       .....:     print(i)
       .....:
    0
    1
    2
    3
    4

But you don't really need to do anything at all with ``i``

In fact, it's a common convention to make this clear with a "nothing" name:

.. code-block:: ipython

    In [21]: for __ in range(5):
       ....:     print("*")
       ....:
    *
    *
    *
    *
    *


.. nextslide:: No Namespace

Be alert that a loop does not create a local namespace:

.. code-block:: ipython

    In [172]: x = 10
    In [173]: for x in range(3):
       .....:     pass
       .....:
    In [174]: x
    Out[174]: 2


.. nextslide:: Loop Control

Sometimes you want to interrupt or alter the flow of control through a loop.

Loops can be controlled in two ways, with ``break`` and ``continue``


.. nextslide:: Break

The ``break`` keyword will cause a loop to immediately terminate:

.. code-block:: ipython

    In [141]: for i in range(101):
       .....:     print(i)
       .....:     if i > 50:
       .....:         break
       .....:
    0 1 2 3 4 5... 46 47 48 49 50 51

.. nextslide:: Continue

The ``continue`` keyword will skip later statements in the loop block, but
allow iteration to continue:

.. code-block:: ipython

    In [143]: for in in range(101):
       .....:     if i > 50:
       .....:         break
       .....:     if i < 25:
       .....:         continue
       .....:     print(i, end=' ')
       .....:
       25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

.. nextslide:: else

For loops can also take an optional ``else`` block.

Executed only when the loop exits normally (not via break):

.. code-block:: ipython

    In [147]: for x in range(10):
       .....:     if x == 11:
       .....:         break
       .....: else:
       .....:     print('finished')
    finished
    In [148]: for x in range(10):
       .....:     if x == 5:
       .....:         print(x)
       .....:         break
       .....: else:
       .....:     print('finished')
    5

This is a really nice unique Python feature!

While Loops
===========

While loops are different -- they are not for iterating over a collection, but rather for repeating something an unknown number of times -- and maybe even forever.

The ``while`` keyword is for when you don't know how many loops you need.

It continues to execute the body until condition is not ``True``::

    while a_condition:
       some_code
       in_the_body

.. nextslide:: ``while`` vs. ``for``

``while``  is more general than ``for``

-- you can always express ``for`` as ``while``, but not always vice-versa.

``while``  is more error-prone -- requires some care to terminate

loop body must make progress, so condition can become ``False``

potential error -- infinite loops:

.. code-block:: python

    i = 0;
    while i < 5:
        print(i)


.. nextslide:: Terminating a while Loop

Use ``break``:

.. code-block:: ipython

    In [150]: while True:
       .....:     i += 1
       .....:     if i > 10:
       .....:         break
       .....:     print(i)
       .....:
    1 2 3 4 5 6 7 8 9 10

.. nextslide:: Terminating a while Loop

Set a flag:

.. code-block:: ipython

    In [156]: import random
    In [157]: keep_going = True
    In [158]: while keep_going:
       .....:     num = random.choice(range(5))
       .....:     print(num)
       .....:     if num == 3:
       .....:         keep_going = False
       .....:
    3

.. nextslide:: Terminating a While Loop

Use a condition:

.. code-block:: ipython

    In [161]: while i < 10:
       .....:     i += random.choice(range(4))
       .....:     print(i)
       .....:
    0 0 2 3 4 6 8 8 8 9 12


Similarities
------------

Both ``for`` and ``while`` loops can use ``break`` and ``continue`` for
internal flow control.

Both ``for`` and ``while`` loops can have an optional ``else`` block

In both loops, the statements in the ``else`` block are only executed if the
loop terminates normally (no ``break``)

