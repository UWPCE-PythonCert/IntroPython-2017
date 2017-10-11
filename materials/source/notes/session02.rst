:orphan:

.. _notes_session02:

####################
Notes for Session 02
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Up today:

Eowyn C Baughman

Po-Sung Chao

Scott B Peterson

Are you ready? We'll do them in the middle of the session.

Class Outline
=============

Let's take a look at the class outline:

https://uwpce-pythoncert.github.io/IntroPython-2017/


git / gitHub
============

In general, most of you seem to have got the basics down:

 - creating a new file
 - adding it to git
 - pushing it to your fork of the class repo
 - making a "pull request" on gitHub.

Any conceptual questions?

Let's go in and clean up Brian's fork...

Exceptions
==========

Most of you seemed to do fine making the few key exceptions -- any questions?

**Note:**

We were not expecting you to catch the exceptions -- we're really starting at the bottom here, just making sure you get used to seeing Exceptions, and what they mean.

We'll get into Exception handling later.

eval / exec
-----------

One of you used ``eval`` to demonstrate a syntax error:

.. code-block: python

    # SyntaxError test:
    def syntax_test():
        ''' This tests SyntaxError '''
        try:
            date = eval('datetime(2009, 12a, 31)')
        except SyntaxError as e:
            print("Your syntax is wrong: ", e)

Which is a nifty way to get a Syntax Error without crashing the interpreter.

But we were actually expecting you to crash the interpreter! That's kinda what syntax errors are about.

General Advice: **don't use eval or exec**

Why not?

 - dangerous!
 - unnecessary -- metaprograming! -- we'll get to that second quarter.


Coding Bat
==========

Anyone stuck on any of them?

Anyone not like their solution?

Let's talk about it!


Lightning Talks
===============

Let's take a break and do some lightning talks...

Eowyn C Baughman

Po-Sung Chao

Scott B Peterson

Now some new stuff
==================

Grid Printer
------------

Get a start on your own, then we'll come together and finish it up.

:ref:`exercise_grid_printer`

Fizz Buzz
---------

Get a start on your own, then we'll come together and finish it up.

:ref:`exercise_grid_printer`

Recursion
---------

Get a start on your own, then we'll come together and finish it up.

(seeing a pattern here?)

:ref:`exercise_fibonacci`


