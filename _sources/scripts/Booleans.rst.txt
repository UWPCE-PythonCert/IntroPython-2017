:orphan:

Booleans
========

With Rick Riehle
----------------

In a certain sense there isn't much to talk about with regard to booleans. Everybody knows what the word boolean means: true of false, yes or no. When programming we are using them all the time to accomplish flow control, sometimes explicitly yet often implicitly. Among Python's key or reserved words are ``True`` and ``False``.  You can test for these values explicitly when making flow control decisions.

.. code-block:: ipython

	In [1]: if (3 + 3 == 6) is True:
	   ...:     print("Woo! Logic.")
	   ...:
	Woo! Logic.

Yet as often you will not need nor will you use the explicit comparison with True, because the expression within the parenthesis evaluates to True.

.. code-block:: ipython

	In [2]: if (3 + 3 == 6):
	   ...:     print("Woo! Still logic.")
	   ...:
	Woo! Still logic.

Do we even need the comparison within the expression?

.. code-block:: ipython

	In [3]: if (3 + 3):
	   ...:     print("Yep")
	   ...:
	Yep

Perhaps not, but what is really going on here. What if we change the expression as follows?

.. code-block:: ipython

	In [4]: if (3 - 3):
	   ...:     print("Yup")
	   ...:

Wait, we did not get a Yup. Why not?

Truthy & falsy
--------------

We have developed an idea in the programming world... I don't know if it originated in the halls of computer science departments or if it's more of a hacker term. That idea is "truthy". Truthiness, truthy and falsy. Odd sounding terms if you haven't heard them before. They sound somewhat iffy or floaty, as if Truth were hard to pin down. Well, truth is hard to pin down, but that's not the sort of truth we're talking about. Rather, we are referring to values that Python considers to be equivalents to true or values that are equivalent to false. One way to test is to use the built-in function ``bool()``.

.. code-block:: ipython

	In [5]: bool(3+3)
	Out[5]: True

	In [6]: bool(3-3)
	Out[6]: False

By now you are likely noticing a pattern, but to make it yet more obvious....

.. code-block:: ipython

	In [7]: bool(6)
	Out[7]: True

	In [8]: bool(0)
	Out[8]: False

There are a lot of expressions that evaluate to ``True`` in Python. Any non-zero value is considered ``True``. Any expression that evaluates to zero is ``False``. Indeed it may be easier to think about what evaluates to ``False`` and is therefore considered falsy, than it is to think about what is true and therefore truthy. Here is a fairly inclusive list of things that are considered falsy.

	*  None
	*  False
	*  zero of any numeric type, for example, 0, 0.0, 0j
	*  any empty sequence, for example, '', (), []
	*  any empty dictionary or set, for example, {}
	*  any object for which ``__bool__()`` returns False
	*  any object for which ``__len__()`` returns 0

You may not recognize ``__bool__()`` and ``__len__()``. They are Python special methods. Special methods are sometimes called dunders because their names begin and end with double underscores. The Python interpreter invokes them for you, in the background so to speak, when it needs too. Don't worry about it for now, more on dunders later.

Boolean Operations
------------------

There are three boolean operators in Python: ``or``, ``and`` and ``not``. The first two enable compound boolean expressions whereas ``not`` simply negates the boolean value of any expression. To demonstrate, let's set up a couple of functions. One will evaluate to ``True`` and the other will evaluate to ``False``.

.. code-block:: ipython

	In [1]: def truthy():
	   ...:     """ This function might do any number of things....
	   ...:     query databases, make calculations, etc., but ultimately it does this: """
	   ...:     return True
	   ...:

	In [2]: def falsy():
	   ...:     return False
	   ...:

	In [3]: truthy()
	Out[3]: True

	In [4]: falsy()
	Out[4]: False

Now let's use them in expressions to see how ```and```, ```or``` and ```not``` work.

.. code-block:: ipython

	In [5]: (truthy() and falsy())  # Both must be true for the whole expression to be true
	Out[5]: False

	In [6]: (truthy() or falsy())  # Either must be true for the whole expression to be true
	Out[6]: True

	In [7]: (not (truthy() and falsy()))  # The negation of the inner expression
	Out[7]: True

	In [8]: (not (truthy() or falsy()))  # Again, the negation of the inner expression
	Out[8]: False

Summary
-------

As you can see, booleans form the basis of much of the way we control the flow of our programs, particularly when we expand the notion of True and False to include truthy and falsy. I'd suggest you spend a little time in the interpreter with the ``bool()`` function. Try calling it on different sorts of expressions, or on the return values from functions, and see what you get. And remember that you can use it during debugging whenever you're not clear on whether something is Truthy or falsy.

