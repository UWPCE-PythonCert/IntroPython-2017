.. _closures:


##############################
Closures and Function Currying
##############################

Defining specialized functions on the fly.


Functions within Functions
--------------------------

TODO: Preface this topic with basic scope rules, specifically that you can define functions within functions.  -- rriehle

and add nonlocal!

Closures
--------

"Closures" and "Currying" are cool CS terms for what is really just defining functions on the fly. You can find a "proper" definition here:

http://en.wikipedia.org/wiki/Closure_(computer_programming)

But I even have trouble following that.

So let's go straight to an example:


.. code-block:: python

    def counter(start_at=0):
        count = [start_at]
        def incr():
            count[0] += 1
            return count[0]
        return incr

What's going on here?

We have stored the ``start_at`` value in a list.

Then defined a function, ``incr`` that adds one to the value in the list, and returns that value.

[ Quiz: why is it: ``count = [start_at]``, rather than just ``count=start_at`` ]


So what type of object do you get when you call ``counter()``?

.. code-block:: ipython

    In [37]: c = counter(start_at=5)

    In [38]: type(c)
    Out[38]: function

So we get a function back -- makes sense. The ``def`` defines a function, and that function is what's getting returned.

Being a function, we can, of course, call it:

.. code-block:: ipython

    In [39]: c()
    Out[39]: 6

    In [40]: c()
    Out[40]: 7

Each time is it called, it increments the value by one.


But what happens if we call ``counter()`` multiple times?

.. code-block:: ipython

    In [41]: c1 = counter(5)

    In [42]: c2 = counter(10)

    In [43]: c1()
    Out[43]: 6

    In [44]: c2()
    Out[44]: 11

So each time ``counter()`` is called, a new function is created. And that function has its own copy of the ``count`` object. This is what makes in a "closure" -- it carries with it the scope in which is was created.

The returned ``incr`` function is a "curried" function -- a function with some parameters pre-specified.


``functools.partial``
---------------------

The ``functools`` module in the standard library provides utilities for working with functions:

https://docs.python.org/3.5/library/functools.html

Creating a curried function turns out to be common enough that the ``functools.partial`` function provides an optimized way to do it:

What functools.partial does is:

 * Makes a new version of a function with one or more arguments already filled in.
 * The new version of a function documents itself.

Example:

.. code-block:: python

    def power(base, exponent):
        """returns based raised to the give exponent"""
        return base ** exponent

Simple enough. but what if we wanted a specialized ``square`` and ``cube`` function?

We can use ``functools.partial`` to *partially* evaluate the function, giving us a specialized version:

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

Real world Example
------------------

I was writing some code to compute the concentration of a contaminant in a river, as it was reduced exponential decay, defined by a half-life:

https://en.wikipedia.org/wiki/Half-life

So I wanted a function that would compute how much the concentration would reduces as a function of time -- that is:

.. code-block:: python

    def scale(time):
        return scale_factor

The trick is, that how much the concentration would be reduced depends on teh half life. And for a given material, and given flow conditions in teh river, that half life is pre-determined as:

scale = 0.5 ** (time / (half_life))

So to compute the scale, I could pass that half-life in each time I called the function:

.. code-block:: python

    def scale(time, half_life):
        return 0.5 ** (time / (half_life))

But this is a bit klunky -- I need to keep passing that half_life around, even though it isn't changing. And there are places, like ``map`` that require a function that takes only one argument!

What if I could create a function, on the fly, that had a particular half-life "baked in"?

*Enter Currying* -- Currying is a technique where you reduce the number of parameters that function takes, creating a specialized function with one or more of the original parameters set to a particular value. Here is that technique, applied to the half-life decay problem:

.. code-block:: python

    def get_scale_fun(half_life):
        def half_life(time)
            return 0.5 ** (time / half_life)
        return half_life

**NOTE:** This is simple enough to use a lambda for a bit more compact code:

.. code-block:: python

    def get_scale_fun(half_life):
        return lambda time: 0.5 ** (time / half_life)

Using a Curried Function
........................

Create a scale function with a half-life or one hour:

.. code-block:: ipython

    In [8]: scale = get_scale_fun(1)

    In [9]: [scale(t) for t in range(7)]
    Out[9]: [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]

The value is reduced by half every hour.

Now create one with a half life of 2 hours:

.. code-block:: ipython

    In [10]: scale = get_scale_fun(2)

    In [11]: [scale(t) for t in range(7)]
    Out[11]:
    [1.0,
     0.7071067811865476,
     0.5,
     0.3535533905932738,
     0.25,
     0.1767766952966369,
     0.125]

And the value is reduced by half every two hours...

And it can be used with ``map``, too:

.. code-block:: ipython

    In [13]: list(map(scale, range(7)))
    Out[13]:
    [1.0,
     0.7071067811865476,
     0.5,
     0.3535533905932738,
     0.25,
     0.1767766952966369,
     0.125]









