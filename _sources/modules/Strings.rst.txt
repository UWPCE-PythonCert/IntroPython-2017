.. _strings:

#######
Strings
#######

  Fun with Strings

Strings
=======

A "String" is a computerese word for a piece of text -- a "string" of characters.

Creating strings:
-----------------

A string literal creates a string type.

(we've seen this already...)

::

    "this is a string"

    'So is this'

    """and this also"""

    '''and even this'''

You can also use ``str()``

.. code-block:: ipython

    In [256]: str(34)
    Out[256]: '34'

And strings can be read from files or other sources of I/O.

String Methods
===============

String objects have a lot of methods.

Here are just a few:

Splitting and Joining Strings
-----------------------------

``split`` and ``join``:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']
    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'

It may seem odd at first that ``.join()`` is a string method, rather than, say, a method on lists. But, in fact it makes a lot of sense. Lists (and tuples, and other sequences) can hold any type of data -- and "joining" arbitrary data types doesn't make any sense.  Joining is strictly a string activity.

And you need a string so you can join the parts -- therefore, we need a string object in there somewhere anyway.

Lastly, having join() be a string method means that it can join strings in ANY iterable object -- not just the built-in sequence types.

So it does make sense -- but even if not, that's the way it is.

So to be clear: if you have a bunch of strings in a sequence and you want to put them together, you create a string with the character (or characters) you want to join them with, and call join() on that object:

.. code-block:: python

    In [20]: # comma separated:

    In [21]: ",".join(["these", "are", "some", "strings"])
    Out[21]: 'these,are,some,strings'

    In [22]: # you can concatenate by joining with the empty string:

    In [23]: "".join(["these", "are", "some", "strings"])
    Out[23]: 'thesearesomestrings'

Building up a long string.
--------------------------

The obvious thing to do is something like:

.. code-block:: python

  msg = ""
  for piece in list_of_stuff:
      msg += piece

But: strings are immutable -- Python needs to create a new string each time you add a piece -- not efficient:

.. code-block:: python

   msg = []
   for piece in list_of_stuff:
       msg.append(piece)
   " ".join(msg)

appending to lists is efficient -- and so is the join() method of strings.


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

    In [12]: print(s)
    these   are separated   by  tabs

https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
https://docs.python.org/3/library/stdtypes.html#string-methods

Raw Strings
------------

Add an ``r`` in front of the string literal:

**Escape Sequences Ignored**

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

putting a backslash right before the end quote confuses the interpreter!

This can be very handy for things like regular expressions that need embedded backslashes.


Ordinal values
--------------

Characters in strings are stored as numeric values:

* "ASCII" values: 1-127

* Unicode values -- 1 - 1,114,111 (!!!)

Unicode supports a LOT of characters --every character in every language known to man -- and then some :-)

To get the value:

.. code-block:: ipython

    In [109]: for i in 'Chris':
       .....:     print(ord(i), end=' ')
    67 104 114 105 115
    In [110]: for i in (67,104,114,105,115):
       .....:     print(chr(i), end='')
    Chris

For the English language, stick with ASCII, otherwise use full Unicode: it's easy with Python3 -- more on that in a later lesson.


Building Strings from data
--------------------------

You could, but please don't(!), do this:

.. code-block:: python

    'Hello ' + name + '!'

(I know -- we did that in the grid_printing exercise)

Do this instead:

.. code-block:: python

    'Hello {}!'.format(name)

It's much faster and safer, and easier to modify as code gets complicated.

https://docs.python.org/3/library/string.html#string-formatting


Old and New string formatting
-----------------------------

Back in early Python days, there was the string formatting operator: ``%``

.. code-block:: python

    "a string: %s and a number: %i "%("text", 45)

This is very similar to C-style string formatting (`sprintf`).

It's still around, and handy --- but ...

The "new" ``format()`` method is more powerful and flexible, so we'll focus on that in this class.

String Formatting
-----------------

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


    In [69]: "Hello, {name}, whadaya know?".format(name="Joe")
    Out[69]: 'Hello, Joe, whadaya know?'

You can use values more than once, and skip values:

.. code-block:: ipython

    In [73]: "Hi, {name}. Howzit, {name}?".format(name='Bob')
    Out[73]: 'Hi, Bob. Howzit, Bob?'


