
.. _unit_testing:

############
Unit Testing
############

You've already seen a very basic testing strategy.

You've written some tests using that strategy.

These tests were pretty basic, and a bit awkward in places (testing error
conditions in particular).

    **It gets better**

Test Frameworks
---------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.


* They are run only when the file is executed
* They are always run when the file is executed
* You can't do anything else when the file is executed without running tests.


    This is not optimal.

    Python provides testing systems to help.


Standard Library: ``unittest``
------------------------------

The original testing system in Python.

``import unittest``

More or less a port of ``JUnit`` from Java

A bit verbose: you have to write classes & methods

(And we haven't covered that yet!)

But here's a bit of an introduction, as you will see this in others' code.

And seeing how verbose it can be will help you appreciate other options.


Using ``unittest``
------------------

To use ``unittest``, you need to write subclasses of the ``unittest.TestCase`` class:

.. code-block:: python

    # in test.py
    import unittest

    class MyTests(unittest.TestCase):

        def test_tautology(self):
            self.assertEqual(1, 1)

Then you run the tests by using the ``main`` function from the ``unittest``
module:

.. code-block:: python

    # in test.py
    if __name__ == '__main__':
        unittest.main()


Testing Your Code
-----------------

This way, you can write your code in one file and test it from another:

in ``my_mod.py``:

.. code-block:: python

    def my_func(val1, val2):
        return val1 * val2

in ``test_my_mod.py``:

.. code-block:: python

    import unittest
    from my_mod import my_func


    class MyFuncTestCase(unittest.TestCase):
        def test_my_func(self):
            test_vals = (2, 3)
            expected = test_vals[0] * test_vals[1]
            actual = my_func(*test_vals)
            self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()


Advantages of ``unittest``
--------------------------


    The ``unittest`` module is pretty full featured

    It comes with the standard Python distribution, no installation required.

    It provides a wide variety of assertions for testing all sorts of situations.

    It allows for a setup and tear down workflow both before and after all tests and before and after each test.

    It's well known and well understood.


Disadvantages of ``unittest``
-----------------------------

    It's Object Oriented, and quite "heavyweight".

      - modeled after Java's ``JUnit`` and it shows...

    It uses the framework design pattern, so knowing how to use the features means learning what to override.

    Needing to override means you have to be cautious.

    Test discovery is both inflexible and brittle.

    And there is no built-in parameterized testing.


Other Options
-------------

There are several other options for running tests in Python.

* `Nose`: https://nose.readthedocs.org/

* `pytest`: http://pytest.org/latest/

* ... (many frameworks supply their own test runners: e.g. django)

Nose was the most common test runner when I first started learning testing, but it has been in maintaince mode for a while.

pytest has become the defacto standard for test runners those that want a and a more "pythonic" test framework.

It is very capable and widely used.

For a great description of the strengths of pytest, see:

`The Cleaning Hand of Pytest <https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684>`_

Installing ``pytest``
---------------------

The first step is to install the package:

.. code-block:: bash

    $ python3 -m pip install pytest

Once this is complete, you should have a ``pytest`` command you can run
at the command line:

.. code-block:: bash

    $ pytest

If you have any tests in your repository, that will find and run them.

    **Do you?**

Pre-existing Tests
------------------

Let's take a look at some examples.

in ``IntroPython-2017\Examples\Session06``

.. code-block:: bash

  $ pytest

You can also run pytest on a particular test file:

.. code-block:: bash

  $ pytest test_random_unitest.py

The results you should have seen when you ran ``pytest`` above come
partly from these files.

Take a few minutes to look these files over.

``test_random_unitest.py`` contains the tests for some of the functions in the built in``random`` module. You really don't need to test Python's built in modules -- they are already tested! This is just to demonstrate the process.


What is Happening Here?
-----------------------

You should have gotten results that look something like this::

    MacBook-Pro:Session06 Chris$ pytest test_random_unitest.py
    ============================= test session starts ==============================
    platform darwin -- Python 3.6.2, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
    rootdir: /Users/Chris/PythonStuff/UWPCE/IntroPython-2017/examples/Session06, inifile:
    collected 3 items

    test_random_unitest.py ...

    =========================== 3 passed in 0.02 seconds ===========================


When you run the ``pytest`` command, ``pytest`` starts in your current
working directory and searches the file system for things that might be tests.

It follows some simple rules:

* Any python file that starts with ``test_`` or ``_test`` is imported.

* Any functions in them that start with ``test_`` are run as tests.

* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.

( don't worry about "classes" part just yet ;-) )

* Any ``unitest`` test cases are run.

pytest
------

This test running framework is simple, flexible and configurable.

Read the documentation for more information:

http://pytest.org/latest/getting-started.html#getstarted

It will run ``unittest`` tests for you, so an be used as a test runner.

But in addition to finding and running tests, it makes writing tests simple, and provides a bunch of nifty utilities to support more complex testing.


Test Driven Development
-----------------------

Download these files, and save them in your own students directory in the class repo:

:download:`test_cigar_party.py <../examples/testing/test_cigar_party.py>`
and:
:download:`cigar_party.py <../examples/testing/cigar_party.py>`

then, in dir where you put the files, run::

  $ pytest test_cigar_party.py

You will get a LOT of test failures!

What we've just done here is the first step in what is called:

  **Test Driven Development**.

The idea is that you write the tests first, and then write the code that passes the tests. In this case, the writing the tests part has been done for you:

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run the tests is a goad to you to write the code that fixes these tests.

The tests all failed  because ``cigar_party()`` looks like:

.. code-block:: python

  def cigar_party(cigars, is_weekend):
      pass

A totally do nothing function!

Put real code in  ``cigar_party.py`` until all the tests pass.

When the tests pass -- you are done! That's the beauty of test-drive development.

Trying it yourself
------------------

Try it a bit more, writing the tests yourself:

Pick an example from codingbat:

  `codingbat <http://codingbat.com>`_

Do a bit of test-driven development on it:

   * run something on the web site.
   * write a few tests using the examples from the site.
   * then write the function, and fix it 'till it passes the tests.

Do at least two of these...


