.. _exercise_unit_testing:

############################
Introduction To Unit Testing
############################

Test Driven Development
-----------------------

in the examples/Session06 dir, try::

  $ py.test test_cigar_party

What we've just done here is the first step in what is called:


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

  $ py.test test_cigar_party.py

Copy both of these files into your home directory in the repo.

Develop ``cigar_party.py`` until all the tests pass.


  Pick an example from codingbat:

  ``http://codingbat.com``

  Do a bit of test-driven development on it:

   * run something on the web site.
   * write a few tests using the examples from the site.
   * then write the function, and fix it 'till it passes the tests.

  Do at least two of these...

