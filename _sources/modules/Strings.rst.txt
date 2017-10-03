.. _strings:

#######
Strings
#######

  Fun with Strings

Strings
=======

A "String" is a computerese work=d for a piece of text -- a "string" of charactors.

Creating strings:
-----------------

A string literal creates a string type

(we've seen this already...)

::

    "this is a string"

    'So is this'

    """and this also"""

You can also use ``str()``

.. code-block:: ipython

    In [256]: str(34)
    Out[256]: '34'

And strings can be read from files, and other sources of I/O.

String Methods
===============

String objects have a lot of methods.

Here are just a few:

String Manipulations
---------------------

``split`` and ``join``:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']
    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'


Case Switching
--------------

.. code-block:: ipython

    In [171]: sample = 'A long string of words'
    In [172]: sample.upper()
    Out[172]: 'A LONG STRING OF WORDS'
    In [173]: sample.lower()
    Out[173]: 'a long string of words'
    In [174]: sample.swapcase()
    Out[174]: 'a LONG STRING OF WORDS'
    In [175]: sample.title()
    Out[175]: 'A Long String Of Words'


Testing
--------

.. code-block:: ipython

    In [181]: number = "12345"
    In [182]: number.isnumeric()
    Out[182]: True
    In [183]: number.isalnum()
    Out[183]: True
    In [184]: number.isalpha()
    Out[184]: False
    In [185]: fancy = "Th!$ $tr!ng h@$ $ymb0l$"
    In [186]: fancy.isalnum()
    Out[186]: False


String Literals
-----------------

Common Escape Sequences::

    \\  Backslash (\)
    \a  ASCII Bell (BEL)
    \b  ASCII Backspace (BS)
    \n  ASCII Linefeed (LF)
    \r  ASCII Carriage Return (CR)
    \t  ASCII Horizontal Tab (TAB)
    \ooo  Character with octal value ooo
    \xhh  Character with hex value hh

for example -- for tab-separated values:

.. code-block:: ipython

    In [25]: s = "these\tare\tseparated\tby\ttabs"

    In [26]: print(s)
    these   are separated    by  tabs

https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
https://docs.python.org/3/library/stdtypes.html#string-methods

Raw Strings
------------

Add an ``r`` in front of the string literal:

Escape Sequences Ignored

.. code-block:: ipython

    In [408]: print("this\nthat")
    this
    that
    In [409]: print(r"this\nthat")
    this\nthat

**Gotcha**

.. code-block:: ipython

    In [415]: r"\"
    SyntaxError: EOL while scanning string literal

(handy for regex, windows paths...)


Ordinal values
--------------

Characters in strings are stored as numeric values:

* "ASCII" values: 1-127

* Unicode values -- 1 - 1,114,111 (!!!)

To get the value:

.. code-block:: ipython

    In [109]: for i in 'Chris':
       .....:     print(ord(i), end=' ')
    67 104 114 105 115
    In [110]: for i in (67,104,114,105,115):
       .....:     print(chr(i), end='')
    Chris

(these days, stick with ASCII, or use full Unicode: more on that in a few weeks)


Building Strings
-----------------

You can, but please don't do this:

.. code-block:: python

    'Hello ' + name + '!'

(I know -- we did that in the grid_printing excercise)

Do this instead:

.. code-block:: python

    'Hello {}!'.format(name)

It's much faster and safer, and easier to modify as code gets complicated.

https://docs.python.org/3/library/string.html#string-formatting

Old and New string formatting
-----------------------------

back in early python days, there was the string formatting operator: ``%``

.. code-block:: python

    " a string: %s and a number: %i "%("text", 45)

This is very similar to C-style string formatting (`sprintf`).

It's still around, and handy --- but ...

The "new" ``format()`` method is more powerful and flexible, so we'll focus on that in this class.

.. nextslide:: String Formatting

The string ``format()`` method:

.. code-block:: ipython

    In [62]: "A decimal integer is: {:d}".format(34)
    Out[62]: 'A decimal integer is: 34'

    In [63]: "a floating point is: {:f}".format(34.5)
    Out[63]: 'a floating point is: 34.500000'

    In [64]: "a string is the default: {}".format("anything")
    Out[64]: 'a string is the default: anything'


Multiple placeholders:
-----------------------

.. code-block:: ipython

    In [65]: "the number is {} is {}".format('five', 5)
    Out[65]: 'the number is five is 5'

    In [66]: "the first 3 numbers are {}, {}, {}".format(1,2,3)
    Out[66]: 'the first 3 numbers are 1, 2, 3'

The counts must agree:

.. code-block:: ipython

    In [67]: "string with {} formatting {}".format(1)
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-67-a079bc472aca> in <module>()
    ----> 1 "string with {} formatting {}".format(1)

    IndexError: tuple index out of range


Named placeholders:
-------------------

.. code-block:: ipython


    In [69]: "Hello, {name}, whaddaya know?".format(name="Joe")
    Out[69]: 'Hello, Joe, whaddaya know?'

You can use values more than once, and skip values:

.. code-block:: ipython

    In [73]: "Hi, {name}. Howzit, {name}?".format(name='Bob')
    Out[73]: 'Hi, Bob. Howzit, Bob?'

.. nextslide::

The format operator works with string variables, too:

.. code-block:: ipython

    In [80]: s = "{:d} / {:d} = {:f}"

    In [81]: a, b = 12, 3

    In [82]: s.format(a, b, a/b)
    Out[82]: '12 / 3 = 4.000000'

So you can dynamically build a format string

Complex Formatting
------------------

There is a complete syntax for specifying all sorts of options.

It's well worth your while to spend some time getting to know this
`formatting language`_. You can accomplish a great deal just with this.

.. _formatting language: https://docs.python.org/3/library/string.html#format-specification-mini-language


String Formatting LAB
=====================

Let's play with these a bit:

:ref:`exercise_string_formatting`

