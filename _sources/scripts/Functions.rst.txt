Functions
=========

With Rick Riehle
----------------

We have seen some of the building blocks of programs such as basic data structures, conditional flow control statements like ``if`` and looping constructs such as ``while`` and ``for``. We can do quite a lot with these constructs alone.

Take a moment to think about what your programs will look like using only these constructs. If you are relatively new to programming this should be easy. If you've been around for awhile, you may need to forget some of what you already know for this thought experiment to work.

Using only the basic building blocks you start at the top of your program and work your way to the bottom. You likely define a few variables early on. From there you might have an ``if`` statement that conditionally executes some code block rather than some other code block. Beyond that perhaps you iterate over a list with a ``for`` loop. Maybe you load data from a database into a list of tuples and iterate over those, printing to the console the interesting bits. At the end it might be nice to print 'Done!'

Think about this in its general form. Where does execution begin and where does it end? What happens if you find yourself repeating the same code, the same series of statements, in several ``while`` or ``for`` loops. What happens if you need to change the code in one of the loops, say in response to a change in the fields returned from your database, yet forget to change the corresponding code in all of the loops?

Without a higher level construct to help organize our code it will be closer to a script than a program. Scripts are common in the automation of systems-level tasks, the type of programming used regularly by Systems Administrators and Devops Developers. To move beyond scripts we need functions.

Basic Function Definition
-------------------------

The basic form of a function is a ``def`` statement, followed by the name of the function ``addOne`` followed by an argument list ``(x)`` and finally a colon, ``:``. All of this is typically on the first line of the function definition. Then within the function are all of the statements and expressions that do the work of the function ``result = x + 1`` and finally a return value ``return result``.

.. code-block:: python

    def addOne(x):
    	result = x + 1
        return result

In simple cases such as this all of the work of the function can be done on the return line which eliminates a name ``result`` and makes the function easier to read.

.. code-block:: python

	def addOne(x):
		return x + 1

Arguments
---------

Functions can take more than a single argument.

.. code-block:: python

    def add(x, y):
    	return x + y

.. code-block:: python

    def add(x, y, z):
    	return x + y + z

Functions can have default values for arguments so that the caller can neglect to specify certain arguments and yet get reasonable defaults.

.. code-block:: ipython

	In [12]: def add(x, y=0, z=0):
	    ...:     return x + y + z
	    ...:

	In [13]: add(3)
	Out[13]: 3

	In [14]: add(3, 2)
	Out[14]: 5

	In [15]: add(3, 2, 1)
	Out[15]: 6

We snuck in an interesting and useful feature of functions in Python: keyword arguments which are often called kwargs for short. The second and third arguments to our function above have names. The first named or keyword argument is ``y`` and the second is ``z``. Note that the act itself of giving default values to arguments turns them from standard positional arguments into keyword arguments. This allows the caller to specify them by name rather than by position so that they can be called in any order. For instance, ``z`` can be specified before ``y``.

.. code-block:: ipython

	In [16]: add(0, z=1, y=2)
	Out[16]: 3

Kwargs also allow the caller to skip unneeded arguments and rely instead on their defaults.

.. code-block:: ipython

	In [17]: add(0, z=1)
	Out[17]: 1

Note however, that positional arguments cannot be skipped. In this simple case we have only one positional argument ``x`` which Python will not permit us to ignore.

.. code-block:: ipython

    In [18]: add(y=2, z=3)
    -------------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call     last)
    <ipython-input-18-5b53a9942d6b> in <module>()
    ----> 1 add(y=2, z=3)

    TypeError: add() missing 1 required positional argument: 'x'

Return Values
-------------

Functions can also take zero arguments and return nothing. Simply leave off the return statement and your function will return no value, or ``None``, to its caller.

.. code-block:: python

    def sayHello():
        print("Hello")

Interestingly, in Python functions can return more than a single value. They can return two, three, four, or indeed an arbitrary number of values. Simply place commas between the values you plan to return.

.. code-block:: ipython

	In [1]: def giveMeTwoValues():
	    ...:     return 1, "two"
	    ...:

	In [2]: first, second = giveMeTwoValues()

	In [3]: first
	Out[3]: 1

	In [4]: second
	Out[4]: 'two'

Give the return value a single name and the objects will be packed into a tuple; each object in the tuple can be accessed according to its position.

