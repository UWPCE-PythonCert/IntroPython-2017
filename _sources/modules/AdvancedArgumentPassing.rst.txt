Advanced Argument Passing
=========================

This is a very, very nifty Python feature -- it really lets you write dynamic programs.

Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x=0, y=0, z=0):
            print(x,y,z)
       .....:
    In [152]: fun(1,2,3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(z=3, y=2)
    0 2 3


.. nextslide::


A Common Idiom:

.. code-block:: python

    def fun(x, y=None):
        if y is None:
            do_something_different
        go_on_here


.. nextslide::

Can set defaults to variables

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4


.. nextslide::

Defaults are evaluated when the function is defined

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4
    In [159]: y = 6
    In [160]: fun()
    x is: 4

This is a **very** important point.


Function arguments in variables
-------------------------------

When a function is called, its arguments are really just:

* a tuple (positional arguments)
* a dict (keyword arguments)

.. code-block:: python

    def f(x, y, w=0, h=0):
        print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))

    position = (3,4)
    size = {'h': 10, 'w': 20}

    >>> f(*position, **size)
    position: 3, 4 -- shape: 20, 10


Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    def f(*args, **kwargs):
        print("the positional arguments are:", args)
        print("the keyword arguments are:", kwargs)

    In [389]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the keyword arguments are: {'this': 5, 'that': 7}

This can be very powerful...

Passing a dict to str.format()
-------------------------------

Now that you know that keyword args are really a dict,
you know how this nifty trick works:

The string ``format()`` method takes keyword arguments:

.. code-block:: ipython

    In [24]: "My name is {first} {last}".format(last="Barker", first="Chris")
    Out[24]: 'My name is Chris Barker'

Build a dict of the keys and values:

.. code-block:: ipython

    In [25]: d = {"last":"Barker", "first":"Chris"}

And pass to ``format()``with ``**``

.. code-block:: ipython

    In [26]: "My name is {first} {last}".format(**d)
    Out[26]: 'My name is Chris Barker'

Kinda handy for the dict lab, eh?

This:

.. code-block:: ipython

  print("{} is from {}, and he likes "
        "{} cake, {} fruit, {} salad, "
        "and {} pasta.".format(food_prefs["name"],
                               food_prefs["city"],
                               food_prefs["cake"],
                               food_prefs["fruit"],
                               food_prefs["salad"],
                               food_prefs["pasta"]))

Becomes:

.. code-block:: ipython

  print("{name} is from {city}, and he likes "
        "{cake} cake, {fruit} fruit, {salad} salad, "
        "and {pasta} pasta.".format(**food_prefs))

LAB
----

Time to play with all this to get a feel for it.

:ref:`exercise_args_kwargs_lab`

This is not all that clearly specified.  The goal is for you to
experiment with various ways to define and call functions so that
you understand what is possible and what happens with each call.
