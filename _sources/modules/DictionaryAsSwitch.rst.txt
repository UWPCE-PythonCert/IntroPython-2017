Dictionary as Switch
====================

Python does not have a switch/case statement.  Why not?

https://www.python.org/dev/peps/pep-3103/

What to use instead of "switch-case"?

Switch case
-----------

Many languages have a "switch-case" construct::

    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };

How do you say this in Python?

``if-elif`` chains
------------------

The obvious way to say it is a chain of ``elif`` statements:

.. code-block:: python

    if argument ==  0:
        return "zero"
    elif argument == 1:
        return "one"
    elif argument == 2:
        return "two"
    else:
        return "nothing"

And there is nothing wrong with that, but....

Dict as switch
--------------

The ``elif`` chain is neither elegant nor efficient. There are a number of ways to say it in python -- but one elegant one is to use a dict:

.. code-block:: python

    arg_dict = {0:"zero", 1:"one", 2: "two"}
        dict.get(argument, "nothing")

Simple, elegant and fast.

You can do a dispatch table by putting functions as the value.

Example: Chris' mailroom2 solution.

Switch with functions
---------------------

What would this be like if you used functions instead? Think of the possibilities.

.. code-block:: ipython

    In [11]: def my_zero_func():
    return "I'm zero"

    In [12]: def my_one_func():
        return "I'm one"

    In [13]: switch_func_dict = {
        0: my_zero_func,
        1: my_one_func,
    }

    In [14]: switch_func_dict.get(0)()
    Out[14]: "I'm zero"

