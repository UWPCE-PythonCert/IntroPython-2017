.. _exceptions:

##################
Exception Handling
##################

Exceptions are a really nifty Python feature -- really handy!

From the zen:

"Errors should never pass silently."

"Unless explicitly silenced."

That's what exception handling is all about.

Exceptions
----------

An "Exception" is an indication that something out of the ordinary (exceptional) happened.

Note that they are NOT called "Errors" -- often they are, but often it's not an indication of an error per se.

This is why we have exception handling -- because we often know that exceptions will occur, and know how to handle them -- we don't want the program to crash out.

Handling Exceptions
-------------------

Exceptions are handled with a "try -- except" block.

This provides another branching structure (kind of like if) -- a way for different code to run depending on what happens.

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")

bare ``except``
---------------

*Never* do this:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except:
        print "couldn't open missing.txt"

If you don't specify a particular exception, ``except`` will catch *All* exceptions.

**Always** capture the *particular* Exception(s) you know how to handle.

Trust me, you can't anticipate everything, and you want the exception to propagate if it is not expected when you wrote the code.


Testing for errors "by hand":
-----------------------------

Use Exceptions, rather than your own tests:

Don't do this:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)

It will almost always work -- but the almost will drive you crazy.

It is "possible" that the file got deleted by another process in the precise moment between checking for it and opening it. Rare, but possible. But catching the exception will always work.


Example from mailroom exercise:
-------------------------------

You want to convert the user's input into an integer. And you want to give a nice message if the user didn't provide a valid input.

So you could do this:

.. code-block:: python

    if num_in.isdigit():
        num_in = int(num_in)

But -- ``int(num_in)`` will only work if the string can be converted to an integer.

So you can do

.. code-block:: python

    try:
        num_in = int(num_in)
    except ValueError:
        print("Input must be an integer, try again.")

This is particularly helpful for things like converting to a float -- much more complicated to check -- and all that logic is already in the ``float()`` constructor.

Or let the Exception be raised if you can't handle it.

EAFP
----

This is all an example of the EAFP principle:

"It's Easier to Ask Forgiveness than Permission"

 -- Grace Hopper

The idea is that you want to try to do what you want to do -- and then handle it if it doesn't work (forgiveness).

Rather than check to see if you can do it before trying (permission).

Here's a nice PyCon talk by Alex Martelli about that:

http://www.youtube.com/watch?v=AZDWveIdqjY

(Alex Martelli is a Python Luminary -- read / watch anything you find by him).


Do you catch all Exceptions?
----------------------------

For simple scripts, let exceptions happen.

Only handle the exception if the code can and will do something about it.

This results in much better debugging info when an error does occur.  The user will see the exception, and where in the code it happened, etc.


Exceptions -- finally
---------------------

There is another control structure to exceptions:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")
    finally:
        do_some_clean-up

The ``finally:``  clause will always run.

This is really important if your code does anything before the exception occurred that needs to be cleaned up -- open database connection, etc...


Exceptions -- ``else``
----------------------

Yet another flow control option:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError:
        print("couldn't open missing.txt")
    else:
        process(f) # only called if there was no exception

So the ``else`` block only runs if there was no exception. That was also the case in the previous code, so what's the difference?

**Advantage of ``else``:**

Using the ``else`` block lets you catch the exception as close to where it occurred as possible -- always a good thing.

Why? -- because maybe the "process(f)" could raise an exception, too? Then you don't know if the exception came from the ``open()`` call or in some code after that.

This bears repeating:

**Always catch exceptions as close to where they might occur as you can**.

Exceptions -- using the exception object
----------------------------------------

What can you do in an ``except`` block?

If your code can continue along fine, you can do very little and move along:

.. code-block:: python

    try:
        do_something()
    except ValueError:
        print("That wasn't any good")

And that's that.

But if your code *can't* continue on, you can re-raise the exception:

.. code-block:: python

    try:
        do_something()
    except ValueError:
        print("That wasn't any good")
        raise

The ``raise`` statement will re-raise the same exception object, where it may get caught higher up in the code, or even end the program.

Exception objects are full-fledged Python objects -- they can contain data, and you can add data to them:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError as the_error:
        print(the_error)
        the_error.extra_info = "some more information"
        raise

This prints the exception, then adds some extra information to it, and then re-raises the same exception object -- so it will have that extra data when it gets handled higher up on the stack.

This is particularly useful if you catch more than one exception:

.. code-block:: python

    except (IOError, BufferError, OSError) as the_error:
        do_something_with(the_error)

You may want to do something different depending on which exception it is.

Multiple Exceptions
-------------------

As seen above, you can catch multiple exceptions in an ``except`` statement

If you want to do something completely different with each exception type, you can have multiple ``except`` blocks:

.. code-block:: python

    try:
       some_code
    except IOError:
        handle_the_error
    except BufferError:
        handle_the_error
    except OSError:
        handle_the_error

So a full-featured ``try`` block has all of this:

.. code-block:: python

    try:
       some_code
    except IOError:
        handle_the_error
    except BufferError:
        handle_the_error
    ...
    else:
        some code to run if none of these exceptions occurred
    finally:
        some code to run always.

The minimal try block as a ``try``, and one ``except``.

Raising Exceptions
-------------------

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("b can not be zero")
        else:
            return a / b

(OK, this is a stupid example, as that error will be raised for you anyway. but bear with me).

When you call it:

.. code-block:: ipython

    In [515]: divide (12,0)
    ZeroDivisionError: b can not be zero

note how you can pass a message to the exception object constructor. It will get printed when the exception is printed.


Built in Exceptions
-------------------

You can create your own custom exceptions.

But...

.. code-block:: python

    exp = \
     [name for name in dir(__builtin__) if "Error" in name]
    len(exp)
    48

For the most part, you can/should use a built in one.

There are 48 built-in Exceptions -- odds are good that there's one that matches your use-case.

Also -- custom exceptions require subclassing -- and we haven't learned that yet :-).


Choosing an Exception
---------------------

Choose the best match you can for the built in Exception you raise.

Example::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise ValueError

Is it the *value* or the input the problem here?

Nope: the *type* is the problem::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise TypeError

but should you be checking type anyway? (EAFP)

What I usually do is run some code that's similar that raises a built-in exception, and see what kind it raises, then I use that.

Knowing what Exception to catch
-------------------------------

I usually figure out what exception to catch with an iterative process.

I write the code without a try block, pass in "bad data", or somehow trigger the exception, then see what it is.

Example:

What if the file I want to read doesn't exist?

.. code-block:: ipython

    In [7]: open("some_non_existant_file")
    ---------------------------------------------------------------------------
    FileNotFoundError                         Traceback (most recent call last)
    <ipython-input-7-a18e010ecdd0> in <module>()
    ----> 1 open("some_non_existant_file")

    FileNotFoundError: [Errno 2] No such file or directory: 'some_non_existant_file'

Now I know to use::

    except  ``FileNotFoundError``:

In the ``try`` block where I am opening the file.





