.. _modules_and_namespaces:

#######################################
Code Structure, Modules, and Namespaces
#######################################


**How to get what you want when you want it.**


Code Structure
==============

In Python, the structure of your code is determined by whitespace. This is nicely clear, and you've probably already figured it out, but we'll formally spell it out here:

How you *indent* your code determines how it is structured

::

    block statement:
        some code body
        some more code body
        another block statement:
            code body in
            that block
        end of "another" block statement
        still in the first block
    outside of the block statement

The colon that terminates a block statement is also important...

One-liners
----------

You can put a one-liner after the colon:

.. code-block:: ipython

    In [167]: x = 12
    In [168]: if x > 4: print(x)
    12

But this should only be done if it makes your code **more** readable.

So you need both the colon and the indentation to start a new a block.  But the end of the indented section is the only indication of the end of the block.

Spaces vs. Tabs
---------------

Whitespace is important in Python.

An indent *could* be:

* Any number of spaces
* A tab
* A mix of tabs and spaces:

If you want anyone to take you seriously as a Python developer:

**Always use four spaces -- really!**

`(PEP 8) <http://legacy.python.org/dev/peps/pep-0008/>`_

Also note: if you DO you tabs (and really, don't do that!) python interprets them as the equivalent of *eight* spaces.  Text editors can display tabs as any number of spaces, and most modern editors default to four -- so this can be *very* confusing! so again:

**never mix tabs and spaces in python code**

Spaces Elsewhere
----------------

Other than indenting -- space doesn't matter, technically.

.. code-block:: python

    x = 3*4+12/func(x,y,z)
    x = 3*4 + 12 /   func (x,   y, z)

These will give the exact same results.

But you should strive for proper style. Isn't this easier to read?

.. code-block:: python

    x = (3 * 4) + (12 / func(x, y, z))


*Read PEP 8 and install a linter in your editor.*


Modules and Packages
====================

Python is all about *namespaces* --  the "dots"

``name.another_name``

The "dot" indicates that you are looking for a name in the *namespace* of the given object. It could be:

* name in a module
* module in a package
* attribute of an object
* method of an object

The only way to know is to know what type of object the name refers to.  But in all cases, it is looking up a name in the namespace of the object.


Modules
-------

A module is simply a namespace.

It might be a single file, or it could be a collection of files that define a shared API.

But in the common and simplest case, a single file is a single module.

So you can think of the files you write that end in ``.py`` as modules.

When a module is imported, the code in that file is run, and any names defined in that file are now defined in the module namespace.


Packages
--------

A package is a module with other modules in it.

On a filesystem, this is represented as a directory that contains one or more``.py`` files, one of which **must** be called ``__init__.py``.

When you have a package, you can import only the package, or any of the modules inside it. When a package is imported, the code in the ``__init__.py`` file is run.


Importing modules
-----------------

There are a few ways to import modules:

.. code-block:: python

    import modulename

This adds the name of the module to the global namespace, and lets you access the names defined in that module:

.. code-block:: python

    modulename.a_name_in_the_module

.. code-block:: python

    from modulename import this, that

This brings only the names specified (``this``, ``that``) into the global namespace. All the code in the module is run, but the module's name is not available. But the imported names are directly available.

.. code-block:: python

    import modulename as a_new_name

This imports the module, and gives it a new name in the global namespace.  This is done to avoid a name conflict, or to give the module a shorter name. For example, the numpy module is usually imported as:

.. code-block:: python

    import numpy as np

Because numpy has a LOT of names, some of which may conflict, and users want to be able to reference them without a too much typing.

.. code-block:: python

    from modulename import this as that

This imports only one name from a module, while also giving it a new name in the global namespace.

Examples
--------

You can play with some of this with the standard library:

.. code-block:: ipython

    In [1]: import math

    In [2]: math.sin(1.2)
    Out[2]: 0.9320390859672263

    In [3]: from math import cos

    In [4]: cos(1.2)
    Out[4]: 0.3623577544766736

    In [5]: import math as m

    In [6]: m.sin(1)
    Out[6]: 0.8414709848078965

    In [7]: from math import cos as cosine

    In [8]: cosine(1.2)
    Out[8]: 0.3623577544766736

My rules of thumb
-----------------

If you only need a few names from a module, import only those:

.. code-block:: python

    from math import sin, cos, tan

If you need a lot of names from that module, just import the module:

.. code-block:: python

    import math
    math.cos(2 * math.pi)

Or import it with a nice short name:

.. code-block:: python

    import math as m
    m.cos(2 * m.pi)

import \* ?
-----------

**Warning:**

You can also import all the names in a module with:

.. code-block:: python

    from modulename import *

But this leads to name conflicts, and a cluttered namespace. It is NOT recommended practice.


Importing from packages
-----------------------

Packages can contain modules, which can be nested -- ideally not very deeply.

In that case, you can simply add more "dots" and follow the same rules as above.

.. code-block:: python


Here's a nice reference for more detail:

http://effbot.org/zone/import-confusion.htm



``import``
----------

When you import a module, or a symbol from a module, the Python code is *compiled* to **bytecode**.

The result is a ``module.pyc`` file.

Then after compiling, all the code in the module is run **at the module scope**.

For this reason, it is good to avoid module-scope statements that have global side-effects.


Re-import
----------

The code in a module is NOT re-run when imported again. This makes it efficient to import the same module multiple places in a program. But it means that if you change the code in a module after importing it, that change will not be reflected when it is imported again.

I you DO want ca change to be reflected, you can explicitly reload a module:

.. code-block:: python

    import importlib
    importlib.reload(modulename)

This is rarely needed (why it's a bit buried in the ``importlib`` module), but is good to keep in mind when you are interactively working on code under development.

Import Interactions
-------------------

Another key point to keep in mind is that all code files in a given python program are sharing the same modules. So if you change a value in a module, that value's change will be reflected in other parts of the code that have imported that same module.

This can create dangerous side effects and hard to find bugs if you change anything in an imported module, but it can also be used as a handy way to store truly global state, like application preferences, for instance.

A rule of thumb for managing global state is to have only *one* part of your code change the values, and everywhere else considers them read-only.






