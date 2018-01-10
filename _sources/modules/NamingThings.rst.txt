:orphan:

.. _style_and_naming:

################
Style and Naming
################

**Style matters!**

PEP 8 reminder
--------------

PEP 8 (Python Enhancement Proposal 8):
https://www.python.org/dev/peps/pep-0008/

Is the "official" style guide for Python code.

Strictly speaking, you only need to follow it for code in the standard library.

But style matters -- consistent style makes your code easier to read and understand.

And everyone in the community has accepted PEP as *the* Python style guide.

So **follow PEP 8**

**Exception:** if you have a company style guide -- follow that instead.

Try the "pycodestyle" module on your code::

  $ python3 -m pip install pycodestyle
  $ pycodestyle my_python_file

Try it now -- really!

Note that ideally you have a linter installed in your editor that yells at you if you violate PEP8 -- no need to run ``pycodestyle`` if it's already in your editor.

See: :ref:`editor_for_python` for suggestions on editors and configuration.

Naming things...
----------------

It matters what names you give your variables.

Python has rules about what it *allows*.

PEP8 has rules for style: capitalization, and underscores and all that.

But you still get to decide within those rules.

So use names that make sense to the reader.

Naming Guidelines
-----------------

Whenever possible, use strong, unambiguous names that relate to a concept in the business area applicable for your program.
For example, cargo_weight is probably better than item_weight, current_fund_price is better than value.

Only use single-letter names for things with limited scope: indexes and the like:

.. code-block:: python

    for i, item in enumerate(a_sequence):
        do_something(i, item)

But **don't** use a name like "item", when there is a meaning to what the item is:

.. code-block:: python

    for name in all_the_names:
        do_something_with(name)

Use plurals for collections of things:

.. code-block:: python

    names = ['Fred', 'George', ...]

And then singular for a single item in that collection:

.. code-block:: python

    for name in names:
       ...

**Do** re-use names when the use is essentially the same, and you don't need the old one:

.. code-block:: python

    line = line.strip()
    line = line.replace(",", " ")
    ....

Here's a nice talk about naming:

http://pyvideo.org/video/3792/name-things-once-0

