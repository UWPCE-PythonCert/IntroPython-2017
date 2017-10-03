Decorators
==========

**A Short Reminder**

.. rst-class:: left

    Functions are things that generate values based on input (arguments).

    In Python, functions are first-class objects.

    This means that you can bind names to them, pass them around, etc., just like
    other objects.

    Because of this fact, you can write functions that take functions as
    arguments and/or return functions as values:

    .. code-block:: python

        def substitute(a_function):
            def new_function(*args, **kwargs):
                return "I'm not that other function"
            return new_function


A Definition
------------

There are many things you can do with a simple pattern like this one.
So many, that we give it a special name:

.. rst-class:: centered medium

**Decorator**

.. rst-class:: build centered

    "A decorator is a function that takes a function as an argument and
    returns a function as a return value."

    That's nice and all, but why is that useful?

An Example
----------

Imagine you are trying to debug a module with a number of functions like this
one:

.. code-block:: python

    def add(a, b):
        return a + b

.. rst-class:: build
.. container::

    You want to see when each function is called, with what arguments and
    with what result. So you rewrite each function as follows:

    .. code-block:: python

        def add(a, b):
            print("Function 'add' called with args: {}, {}".format(a, b) )
            result = a + b
            print("\tResult --> {}".format(result))
            return result

.. nextslide::

That's not particularly nice, especially if you have lots of functions
in your module.

Now imagine we defined the following, more generic *decorator*:

.. code-block:: python

    def logged_func(func):
        def logged(*args, **kwargs):
            print("Function {} called".format(func.__name__))
            if args:
                print("\twith args: {}".format(args))
            if kwargs:
                print("\twith kwargs: {}".format(kwargs))
            result = func(*args, **kwargs)
            print("\t Result --> {}".format(result))
            return result
        return logged

(demo)

.. nextslide::

We could then make logging versions of our module functions:

.. code-block:: python

    logging_add = logged_func(add)

Then, where we want to see the results, we can use the logged version:

.. code-block:: ipython

    In [37]: logging_add(3, 4)
    Function 'add' called
        with args: (3, 4)
         Result --> 7
    Out[37]: 7

.. rst-class:: build
.. container::

    This is nice, but we have to call the new function wherever we originally
    had the old one.

    It'd be nicer if we could just call the old function and have it log.

.. nextslide::

Remembering that you can easily rebind symbols in Python using *assignment
statements* leads you to this form:

.. code-block:: python

    def logged_func(func):
        # implemented above

    def add(a, b):
        return a + b
    add = logged_func(add)

.. rst-class:: build
.. container::

    And now you can simply use the code you've already written and calls to
    ``add`` will be logged:

    .. code-block:: ipython

        In [41]: add(3, 4)
        Function 'add' called
            with args: (3, 4)
             Result --> 7
        Out[41]: 7

Syntax
------

Rebinding the name of a function to the result of calling a decorator on that
function is called **decoration**.

Because this is so common, Python provides a special operator to perform it
more *declaratively*: the ``@`` operator
-- I told you I'd eventually explain what was going on under the hood with
that wierd `@` symbol:

.. code-block:: python

    def add(a, b):
        return a + b
    add = logged_func(add)

    @logged_func
    def add(a, b):
        return a + b

The declarative form (called a decorator expression) is far more common,
but both have the identical result, and can be used interchangeably.

(demo)

Callables
---------

Our original definition of a *decorator* was nice and simple, but a tiny bit
incomplete.

In reality, decorators can be used with anything that is *callable*.

Remember from last week, a *callable* is a function, a method on a class,
or a class that implements the ``__call__`` special method.

So in fact the definition should be updated as follows:

.. rst-class:: centered medium

A decorator is a callable that takes a callable as an argument and
returns a callable as a return value.

An Example
----------

Consider a decorator that would save the results of calling an expensive
function with given arguments:

.. code-block:: python

    class Memoize:
    """
    memoize decorator from avinash.vora
    http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    """
    def __init__(self, function):  # runs when memoize class is called
        self.function = function
        self.memoized = {}

    def __call__(self, *args):  # runs when memoize instance is called
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]

.. nextslide::

Let's try that out with a potentially expensive function:

.. code-block:: ipython

    In [56]: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in xrange(n))
       ....:

    In [57]: sum2x(10000000)
    Out[57]: 99999990000000

    In [58]: sum2x(10000000)
    Out[58]: 99999990000000

It's nice to see that in action, but what if we want to know *exactly*
how much difference it made?

Nested Decorators
-----------------

You can stack decorator expressions.  The result is like calling each
decorator in order, from bottom to top:

.. code-block:: python

    @decorator_two
    @decorator_one
    def func(x):
        pass

    # is exactly equal to:
    def func(x):
        pass
    func = decorator_two(decorator_one(func))

.. nextslide::

Let's define another decorator that will time how long a given call takes:

.. code-block:: python

    import time
    def timed_func(func):
        def timed(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print("time expired: {}".format(elapsed))
            return result
        return timed

.. nextslide::

And now we can use this new decorator stacked along with our memoizing
decorator:

.. code-block:: ipython

    In [71]: @timed_func
       ....: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in xrange(n))
    In [72]: sum2x(10000000)
    time expired: 0.997071027756
    Out[72]: 99999990000000
    In [73]: sum2x(10000000)
    time expired: 4.05311584473e-06
    Out[73]: 99999990000000


Examples from the Standard Library
----------------------------------

It's going to be a lot more common for you to use pre-defined decorators than
for you to be writing your own.

We've seen a few already:

.. nextslide::

For example, ``@staticmethod`` and ``@classmethod`` can also be used as simple
callables, without the nifty decorator expression:

.. code-block:: python

    # the way we saw last week:
    class C(object):
        @staticmethod
        def add(a, b):
            return a + b

Is exactly the same as:

.. code-block:: python

    class C(object):
        def add(a, b):
            return a + b
        add = staticmethod(add)

Note that the "``def``" binds the name ``add``, then the next line
rebinds it.


.. nextslide::

The ``classmethod()`` builtin can do the same thing:

.. code-block:: python

    # in declarative style
    class C(object):
        @classmethod
        def from_iterable(cls, seq):
            # method body

    # in imperative style:
    class C(object):
        def from_iterable(cls, seq):
            # method body
        from_iterable = classmethod(from_iterable)


property()
-----------

Remember the property() built in?

Perhaps most commonly, you'll see the ``property()`` builtin used this way.

Two weeks ago we saw this code:

.. code-block:: python

    class C(object):
        def __init__(self):
            self._x = None
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x

.. nextslide::

But this could also be accomplished like so:

.. code-block:: python

    class C(object):
        def __init__(self):
            self._x = None
        def getx(self):
            return self._x
        def setx(self, value):
            self._x = value
        def delx(self):
            del self._x
        x = property(getx, setx, delx,
                     "I'm the 'x' property.")


``Examples/Session10/property_ugly.py``


.. nextslide::

Note that in this case, the decorator object returned by the property decorator
itself implements additional decorators as attributes on the returned method
object. So you could actually do this:


.. code-block:: python

    class C(object):
        def __init__(self):
            self._x = None
        def x(self):
            return self._x
        x = property(x)
        def _set_x(self, value):
            self._x = value
        x = x.setter(_set_x)
        def _del_x(self):
            del self._x
        x = x.deleter(_del_x)

But that's getting really ugly!
