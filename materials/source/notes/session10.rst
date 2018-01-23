
:orphan:

.. _notes_session10:

####################
Notes for Session 10
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Hiroyuki Takechi

Jacob Olsby

Larry Beausoleil


Issues that came up during the week.
====================================

When to make a method or property?
-----------------------------------

It is a good idea to make a property to access information in your class that requires "inside information", For example, in a Donor class:

.. code-block:: python

  @property
  def maxdonation(self):
      return max(self.donations)

This way, client code can get the maximum donation without knowing, or caring how the donations are stored in the class.

However, there is no need to create a property to "hide" something that is already part of the public API:

.. code-block:: python

  @property
  def namelength(self):
      return(len(self.name))

There is no point to this -- ``a_donor.name`` is expected to be a string -- so if you want to know how long it is, you can simply do:  ``len(a_donor.name)``

You *do* want to use properties to "hide" implementation details -- but the name attribute being a string is part of the API, not an implementation detail.

Anything else from OO mailroom?
-------------------------------


The Next Class
==============

Next quarter, we'll finish up the core of the Python language, then go into depth on some of the more advanced features of the language. Finally, we'll do a bit with using Python with other tools, such as databases.

Here's a Tentative Outline:

Functional Programming 2
------------------------

* Iterators and Iterables
* Itertools
* Functools


Functional Programming 3
------------------------

* Closures and Currying
* Generators
* Coroutines

Advanced Python Language Constructs
-----------------------------------

* Decorators
* Context Managers

* Meta Programming
* Meta Classes

Debugging & Logging
-------------------
* Logging module
* Syslog
* pdb/ipdb

Advanced Testing
----------------
* Linting
* Coverage
* Fixtures
* Mocking

Relational Databases
--------------------
* SQL
* ORMs
  * Normalization
  * Schema
* Sqlite
* Postgresql


NoSQL Databases
---------------
Object/Document, Key/Value and Graph Databases

* Schema vs “Schemaless”
* Mongo
* Redis
* Neo4j

Profiling & Performance
-----------------------

* Timing
* Profiling
* PyPy
* Cython

Concurrency & Async Programming
-------------------------------

* Concurrency
* Threading and Multiprocessing
* Message Queues
* Async
* Celery


Functional Programming
======================

The readings were a little, shall we say, sparse.

So I'll go over them now.

lambda
------

map, filter, reduce
-------------------

Want to try it with mailroom?

:ref:`exercise_mailroom_fp`

End of Quarter:
===============

We will review PRs through Sunday.

I will hold office hours one last time this Sunday as well.

**Anyone up for Celebratory Beer?**





