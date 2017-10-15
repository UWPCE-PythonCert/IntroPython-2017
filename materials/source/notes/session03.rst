:orphan:

.. _notes_session03:

####################
Notes for Session 03
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Up today:

Amitkumar Chudasma

Daniel Wojciechowski

Eric V Adams

Tian Chuan Yen

Are you ready? We'll do them in the middle of the session.

Issues that came up during the week.
====================================

Separation of concerns
----------------------
From print_grid: if you are going to have separate functions, better for them to return a string, and then put all the printing in the calling function, on one place. That would make it more re-usable -- say you want to write to a file?

This is a tiny example of what's known as "separation of concerns"

Make use of symmetry
--------------------

nice trick:

.. code-block:: python

    def gene_line(char_a, char_b, n):
        line = char_a + ' ' + ((n - 1) // 2) * (char_b + ' ')
        line = line + char_a + line[::-1]



