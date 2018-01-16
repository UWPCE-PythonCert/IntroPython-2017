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