.. code-block:: ipython

	In [25]: myTwoValues = giveMeTwoValues()

	In [26]: myTwoValues
	Out[26]: (1, 'two')

	In [27]: type(myTwoValues)
	Out[27]: tuple

	In [28]: myTwoValues[0]
	Out[28]: 1

	In [29]: myTwoValues[1]
	Out[29]: 'two'

	In [30]: type(myTwoValues[0])
	Out[30]: int

	In [31]: type(myTwoValues[1])
	Out[31]: str

Scope
-----

Functions can carry variables that come into existence and go out of existence during the run of the function. This is known as scope. I could have as correctly said that these variables come into scope and go out of scope during the run of the function.

.. code-block:: ipython

	In [1]: def my_func(x=1):
	   ...:     a = "alpha"
	   ...:     b = "beta"
	   ...:     return a*x, b*x
	   ...:

	In [2]: my_func()
	Out[2]: ('alpha', 'beta')

	In [3]: my_func(2)
	Out[3]: ('alphaalpha', 'betabeta')

Variables that are defined within a function are called local variables, because they are local to the function. Note that once the function has completed executing its local variables are no longer in scope.

.. code-block:: ipython

	In [4]: a
	---------------------------------------------------------------------------
	NameError                                 Traceback (most recent call last)
	<ipython-input-4-3f786850e387> in <module>()
	----> 1 a

	NameError: name 'a' is not defined

	In [5]: b
	---------------------------------------------------------------------------
	NameError                                 Traceback (most recent call last)
	<ipython-input-5-89e6c98d9288> in <module>()
	----> 1 b

	NameError: name 'b' is not defined

Python's scoping rules are such that any variables outside the function with the same names are masked by local variables. In other words, if ``a`` and ``b`` are defined outside the function they do not interfere with the variables inside the function.

.. code-block:: ipython

	In [6]: a = "apple"

	In [7]: b = "banana"

	In [8]: my_func(2)
	Out[8]: ('alphaalpha', 'betabeta')

``my_func`` still returns alphas and betas rather than apples and bananas.

While we are still on the topic of scope and which names are available when, let's take the example above and put it into an executable python file or a script.

.. code-block:: python

	def my_func(x=1):
	    a = "alpha"
	    b = "beta"
	    return a*x, b*x

	a = "apple"

	b = "banana"

Look at the sturcutre of that code, it's physical layout. Notice how certain elements are indented under others. Notice that some are not indented at all, but rather sit along the left margin of the file. This is meaningful. The indented elements are only in scope within their enclosing blocks. Python is very explicit about this: indentation is meaningful. When Python was first created this was on of its most controversial features. Other languages used syntactic elements such as parenthesis, brackets and semi-colons to indicate structure including things like scope. Python dispensed with most of that and some people like it and some people don't. The purpose is so that as programmers, at a glance, we have clear visual clues as to what is related to what. Clues at to which symbols are in scope and when. Python also has a rigorous style guide called PEP8 which we will refer to regularly during the class. Other languages also recognize how useful these visual clues can be and so now most code editors have auto-formatting features which follow conventions, conventions like PEP8, about how code should be laid out for whatever language you happen to be working in. One nice effect of all this is that as you spend more and more time with the language the details of its syntax tends to fade into the background which allows you as the programmer to pay more attention to the problem you are trying to solve. Just as with a written language such as English or Spanish: after awhile you hardly see the syntax and you focus on the words and their meaning. The conventions around paragraph indentation give you clues about where one idea ends and another begins. So it is with computer code, particularly Python.

Python3 has two keywords for controlling scope: ``global`` and ``nonlocal``. In a sense they are for breaking the scoping rules and conventions we've talked about. Don't worry about them for now. Know they're there, and know that you can use them as a lazy way to get out of a tight spot. We will probably talk about them down the road, perhaps when we start defining functions within functions.

Summary
-------

Now think back to our thought experiment from when we started. How could the use of functions improve the way we construct programs? Perhaps most significantly we can now reduce code redundancy by factoring out repetitive code blocks as functions which can be called from wherever in our program they are needed. Moreover Where once we had to work strictly from the top of our program to the bottom we can now construct a series of functions that can be called from a main routine or from higher level functions making our program more readable.
