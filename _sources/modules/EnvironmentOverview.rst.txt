Introduction to the Environment
===============================

There are three basic elements to your environment when working with Python:

.. rst-class:: left

.. rst-class:: build

* The Command Line
* The Interpreter
* The Editor


The Command Line (cli)
----------------------

Having some facility on the command line is important

We won't cover this much in class, so if you are not comfortable,
please bone up on your own.

We have some resources here: `PythonResources--command line <http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/command_line.html>`_

We suggest running through the **cli** tutorial at "learn code the hard way":

http://cli.learncodethehardway.org/book/

**Windows:**

Most of the demos in class, etc, will be done using the "bash" command line shell on OS-X. This is identical to the bash shell on Linux.

Windows provides the "DOS" command line, which is OK, but pretty old and limited, or "Power Shell" -- a more modern, powerful, flexible command shell.

If you are comfortable with either of these -- go for it.

If not, you can use the "git Bash" shell -- which is much like the bash shell on OS-X and Linux. Or, on Windows 10, look into the "bash shell for Windows" otherwise known as the "Linux system" - - more info here: `PythonResources--Windows Bash  <http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/windows_bash.html>`_


The Interpreter
---------------

Python comes with a built-in interpreter.

You see it when you type ``python`` at the command line:

.. code-block:: bash

  $ python
  Python 3.6.1 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

That last thing you see, ``>>>`` is the "Python prompt".

This is where you type code.


Python in the Interpreter
-------------------------

Try it out:

.. code-block:: python

    >>> print("hello world!")
    hello world!
    >>> 4 + 5
    9
    >>> 2 ** 8 - 1
    255
    >>> print ("one string" + " plus another")
    one string plus another
    >>>

.. nextslide:: Tools in the Interpreter

When you are in an interpreter, there are a number of tools available to
you.

There is a help system:

.. code-block:: python

    >>> help(str)
    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object='') -> string
     |
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     ...

You can type ``q`` to exit the help viewer.

.. nextslide:: Tools in the Interpreter

You can also use the ``dir`` builtin to find out about the attributes of a
given object:

.. code-block:: python

    >>> bob = "this is a string"
    >>> dir(bob)
    ['__add__', '__class__', '__contains__', '__delattr__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
     ...
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
     'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> help(bob.rpartition)

This allows you quite a bit of latitude in exploring what Python is.

.. nextslide:: Advanced Interpreters

In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython``

More on this soon.


The Editor
----------

Typing code in an interpreter is great for exploring.

But for anything "real", you'll want to save the work you are doing in a more permanent
fashion.

This is where an Editor fits in.

.. nextslide:: Text Editors Only

Any good text editor will do.

MS Word is **not** a text editor.

Nor is *TextEdit* on a Mac.

``Notepad`` on Windows is a text editor -- but a crappy one.

You need a real "programmers text editor"

A text editor saves only what it shows you, with no special formatting
characters hidden behind the scenes.

.. nextslide:: Minimum Requirements

At a minimum, your editor should have:

.. rst-class:: build

* Syntax Colorization
* Automatic Indentation

In addition, great features to add include:

.. rst-class:: build

* Tab completion
* Code linting
* Jump-to-definition

Have an editor that does all this? Feel free to use it.

If not, we recommend ``SublimeText``:

http://www.sublimetext.com/

Use version 3.

http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/sublime_as_ide.html

"Atom" is another good open source option.

https://atom.io/

And, of course, vim or Emacs on Linux, if you are familiar with those.

Why No IDE?
-----------

An IDE does not give you much that you can't get with a good editor plus a good interpreter.

An IDE often weighs a great deal

Setting up IDEs to work with different projects can be challenging and time-consuming.

Particularly when you are first learning, you don't want too much done for you.


Why Not an IDE?
---------------

That said ...

You may want to go get the educational edition of PyCharm:

https://www.jetbrains.com/pycharm-edu/

Which is awesome.
