:orphan:

.. _script_slicing:

.. NOTE: this is only a few things I want to show on screen, the text is elsewhere.

#######
Slicing
#######

Python's "secret power".

Syntax:
=======

Slicing a sequence creates a new sequence with a range of objects from the
original sequence.

|


Slicing uses the indexing operator: ``[]``

... but with a twist.

|
|

``sequence[start:end]``
==========================


Returns:

``sequence[i] for which start <= i < end``
=============================================


|
|

That's a fancy way to say that it's all the items from start to end -- including start, but NOT including end.


Helpful Hint
============

|

Think of the indexes as pointing to the spaces between the items::

       a       b   u   n   c   h       o   f       w   o   r   d   s
     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15

|


Nifty Slicing Properties
========================


``len(seq[a:b]) == b-a``
------------------------

``len(seq[:b]) == b``
---------------------

``len(seq[-b:]) == b``
----------------------

``seq[:b] + seq[b:] == seq``
----------------------------

|

There are very many fewer "off by one" errors as a result.


