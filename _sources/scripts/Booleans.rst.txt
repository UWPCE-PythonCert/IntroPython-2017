:orphan:

Moved to google docs

.. _script_booleans:

Booleans Video
==============

With Rick Riehle
----------------

In a certain sense there isn't much to talk about with regard to booleans. Everybody knows what the word boolean means: true of false, yes or no. When programming we're using them all the time to accomplish flow control, sometimes explicitly, often implicitly. Among Python's key or reserved words are ``True`` and ``False``.  You can test for these values explicitly when making flow control decisions.

if (3 + 3 == 6) is True:
	print("something")

Yet as often you will not need nor will you use the explicit comparison with True, because the expression within the parenthesis evaluates to True.

if (3 + 3 == 6):
	print("something")

Do we even need the comparison within the expression?

if (3 + 3):
	print("something")

Perhaps not, but what is really going on here. What if we change the expression as follows?

if (3 - 3):
	print("something")

Wait, did we get "something". Why not?

Truthy & falsy
--------------

We have taken up an idea in the programming world... truthy. We think Stephen Colbert coined the term. Truthiness, truthy and falsy. Odd sounding terms if you haven't heard them before. They sound somewhat iffy or floaty, as if Truth were hard to pin down. When we're using it in the Python world we are thinking about what Python considers equivalents of true and false. One way to test is to use the built-in function ``bool()``.

bool(3+3)
True

bool(3-3)
False

By now you are likely noticing a pattern -- something verses nothing. Something is truthy and nothing is falsy. To make it perfectly obvious....

bool(6)
True

bool(0)
False

There are a lot of expressions that evaluate to ``True`` in Python. Any non-zero value is considered ``True``. Any expression that evaluates to zero is ``False``. Indeed it may be easier to think about what evaluates to ``False`` and is therefore considered falsy, than it is to think about what is true and therefore truthy. Here is a fairly inclusive list of things that are considered falsy.

	None
	False
	zero of any numeric type, for example, 0, 0.0, 0j
	any empty sequence, for example, '', (), []
	any empty dictionary or set, for example, {}
	any object for which ``__bool__()`` returns False
	any object for which ``__len__()`` returns 0

You may not recognize ``__bool__()`` and ``__len__()``. They are Python special methods. Special methods are sometimes called dunders because their names begin and end with double underscores. The Python interpreter invokes them for you, in the background so to speak, when it needs too. Don't worry about it for now, more on dunders later.

Boolean Operations
------------------

There are three boolean operators in Python: ``or``, ``and`` and ``not``. The first two enable compound boolean expressions whereas ``not`` simply negates the boolean value of any expression. To demonstrate, let's set up a couple of functions. One will evaluate to ``True`` and the other will evaluate to ``False``.

def truthy():
	return True

def falsy():
	return False

truthy()
True

falsy()
False

Now let's use them in expressions to see how ```and```, ```or``` and ```not``` work.

(truthy() and falsy())  # Both must be true for the whole expression to be true
False

(truthy() or falsy())  # Either must be true for the whole expression to be true
True

(not (truthy() and falsy()))  # The negation of the inner expression
True

(not (truthy() or falsy()))  # Again, the negation of the inner expression
False

Summary
-------

As you can see, booleans form the basis of much of the way we control the flow of our programs, particularly when we expand the notion of True and False to include truthy and falsy. I'd suggest you spend a little time in the interpreter with the ``bool()`` function. Try calling it on different sorts of expressions, or on the return values from functions, and see what you get. And remember that you can use it during debugging whenever you're not clear on whether something is Truthy or falsy.