The format operator works with string variables, too:

.. code-block:: ipython

    In [80]: s = "{:d} / {:d} = {:f}"

    In [81]: a, b = 12, 3

    In [82]: s.format(a, b, a/b)
    Out[82]: '12 / 3 = 4.000000'

So you can dynamically build a format string, and then use it in multiple places in the code.


Complex Formatting
------------------

There is a complete syntax for specifying all sorts of options.

It's well worth your while to spend some time getting to know this
`formatting language`_. You can accomplish a great deal just with this.

.. _formatting language: https://docs.python.org/3/library/string.html#format-specification-mini-language

Here is a nice tutorial:

https://pyformat.info/

And a nice formatting cookbook:

https://mkaz.tech/python-string-format.html


Literal String Interpolation
============================

In Python 3.6, yet another string formatting method was introduced.

Known at "f-strings", or more formally, "Literal String Interpolation", they provide a concise, readable way to include the value of Python expressions inside strings. In particular, they make it easy to include names in the current namespace without having to type them multiple times.

For example:

.. code-block:: ipython

    In [24]: first = "Chris"

    In [25]: last = "Barker"

    In [26]: f"My name is {first} {last}"
    Out[26]: 'My name is Chris Barker'

Note that they are called "f-strings" because they are created by putting and "f" before the string -- "f" is for format.

All the other ways to do this required a lot more typing:

.. code-block:: ipython

    In [28]: "My name is {first} {last}".format(first=first, last=last)
    Out[28]: 'My name is Chris Barker'

    In [29]: "My name is {} {}".format(first, last)
    Out[29]: 'My name is Chris Barker'

    In [30]: "My name is %s %s" % (first, last)
    Out[30]: 'My name is Chris Barker'

f-string basics
---------------

f-strings are actually pretty simple concept:

You can interpolate the stringifcation of any expression into a string at run time. Variables are all evaluated at the current scope.

The expression is put inside curly brackets: {}, the same as for the ``.format`` method.

So what does that all mean?

For this most simple example::

  f"some text: {str(expression)}"

`expression` is any valid python expression(remember that an expression is a combination of values and operators and names that produces a value).

The expression is evaluated, and then, if it is not a string, it is converted to one, so it's really::

  f"some text: {str(expression)}"

Let's see how that works in practice:

.. code-block:: ipython

    In [32]: # define a couple of names:

    In [33]: x = 5

    In [34]: y = 12

    In [35]: name = "fred"

    In [36]: # a simple string:

    In [37]: f"some text: {name}"
    Out[37]: 'some text: fred'

    In [38]: # if it's not a string, it will be turned into one:

    In [39]: f"some text: {x}"
    Out[39]: 'some text: 5'

    In [40]: # but you can do a more complex expression as well:

    In [41]: f"some text: {x + y}"
    Out[41]: 'some text: 17'

    In [42]: # and call methods:

    In [43]: f"some text: {name.capitalize()}"
    Out[43]: 'some text: Fred'

    In [45]: # even boolean expressions:

    In [46]: f"some text: {name if x < 5 else name2}"
    Out[46]: 'some text: bob'

You can put ANY expression in there -- no matter how complex. But do be careful, if it's too complex, it will just make the code harder to read!

And it has to be an expression, not a statement -- so you can't put a for loop or anything like that in there.

You can see how this can be a very powerful and quick way to get things done.

f-string use
------------

F-strings are a very new Python feature. They will cause a syntax error in any Python version older than 3.6 -- and 3.6 was first released on December 23, 2016 -- less than a year from this writing.

So there is not much out there in the wild, and I have yet to see it in production code.

They are not currently used in any of the examples in this course.

Nevertheless, they are a nifty feature that could be very useful, so feel free to use them where it makes you code cleaner and clearer.

More on f-strings
-----------------

To read all about the justification and syntax, read PEP 498:

https://www.python.org/dev/peps/pep-0498/

Other resources for f-strings
-----------------------------

f-strings are quite new, but there are a few introductions out there:

A short introduction:

https://cito.github.io/blog/f-strings/

Another intro:

https://www.pydanny.com/python-f-strings-are-fun.html

One that gets into the technical details (bytecode! -- for the real geeks):

https://hackernoon.com/a-closer-look-at-how-python-f-strings-work-f197736b3bdb

