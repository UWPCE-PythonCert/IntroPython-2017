:orphan:

.. _notes_session03:

####################
Notes for Session 03
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Up today:

Amitkumar Chudasma

Daniel Wojciechowski

Eric V Adams

Tian Chuan Yen

Are you ready? We'll do them in the middle of the session.

Issues that came up during the week.
====================================

Separation of concerns
----------------------
From print_grid: if you are going to have separate functions, better for them to return a string, and then put all the printing in the calling function, on one place. That would make it more re-usable -- say you want to write to a file?

This is a tiny example of what's known as "separation of concerns"

Make use of symmetry
--------------------

nice trick:

.. code-block:: python

    def gene_line(char_a, char_b, n):
        line = char_a + ' ' + ((n - 1) // 2) * (char_b + ' ')
        line = line + char_a + line[::-1]

``is`` vs ``==``
----------------

In FizzBuzz, someone had code something like this:

```
if n % 3 is 0:
```

That works, but it's a "Bad Idea™"

"is" tests whether the objects are actually the same object -- not whether they have the same value. As you can easily have multiple objects that happen to have the same value, "is" will fail in the general case.

This works because cpython has an optimization called "interning" -- since small integers are used so often, the interpreter keeps a pool of them around to re-use, rather than creating multiple integer objects with the same value.

So "is" will work as a test for small integers, but not large ones:

.. code-block:: ipython

    In [65]: x = 5

    In [66]: y = 5

    In [67]: x is y
    Out[67]: True

    In [68]: x = 345678

    In [69]: y = 345678

    In [70]: x is y
    Out[70]: False

**NOTE:** This is also the case for small strings.

**Important:** This is an implementation detail. Do not count on it!


The Zen of Python
-----------------

Have you ever tried: ``import this`` ?




