.. _python_overview:

###############
Python Overview
###############

What is Python?
---------------

.. rst-class:: build

* Dynamic
* Object oriented
* Byte-compiled
* Interpreted

.. rst-class:: center large

But what does that mean?

Python Features
---------------

.. rst-class:: build

* Unlike C, C++, C\#, Java ... More like Ruby, Lisp, Perl, Javascript
  ...

* **Dynamic** -- no type declarations

  * Programs are shorter
  * Programs are more flexible
  * Less code means fewer bugs

* **Interpreted** -- no separate compile, build steps - programming process is simpler

What's a Dynamic language?
--------------------------

**Dynamic typing**.

* Type checking and dispatch happen at run-time

.. code-block:: ipython

    In [1]: x = a + b

.. rst-class:: build

* What is ``a``?
* What is ``b``?
* What does it mean to add them?
* ``a`` and ``b`` can change at any time before this process

**Strong typing**.

.. code-block:: ipython

    In [1]: a = 5

    In [2]: type(a)
    Out[2]: int

    In [3]: b = '5'

    In [4]: type(b)
    Out[4]: str

.. rst-class:: build

* **everything** has a type.
* the *type* of a thing determines what it can do.

Duck Typing
-----------

.. rst-class:: center large

"If it looks like a duck, and quacks like a duck -- it's probably a duck"

.. rst-class:: center large

If an object behaves as expected at run-time, it's the right type.

Python Versions
---------------

Python 2.x

.. rst-class:: build

* "Classic" Python
* Evolved from original

Python 3.x ("py3k")

.. rst-class:: build

* Updated version
* Removed the "warts"
* Allowed to break code


This class uses Python 3 -- not Python 2

.. rst-class:: build

* Adoption of Python 3 is growing fast

  * Almost all key packages now supported (https://python3wos.appspot.com/)
  * But much code in the wild is still 2.x

* If you find yourself needing to work with Python 2 and 3, there are ways to write compatible code: https://wiki.python.org/moin/PortingPythonToPy3k

* We will cover that more later in the program. Also: a short intro to the differences you really need to know about up front later this session.

:ref:`py2_vs_py3`


