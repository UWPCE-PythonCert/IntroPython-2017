.. _python_for_mac:

**************************
Setting up OS-X for Python
**************************

==================
Getting The Tools
==================

.. rst-class:: left

OS-X comes with Python out of the box, but not the full setup you'll need for development or this class. It also doesn't have the latest version(s), and no version of Python 3.

So we recommend installing a new version.

.. rst-class:: left

**Note**:

.. rst-class:: left

If you use ``macports`` or ``homebrew`` to manage \*nix software on your machine, feel free to use those for ``python``, ``git``, etc, as well. But make sure you have python 3.6.*

If not, then read on.

Terminal
---------

You will need a command line terminal. The built-in "terminal" application works fine. Find it in::

  /Applications/Utilities/Terminal

Drag it to the dock to easy access.

Python
------

While OS-X does provide python out of the box -- it tends not to have the
latest version, and you really don't want to mess with the system
installation. So we recommend installing an independent installation from
``python.org``:

Download the latest realease of Python (currently 3.6.2) installer from Python.org:

https://www.python.org/downloads/

Double click the installer and follow the prompts -- the defaults are your best bet. Simple as that.

Oddly, this does NOT install a ``python`` command, but rather a ``python3`` command. If you want to be able to simply type ``python`` and get python3, then you can add a symlink to the install. Type this at a terminal prompt:

.. code-block:: bash

  $ cd /Library/Frameworks/Python.framework/Versions/3.6/bin
  $ ln -s python3.6 python

(or an add an alias in your shell -- an Unix geeks here?)

Once you have done that, you should be able to type ``python`` at the command prompt, and get something like:

.. code-block:: bash

  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

This is the Python interpreter.

Type ``ctrl+D`` to get out (or ``exit()``)


pip
---

``pip`` is the Python package installer. It is updated faster than python itself, so once you have python, you want to get the latest version of pip working::

  $ python -m ensurepip --upgrade

[first make sure that ``python`` gives you the one you want. You may need to call ``python3`` instead]

It should download and install the latest ``pip``.

You can now use pip to install other packages.

Using pip:
----------

To use pip to install a package, you invoke it with this command::

  python -m pip install the_name_of_the_package

Where ``python`` is the command you use to invoke the python you want to use (could be ``python3``)

**NOTE:** You will frequently see advice to use pip like so::

  $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

  $ python -m pip install something_or_other

calls python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of python that you are running.

iPython
--------

One package we are going to use in the program from the begining is ``iPython``. You can install it with ``pip`` like so::

  $ python3 -m pip install ipython[all]

(it will install a LOT...).

You should now be able to run ``iPython``:

.. code-block:: ipython

  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  Type 'copyright', 'credits' or 'license' for more information
  IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

  In [1]:


git
----

git is a source code version control system. It is not strictly related to Python, but it (or a similar system) is a critical tool for software development in general, and it is very widely used in the Python community. We will be using it, along with the gitHub service, in the program to hand in assignments and support code review.

You need a git client -- the gitHub GUI client may be nice -- I honestly don't know, but we will be using the command line client in class.

There are a couple options for a command line client.

This one:

http://sourceforge.net/projects/git-osx-installer/

Is a big download and install, but has everything you need out of the box.

NOTE: if you get a warning like:

"... can't be opened because it is from an untrusted developer"

you'll need to go to  system preferences:

  "Security and Privacy"

  Then check the box saying "Open Anyway". Or maybe check the box saying you can install untrusted packages -- depends on the OS-X version.

This one:

http://git-scm.com/download/mac

Works great, but you need the XCode command line tools to run it. If you already have that, or expect to need a compiler anyway, then this is a good option.

You can get XCode from the Apple App Store.

(If you try running "git" on the command line after installing, it should send you there).

Warning: XCode is a BIG download. Once installed, run it so it can initialize itself.

After either of these is installed, the ``git`` command should work:

.. code-block:: bash

  $ git --version
  git version 2.11.0 (Apple Git-81)

Testing it out
--------------

To be ready for the program, you need to have:
 - python
 - pip
 - iPython
 - git

All available from the command line.

To try it out, you should be able to run all of these commands, and get something like the following results:

(recall that you can get out of the python or iPython command lines with ``ctrl+D``)

For Python:

.. code-block:: bash

  MacBook-Pro:PythonCertDevel Chris$ python
  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> ^D

For iPython:

.. code-block:: bash

  MacBook-Pro:PythonCertDevel Chris$ ipython
  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  Type 'copyright', 'credits' or 'license' for more information
  IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

  In [1]:

  Do you really want to exit ([y]/n)? y

For pip:

.. code-block:: bash

  MacBook-Pro:PythonCertDevel Chris$ python -m pip --version
  pip 9.0.1 from /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (python 3.6)

For git:

.. code-block:: bash

  MacBook-Pro:PythonCertDevel Chris$ git --version
  git version 2.11.0 (Apple Git-81)


















