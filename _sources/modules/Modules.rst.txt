.. _modules_and_namespaces:

#######################################
Code Structure, Modules, and Namespaces
#######################################


**How to get what you want when you want it.**


Code Structure
==============

In Python, the structure of your code is determined by whitespace.

How you *indent* your code determines how it is structured

::

    block statement:
        some code body
        some more code body
        another block statement:
            code body in
            that block

The colon that terminates a block statement is also important...

One-liners
----------

You can put a one-liner after the colon:

.. code-block:: ipython

    In [167]: x = 12
    In [168]: if x > 4: print(x)
    12

But this should only be done if it makes your code **more** readable.


Spaces vs. Tabs
---------------

Whitespace is important in Python.

An indent *could* be:

* Any number of spaces
* A tab
* A mix of tabs and spaces:

If you want anyone to take you seriously as a Python developer:

.. rst-class:: centered

**Always use four spaces -- really!**

`(PEP 8) <http://legacy.python.org/dev/peps/pep-0008/>`_

Spaces Elsewhere
----------------

Other than indenting -- space doesn't matter, technically.

.. code-block:: python

    x = 3*4+12/func(x,y,z)
    x = 3*4 + 12 /   func (x,   y, z)

These will give the exact same results.

But you should strive for proper style.  Read PEP 8 and install a linter in your editor.

Modules and Packages
====================

Python is all about *namespaces* --  the "dots"

``name.another_name``

The "dot" indicates that you are looking for a name in the *namespace* of the given object. It could be:

* name in a module
* module in a package
* attribute of an object
* method of an object


Modules
-------

A module is simply a namespace.

It might be a single file, or it could be a collection of files that define a shared API.

But in the common and simplest case, a single file is a single module.

So you can think of the files you write that end in ``.py`` as modules.

Packages
--------

A package is a module with other modules in it.

On a filesystem, this is represented as a directory that contains one or more``.py`` files, one of which **must** be called ``__init__.py``.

When you have a package, you can import the package, or any of the modules inside it.

importing modules
-----------------

There are a few ways to import modules:

.. code-block:: python

    import modulename
    from modulename import this, that
    import modulename as a_new_name
    from modulename import this as that

    (demo)


Importing from packages
-----------------------

.. code-block:: python

    import packagename.modulename
    from packagename.modulename import this, that
    from package import modulename

    (demo)

Here's a nice reference:

http://effbot.org/zone/import-confusion.htm

import \* ?
-----------

.. code-block:: python

    from modulename import *

.. rst-class:: centered large

**Don't do this!**


``import``
----------

When you import a module, or a symbol from a module, the Python code is *compiled* to **bytecode**.

The result is a ``module.pyc`` file.

Then after compiling, all the code in the module is run **at the module scope**.

For this reason, it is good to avoid module-scope statements that have global side-effects.


Re-import
----------

The code in a module is NOT re-run when imported again

It must be explicitly reloaded to be re-run

.. code-block:: python

    import importlib
    importlib.reload(modulename)

    (demo)


Running a Module
----------------

In addition to importing modules, you can run them.

There are a few ways to do this:

.. rst-class:: build

* ``$ python hello.py``   -- must be in current working directory
* ``$ python -m hello``   -- any module on PYTHONPATH anywhere on the system
* ``$ ./hello.py``        -- put ``#!/usr/env/python``  at top of module (Unix)
* ``In [149]: run hello.py``     -- at the IPython prompt -- running a module brings its names into the interactive namespace


Like importing, running a module executes all statements at the module level.

But there's an important difference.

When you *import* a module, the value of the symbol ``__name__`` in the module is the same as the filename.

When you *run* a module, the value of the symbol ``__name__`` is ``__main__``.

This allows you to create blocks of code that are executed *only when you run a module*

.. code-block:: python

    if __name__ == '__main__':
        # Do something interesting here
        # It will only happen when the module is run

"main" blocks
-------------

This is useful in a number of cases.

You can put code here that lets your module be a utility *script*

You can put code here that demonstrates the functions contained in your module

You can put code here that proves that your module works.


[demo]


Import Interactions
-------------------

Let's experiment with importing different ways:

.. code-block:: ipython

    In [3]: import math

    In [4]: math.<TAB>
    math.acos       math.degrees    math.fsum       math.pi
    math.acosh      math.e          math.gamma      math.pow
    math.asin       math.erf        math.hypot      math.radians
    math.asinh      math.erfc       math.isinf      math.sin
    math.atan       math.exp        math.isnan      math.sinh
    math.atan2      math.expm1      math.ldexp      math.sqrt
    math.atanh      math.fabs       math.lgamma     math.tan
    math.ceil       math.factorial  math.log        math.tanh
    math.copysign   math.floor      math.log10      math.trunc
    math.cos        math.fmod       math.log1p
    math.cosh       math.frexp      math.modf


.. code-block:: ipython

    In [6]: math.sqrt(4)
    Out[6]: 2.0
    In [7]: import math as m
    In [8]: m.sqrt(4)
    Out[8]: 2.0
    In [9]: from math import sqrt
    In [10]: sqrt(4)
    Out[10]: 2.0


Experiment with importing different ways:

.. code-block:: python

    import sys
    print(sys.path)
    import os
    print(os.path)

You wouldn't want to import * those!

And while we are looking at the ``sys.path`` module:

Check out:

.. code-block:: python

    os.path.split('/foo/bar/baz.txt')
    os.path.join('/foo/bar', 'baz.txt')

