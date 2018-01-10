.. _script_python_overview:

NOTE: now managed in Google Docs.

###############
Python Overview
###############

An overview of the Python language and ecosystem

What is Python?

Python is a programming language, I'm sure you all know that -- but there are a lot of different programming languages, all suited to different tasks.

So what makes Python special?

Python is:

* Dynamically typed
* Object oriented
* Byte-compiled
* Interpreted

But what does all that mean?

I'll go over each of these technical terms to give you an idea:


First, to reference other programming languages:

Python is not much like:

C, C++, C\#, and Java.

It is more like:

 Ruby, Lisp, Perl, and Javascript

What do these all have in common? The biggest thing is:

"Dynamic Typing"

This means variables are not declared to have a particualr type.

And that means:

  * Programs are shorter
  * Programs are more flexible

And Programs with less code have fewer bugs

I also mentioned that Python is Interpreted

This means that there is no separate compile or linking build steps.

And THAT means that the programming process is simpler and faster.

So other than not having to declare types, what really IS a Dynamic language?

Dynamic typing means that type checking and dispatch happen at run-time

For example, for a really simple line of code like:

.. code-block:: ipython

    x = a + b


The interpreter, when the code is running, goes through a process somethign like this:

* What type of thing is ``a``?
* What type of thing is ``b``?
* What does it mean to add them?

Then it actually perform the addition, and assign the new value to x.

Importantly, both the type and value of a and b can change at any time before this line of code is run.

However, Python's dynamic typing does not mean it is "weakly typed". In fact,
values in Python are Strongly typed.

At any given moment, a particular python value will have one and only one type. And that type can be checked at run time.

.. code-block:: ipython

    In [1]: a = 5

    In [2]: type(a)
    Out[2]: int

    In [3]: b = '5'

    In [4]: type(b)
    Out[4]: str

So you can see that even though b, in this case, holds text that happens to hold the digit five -- python knows that it is text (the string type), and not a number.

So EVERY value in Python has a type

And the type of the value thing determines what it can do.

Watch what happens when I try to add a and b above:


.. code-block:: ipython

    In [5]: a + b
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-5-f96fb8f649b6> in <module>()
    ----> 1 a + b

TypeError: unsupported operand type(s) for +: 'int' and 'str'

We get a type error -- it's an error because adding a number to a string is meaningless.  While a human could infer that I meant that string with teh digit 5 in it to be Interpreted as a number, and thus give me 10, Python will not change types for you.

In fact, the Python language has a Philosophy of Sorts, known as the "zen of Python", and one of its tenets is:

"In the face of ambiguity, refuse the temptation to guess.""

That is exactly what is going on here.

Despite this approach, Python's typing system is not rigid.

Python users, or "Pythonistas" as they are sometimes called, sometimes refer to Python's typing system  as "Duck Typing".

This is taken from the aphorism:

"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably IS a duck"

Or, in programming terms:

If an object behaves as expected at run-time, it's the right type.

Or, in the above example: if an object knows how to add itself to  number, then Python will add it to the number.

If this is a bit confusing, trust that it will all make more sense to you as you work with the code.

But what it does mean is that for the most part, Python code behaves pretty much as you expect it will.

One more point I'd like to bring up in this introduction:

Python Comes in multiple versions.

There is Python 2.

It is the "Classic" Python, having evolved, without breaking much from the original

And then there is Python 3 -- sometimes known as "py3k"

Python 3 is an Updated version.

It improved the language, and removed many of the "warts" Python 2 had grown over the years.

But is is NOT backward compatible, it was allowed to break code. That is, code that runs under Python 2 will not run unchanged under Python 3.

However, it still very much the same language.  Most of what you learn about Python will be applicable to either version.

This program uses Python 3 -- not Python 2

It is the latest and greatest version, and while a lot of production code is still using version 2, Adoption of Python 3 is growing fast

If you find yourself needing to work with Python 2 and 3, there are ways to write compatible code:

Here is the "official" site about it:

https://wiki.python.org/moin/PortingPythonToPy3k

And here are some other notes:


https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Py2vsPy3.html

