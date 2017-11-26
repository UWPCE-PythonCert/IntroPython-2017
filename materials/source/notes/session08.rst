
:orphan:

.. _notes_session08:

####################
Notes for Session 08
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

John Navitsky

Matthew Sachio Maeda

Morgan Heinemann


Issues that came up during the week.
====================================

What to test? And how?
----------------------

Make sure you test what matters about a function's result -- it's easiest (particularly if you wrote the code first) to simply match results, but your system will be more flexible if you test for the parts that matter, and won't change.

Ideally, your tests should be as isolated as possible. So if you, for instance, need to test that the correct letter is generated from a donor object, then create a donor object in the test, and pass that in, rather than using pulling it from the donor_db -- that way, the donor_db could be broken, and the individual tests will pass.

If the object(s) you need to create are complex, then you can use "fixtures" to set things up for you. We'll get into that in the next quarter.

This will start to make more and more sense as we do more testing -- and particularly when we do TDD and write the tests along with the code.

do you always need an __init__?
------------------------------

No -- you don't :-)

The ONLY thing "special" about __init__ is that it is automatically called when and instance is created.  Other than that, it's a regular method. So if you don't define one, then the superclass' __init__ will be called.

That's what inheritance is all about -- the subclass inherits ALL the superclasses methods -- including __init__.

So never write an __init__ that does nothing but call the superclass __init__


Bad OO design
-------------

Script from work...depersonalized

In class repo: ``examples/session08/unnecessary_oo.py``

Recall Jack Dietrich's talk: "Stop Writing Classes":

Also PEP8, etc....

let's do a code review.







