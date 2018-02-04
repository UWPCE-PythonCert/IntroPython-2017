:orphan:

.. _notes_session12:

############################
Notes for Quarter 2, class 2
############################


Packaging
=========

Where to put ``__init__.py`` files?
-----------------------------------

You only want to put ``init.py`` files in the "package" dirs -- that is, files with modules you want to import.

So not in a data dir, and not in the bin dir -- the bin dir does have python file(s), but they should be top-level scripts, so they will be run, but not imported.

Finding Data Files
------------------

* Putting data in a python file

* Using __file__

* Using setuptools pkg_resources

  http://setuptools.readthedocs.io/en/latest/pkg_resources.html#resourcemanager-api

Checking your package
---------------------

It can be pretty tricky to know if you package is doing the right thing.

While developing and testing, you want to use develop mode. But then if a file isn't getting included, you don't really notice, as it all still works.

Building the package
--------------------

You can use the ``build`` command to "build" the package. If there is not compiled code, it doesn't do much -- but it does copy everything into the build dir. So you can then look there and make sure it's right -- data files included, etc.

OF course, the final test is to do a full install, and then test. If your tests are included in the pacakge, you can run them with::

    $ pytest --pyargs pkg_name

This tells pytest to go into the package, look for its tests, and run them.

Source Distribution
-------------------

One of setuptools' features is the ability to build an "sdist"::

    $ python setup.py sdist

This builds a tarball of all the source, and puts it in the dist dir.

You can unpack that tarball and make sure it has all the files as well.

A complete package
------------------

Let's look at my Solution::

  $ git pull upstream master

``solutions/mailroom_pkg``

generators
==========

Any questions?

Let's look at my solutions:

``solutions/iterators_generators``

Scope and Closures and Currying
===============================

Some nifty functional features:

:ref:`closures`

Decorators
==========

Finally we learn what's under those @ symbols....

:ref:`decorators`





