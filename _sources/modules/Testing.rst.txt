Testing
=======

.. rst-class:: build left
.. container::

    You've already seen a very basic testing strategy.

    You've written some tests using that strategy.

    These tests were pretty basic, and a bit awkward in places (testing error
    conditions in particular).

    .. rst-class:: centered large

    **It gets better**

Test Runners
------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.

.. rst-class:: build

* They are run only when the file is executed
* They are always run when the file is executed
* You can't do anything else when the file is executed without running tests.

.. rst-class:: build
.. container::

    This is not optimal.

    Python provides testing systems to help.


Standard Library: ``unittest``
------------------------------

The original testing system in Python.

``import unittest``

More or less a port of ``Junit`` from Java

A bit verbose: you have to write classes & methods

(And we haven't covered that yet!)


Using ``unittest``
------------------

You write subclasses of the ``unittest.TestCase`` class:

.. code-block:: python

    # in test.py
    import unittest

    class MyTests(unittest.TestCase):
        def test_tautology(self):
            self.assertEquals(1, 1)

Then you run the tests by using the ``main`` function from the ``unittest``
module:

.. code-block:: python

    # in test.py
    if __name__ == '__main__':
        unittest.main()

.. nextslide:: Testing Your Code

This way, you can write your code in one file and test it from another:

.. code-block:: python

    # in my_mod.py
    def my_func(val1, val2):
        return val1 * val2

    # in test_my_mod.py
    import unittest
    from my_mod import my_func

    class MyFuncTestCase(unittest.TestCase):
        def test_my_func(self):
            test_vals = (2, 3)
            expected = reduce(lambda x, y: x * y, test_vals)
            actual = my_func(*test_vals)
            self.assertEquals(expected, actual)

    if __name__ == '__main__':
        unittest.main()

.. nextslide:: Advantages of ``unittest``

.. rst-class:: build
.. container::

    The ``unittest`` module is pretty full featured

    It comes with the standard Python distribution, no installation required.

    It provides a wide variety of assertions for testing all sorts of situations.

    It allows for a setup and tear down workflow both before and after all tests and before and after each test.

    It's well known and well understood.

.. nextslide:: Disadvantages:

.. rst-class:: build
.. container::


    It's Object Oriented, and quite "heavyweight".

      - modeled after Java's ``junit`` and it shows...

    It uses the framework design pattern, so knowing how to use the features
    means learning what to override.

    Needing to override means you have to be cautious.

    Test discovery is both inflexible and brittle.

    And there is no built-in parameterized testing.

Other Options
-------------

There are several other options for running tests in Python.

* `Nose`: https://nose.readthedocs.org/

* `pytest`: http://pytest.org/latest/

* ... (many frameworks supply their own test runners: e.g. django)

Both are very capable and widely used.

Installing ``pytest``
---------------------

The first step is to install the package:

.. code-block:: bash

    $ python3 -m pip install pytest

Or better, use a virtualenv:

.. code-block:: bash

    $ mkvirtualenv testing
    $ pip install pytest

Once this is complete, you should have a ``py.test`` command you can run
at the command line:

.. code-block:: bash

    $ py.test

If you have any tests in your repository, that will find and run them.

.. rst-class:: build
.. container::

    **Do you?**

Pre-existing Tests
------------------

Let's take a look at some examples.

in ``IntroPython2016\Examples\Session06``

.. code-block:: bash

  $ py.test

You can also run py.test on a particular test file:

.. code-block:: bash

  $ py.test test_random_unitest.py

The results you should have seen when you ran ``py.test`` above come
partly from these files.

Let's take a few minutes to look these files over.

What is Happening Here?
-----------------------

When you run the ``py.test`` command, ``pytest`` starts in your current
working directory and searches the filesystem for things that might be tests.

It follows some simple rules:

* Any python file that starts with ``test_`` or ``_test`` is imported.

* Any functions in them that start with ``test_`` are run as tests.

* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.

( don't worry about "classes" part just yet ;-) )

pytest
------

This test running framework is simple, flexible and configurable.

Read the documentation for more information:

http://pytest.org/latest/getting-started.html#getstarted

It will run ``unittest`` tests for you.

But in addition to finding and running tests, it makes writting tests simple, and provides a bunch of nifty utilities to support more complex testing.

Test Driven Development
-----------------------

in the exercises dir, try::

  $ py.test test_cigar_party

What we've just done here is the first step in what is called:

.. rst-class:: centered

  **Test Driven Development**.

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run our tests is a goad to us to write the code that fixes these tests.

Let's do that next!

Test Driven development
-----------------------

Open:

``exercises/test_cigar_party.py``

and:

``exercises/cigar_party.py``

and run::

  $ py.teset test_cigar_party.py

Copy both of these files into your home directory in the repo.

Develop ``cigar_party.py`` until all the tests pass.


LAB
---

.. rst-class:: left

  Pick an example from codingbat:

  ``http://codingbat.com``

  Do a bit of test-driven development on it:

   * run something on the web site.
   * write a few tests using the examples from the site.
   * then write the function, and fix it 'till it passes the tests.

  Do at least two of these...
