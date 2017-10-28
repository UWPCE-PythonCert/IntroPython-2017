:orphan:

.. _notes_session04:

####################
Notes for Session 04
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

The ones we didn't get to last week:

Eric V Adams

Tian Chuan Yen

And Scheduled for today:

Brian Warn

Guillaume R Thomas


Shibata Hiroyuki


Let's do the folks from last week right now. And the others in the middle of the session.

Issues that came up during the week.
====================================

Mutable default parameters
--------------------------

This is a real "gotcha" in Python. One of you wrote a non-recursive solution to the sum_series problem. It worked great -- EXCEPT if it got called more than once! Any idea what the problem is?

.. code-block:: python

    def sum_series(nth=1, sequence=[0,1]):
        """
        Generate a list of sums given a seed and return the Nth number.
        """
        for i in range(2, nth):
            sequence.append(sequence[i-2] + sequence[i-1])
        return sequence[nth-1]

So this uses the logic of starting out with the first two values in the series, and then looping to build up the series from there.

And [0, 1] is set as a default to start the series off -- the start of the Fibonacci series.  So if you pass in only one argument, you should get the Fibonacci number:

Remember that the start of the Fibonacci series is::

  0, 1, 1, 2, 3, 5, 8, 13, ...

What happens when you run this code:

.. code-block:: python

    In [21]: sum_series(5)
    Out[21]: 3

All good.

    In [22]: sum_series(6)
    Out[22]: 1
    # WTF???

The issue is that:

Default Arguments get evaluated **when the function is defined**. So every time the function is called, it will use the *same* list! Each time adding more and more to the list.

Let's explore that some more, and some solutions....

``str(input(...))``???
----------------------

Minor issue, but a number of you have written code like:

.. code-block:: python

    answer = str(input("some prompt > "))

But ``input()`` always returns a string -- no need to wrap a call to ``str()`` around it.

You may have seen code like this on the web, as ``input()`` behaves differently in Python 2.

recursion in an interactive loop
--------------------------------

not a great idea!

you can do something like:

.. code-block:: python

    def mainloop():
        while True:
            ans = input("A question > ")
            ....
            if ans == "again"
                mainloop()

Let's look at this:

``examples/session04/recursive_mainloop.py``

(do a ``git pull upstream master`` if you don't see it.)


Deleting from a list while looping through it
---------------------------------------------

This may seem like an obvious way to filter a list:

.. code-block:: python

  for item in a_list:
      if something:
          a_list.remove(item)

But it turns out that removing stuff from a list while looping through can make a mess of things. Let's try it:

.. code-block:: python

  a_list = list(range(10))
  print(a_list)
  # loop to remove everything...
  for item in a_list:
      if item: # is it an nonzero number?
          a_list.remove(item)
  print(a_list)

Let's run this code, and see what we get.

``examples/session04/deleting_in_loop.py``

What if you add stuff to a list while looping?

Adding up immutables in loops
-----------------------------

Mostly about strings, but it's an issue for numbers, too:



In [8]: l
Out[8]: ['this', 'that', 'the', 'other', 'thing']

In [9]: sum(l, "")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-327c710c973b> in <module>()
----> 1 sum(l, "")

TypeError: sum() can't sum strings [use ''.join(seq) instead]

In [10]: def use_sum(seq):
    ...:     return sum(seq)
    ...:

In [11]: def use_loop(seq):
    ...:     val = 0
    ...:     for i in seq:
    ...:         val += i
    ...:     return val
    ...:

In [12]: seq = list(range(100))

In [13]: use_sum(seq)
Out[13]: 4950

In [14]: use_loop(seq)
Out[14]: 4950

In [15]: seq = list(range(10000))

In [16]: % timeit use_sum(seq)
10000 loops, best of 3: 73.3 µs per loop

In [17]: % timeit use_loop(seq)
1000 loops, best of 3: 385 µs per loop


``if __name__ == "__main__":``
------------------------------

This can be confusing, but one key note:

Put as little as possible in this block -- the idea is that most of your code can be run / used as a module, and *only* the code that has to be run in a script goes here. Often that is simply something like:

.. code-block:: python

    if __name__ == "__main__":
        main_function()
