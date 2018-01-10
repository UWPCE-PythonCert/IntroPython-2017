.. _exercise_mailroom_oo:

Mailroom - Object Oriented
==========================

Making Mailroom Object Oriented.

Goal:
-----

Refactor the mailroom program using classes to help organize the code.

The goal here is the same as the earlier mailroom:

:ref:`exercise_mailroom`

But this time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple mailroom program using a
single module, a simple data structure, and functions that manipulate
that data structure.

But if one were to expand the program with additional functionality, it
would start to get a bit unwieldy and hard to maintain.

So it's a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind these three guidlines for good code structure:

1) Encapsulation: you have a data structure that holds your data, and you have functions that manipulate that data -- you want them "bundled up" in a neat package, so that the rest of the code doesn't need to know about the data structure you are using.

2) Separation of Concerns: The user interaction code should be cleanly separated from the data handling code.

   https://en.wikipedia.org/wiki/Separation_of_concerns

   There should be no `input` function in the class that holds the data!

3) As always: **DRY** -- Don't repeat yourself -- anywhere you see repeated code -- refactor it!


The program
-----------

See: :ref:`exercise_mailroom` to remind yourself what the program needs to do.


Suggestions
-----------

One of the hardest parts of OO design (particularly in Python) is to know how "low" to go with the classes and data structures. In particular, you might have a bit of data collected together (say, a donor's name and donation history), This can be a simple tuple with a few items in it, it can be a dict with those same data available as key:value pairs, or it can be a class, with class attributes (and maybe methods).

There are no hard and fast rules, but I'll try to provide guidelines:

For this assignment it's OK to go with simple tuples. However, in order for the code to be more flexible in the future, for new "fields" were added to the donor object, it's probably better to use a more structured type, so you don't have to worry about changing the order, etc of fields.

So now you have to think about dict or class? Again for flexibility, I think a dict is a bit easier -- you can add fields to it very easily. However, with a class, you can build some functionality in there, too. This is where encapsulation comes in -- for instance, one thing you might want to do is get the total of all donations a donor has made in the past. If you add a method to compute that (or a property!), then the rest of the code doesn't need to know how the donations are stored.

So: if you want my hints :-)...

You'll want a Donor class -- this will hold all the information about the donor, and have attributes and methods to provide access to the donor specific information that is needed.

You'll then want a class that handles the collection of donors. This will hold all the donor objects, but also methods to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data, this class would have that too.

your class for the collection of donors will also hold the code that generates reports about multiple donors.

In general, you will have a method for each of the functions in your non-OO version. Which class they go it will depend on whether the method only needs the information from one donor, or from the whole collection.

