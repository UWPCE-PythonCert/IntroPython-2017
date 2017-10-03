Comprehensions
==============

List comprehensions
-------------------

A bit of functional programming

consider this common ``for`` loop structure:

.. code-block:: python

    new_list = []
    for variable in a_list:
        new_list.append(expression)

This can be expressed with a single line using a "list comprehension"

.. code-block:: python

    new_list = [expression for variable in a_list]


.. nextslide::

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

.. nextslide::

But usually you at least have a conditional in the loop:

.. code-block:: python

    new_list = []
    for variable in a_list:
        if something_is_true:
            new_list.append(expression)

You can add a conditional to the comprehension:

.. code-block:: python

    new_list = [expr for var in a_list if something_is_true]

.. nextslide::

Examples:

.. code-block:: ipython

    In [341]: [x**2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x+y for x in range(3) for y in range(5,7)]
    Out[342]: [5, 6, 6, 7, 7, 8]

    In [343]: [x*2 for x in range(6) if not x%2]
    Out[343]: [0, 4, 8]

.. nextslide::

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

You can do it with sets, too:

.. code-block:: python

    new_set = { value for variable in a_sequence }


same as for loop:

.. code-block:: python

    new_set = set()
    for key in a_list:
        new_set.add(value)


.. nextslide::

Example: finding all the vowels in a string...

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

    new_dict = { key:value for variable in a_sequence}


same as for loop:

.. code-block:: python

    new_dict = {}
    for key in a_list:
        new_dict[key] = value



.. nextslide::

Example

.. code-block:: ipython

    In [22]: { i: "this_%i"%i for i in range(5) }
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}


(not as useful with the ``dict()``  constructor...)
