.. _comprehensions:

##############
Comprehensions
##############


List comprehensions
-------------------

A bit of functional programming.

The concept of "functional programming" is clearly defined in some contexts, but is also used in a less strict sense. Python is **not** a functional language in the strict sense, but it does support a number of functional paradigms.

In general, code is considered "Pythonic" that used functional paradigms where they are natural, but not when they have to be forced in.

We will cover functional programming concepts more clearly later in the program, but for now, we'll talk about the syntax for a common functional paradigm: applying an expression to all the members of a sequence to produce another sequence:

Consider this common ``for`` loop structure:

.. code-block:: python

    new_list = []
    for variable in a_list:
        new_list.append(expression(variable))

This is such a common pattern, that python added syntax to directly support it:

It can be expressed with a single line using a "list comprehension"

.. code-block:: python

    new_list = [expression for variable in a_list]

What about nested for loops?

.. code-block:: python

    new_list = []
    for var in a_list:
        for var2 in a_list2:
            new_list.append(expression)

Can also be expressed in one line:

.. code-block:: python

    new_list =  [exp for var in a_list for var2 in a_list2]

You get the "outer product", i.e. all combinations.

.. code-block:: ipython

    In [33]: list1 = [1, 2, 3]

    In [34]: list2 = [4, 5]

    In [35]: [(a, b) for a in list1 for b in list2]
    Out[35]: [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

Note that it makes every combination of the two input lists, and thus will be ``len(list1) * len(list2)`` in size. And there is no reason for them to be the same size.

zip() with comprehensions
-------------------------

If you want them paired up instead, you can use ``zip()``:

In [31]: [(a, b) for a, b in zip(list1, list2)]
Out[31]: [(1, 4), (2, 5), (3, 6)]



Comprehensions and map()
------------------------

Comprehensions are another way of expressing the "map" pattern from functional programming.

Python does have a ``map()``, which pre-dates comprehensions. But it does much of the same things -- and most folks think comprehensions are the more "Pythonic" way to do it.


What about filter?
------------------

``filter()`` is another functional concept: building an new list with only *some* of the elements -- "filtering" out the ones you don't want.

This is tp support the comon case of when you have a conditional in the loop:

.. code-block:: python

    new_list = []
    for variable in a_list:
        if something_is_true:
            new_list.append(expression)

You can do the same thing by adding a conditional to the comprehension:

.. code-block:: python

    new_list = [expr for var in a_list if something_is_true]

This is expressing the "filter" pattern. (and map at the same time -- one reason I like comprehensions more)


**Examples:**

.. code-block:: ipython

    In [341]: [x**2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x+y for x in range(3) for y in range(5,7)]
    Out[342]: [5, 6, 6, 7, 7, 8]

    In [343]: [x*2 for x in range(6) if not x%2]
    Out[343]: [0, 4, 8]


Get creative....

.. code-block:: python

    [name for name in dir(__builtin__) if "Error" in name]
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BufferError',
     'EOFError',
     ....

Set Comprehensions
------------------

You can do a similar thing with sets, too:

.. code-block:: python

    new_set = { value for variable in a_sequence }


same as for loop:

.. code-block:: python

    new_set = set()
    for key in a_list:
        new_set.add(value)


**Example:** Finding all the vowels in a string...

.. code-block:: ipython

    In [19]: s = "a not very long string"

    In [20]: vowels = set('aeiou')

    In [21]: { l for l in s if l in vowels }
    Out[21]: {'a', 'e', 'i', 'o'}

Side note: why did I do ``set('aeiou')`` rather than just `aeiou` ?


Dict Comprehensions
-------------------

Also with dictionaries

.. code-block:: python

    new_dict = { key: value for variable in a_sequence}


Same as this for loop:

.. code-block:: python

    new_dict = {}
    for key in a_list:
        new_dict[key] = value


**Example:**

.. code-block:: ipython

    In [22]: { i: "this_%i"%i for i in range(5) }
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}


This is not as useful as it used to be, now that we have the ``dict()``  constructor...

A bit of history:
-----------------

In the early days of Python the only way to create a dict was with a literal::

  a_dict = {}  # an empty dict

or a dict that was already populated with a bunch of data.

If you had a bunch of data in some other form, like a couple lists, you'd need to write a loop to fill it in:

.. code-block:: ipython

    In [1]: names = ["fred", "john", "mary"]

    In [2]: ids = [1, 2, 3]

    In [4]: d = {}

    In [5]: for id, name in zip(names, ids):
       ...:     d[id] = name
       ...:

    In [6]: d
    Out[6]: {'fred': 1, 'john': 2, 'mary': 3}

now, with dict comps, you can do:

.. code-block:: ipython

    In [9]: d = {id: name for id, name in zip(ids, names)}

    In [10]: d
    Out[10]: {1: 'fred', 2: 'john', 3: 'mary'}

But there is also now a ``dict()`` constructor (actually the type object for dict):

.. code-block:: ipython

    In [13]: dict?
    Init signature: dict(self, /, *args, **kwargs)
    Docstring:
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    Type:           type

So the first one is an empty dict -- simple enough

The second makes a dict from the contents of another dict (or similar object)

The third one is of interest here -- it makes a dict from an iterable of key, value pairs -- exactly what ``zip()`` gives you.

So we can create a dict from data like so:

.. code-block:: ipython

    In [14]: d = dict(zip(ids, names))

    In [15]: d
    Out[15]: {1: 'fred', 2: 'john', 3: 'mary'}

Which is more compact, and arguably more clear than the dict comprehension.

dict comps are still nice if you need to filter the results, though:

.. code-block:: ipython

    In [16]: d = {id: name for id, name in zip(ids, names) if name != 'mary'}

    In [17]: d
    Out[17]: {1: 'fred', 2: 'john'}

