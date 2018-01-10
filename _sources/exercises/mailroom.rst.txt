.. _exercise_mailroom:

############################
Mailroom: A complete program
############################

Part 1
======

Using Python's basic data types and logic for a full program.

Goal:
-----

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over and over again, so you've decided to
let Python help you out of a jam and do your work for you.

The program
-----------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each.

  You can store that data structure in the global namespace.

* The script should prompt the user (you) to choose from a menu of 3 actions:
  "Send a Thank You", "Create a Report" or "quit")

Sending a Thank You
-------------------

* If the user (you) selects 'Send a Thank You', prompt for a Full Name.

  * If the user types 'list', show them a list of the donor names and re-prompt
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
  * Once a name has been selected, prompt for a donation amount.
  * Turn the amount into a number -- it is OK at this point for the program to crash if someone types a bogus amount.
  * Once an amount has been given, add that amount to the donation history of
    the selected user.
  * Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.

It is fine (for now) to forget new donors once the script quits running.

Creating a Report
------------------

* If the user (you) selected "Create a Report", print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular (values in each column should align with those above and below)
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly.


Your report should look something like this::

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

Guidelines
----------

First, factor your script into separate functions. Each of the above
tasks can be accomplished by a series of steps.  Write discreet functions
that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use-case for the ``while`` loop.

Of course, ``input()`` will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an ``if __name__ == '__main__'`` block.

Finally, use only functions and the basic Python data types you've learned
about so far. There is no need to go any farther than that for this assignment.

Submission
----------

As always, put the new file in your student directory in a ``session03``
directory, and add it to your clone early. Make frequent commits with
good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.

.. _exercise_mailroom_plus:


Part 2: Adding dicts and Files
==============================

**Wait to do this till after you've learned about dictionaries in a later lesson!**

use dicts where appropriate
---------------------------

You should have been able to do all of the above with the basic data types:

numbers, strings, lists and tuples.

But once you've learned about dictionaries, you may be able to re-write it a bit more simply and efficiently.

 * Update your mailroom program to:

  - Use dicts where appropriate

  - See if you can use a dict to switch between the users selections.
    see :ref:`dict_as_switch` for what this means.

  - Try to use a dict and the ``.format()`` method to do the letter as one
    big template -- rather than building up a big string in parts.

Example:

.. code-block:: ipython

  In [3]: d
  Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


  In [5]: "My name is {first_name} {last_name}".format(**d)
  Out[5]: 'My name is Chris Barker'

Don't worry too much about the "**" -- we'll get into the details later, but for now it means, more or less, pass this whole dict in as a bunch of keyword arguments.

Update mailroom with file writing.
----------------------------------

Write a full set of letters to everyone to individual files on disk.

In the first version of mailroom, you generated a letter to someone who had just made a new donation, and printed it to the screen.

In this version, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter, and writes it to disk as a text file.

Your main menu may look something like::

  Choose an action:

  1 - Send a Thank You
  2 - Create a Report
  3 - Send letters to everyone
  4 - Quit

The letters should each get a unique file name -- derived from the donor's name, and maybe a date.

After running the "send letters to everyone" option, you should get a bunch of new files in the working dir -- one for each donor.

After choosing (3) above, I get these files in the dir I ran it from::

  Jeff_Bezos.txt
  Mark_Zuckerberg.txt
  Paul_Allen.txt
  William_Gates_III.txt

(If you want to get really fancy, ask the user for a directory name to write to!)

An example looks like this::

  Dear Jeff Bezos,

          Thank you for your very kind donation of $877.33.

          It will be put to very good use.

                         Sincerely,
                            -The Team

Feel free to enhance it with some more information about past generosity, etc....

The idea is to require you to structure your code so that you can write the same letter to the screen or to disk (and thus anywhere else) and also exercise a bit of file writing.


.. _exercise_mailroom_exceptions:


Part 3: Adding Exceptions and Comprehensions
============================================

**After the lesson where you learn about Exceptions**.

Exceptions
----------

Now that you've learned about exception handling, you can update your code to handle errors better -- like when a user inputs bad data.

Comprehensions
--------------

Can you use comprehensions to clean up your code a bit?

.. _exercise_mailroom_testing:

Part 4: Adding Unit Tests
=========================

**After the lesson when you learn about Unit Testing**

Add a full suite of unit tests.

"Full suite" means all the code is tested. In practice, it's very hard to test the user interaction, but you can test everything else. Make sure that there is as little untested code in the user interaction portion of the program as possible -- hardly any logic.

This is a big step -- you may find that your code is hard to test. If that's the case, it's a good sign that you *should* refactor your code.

I like to say: "If it's hard to test, it's not well structured"

Put in the tests **before** you make the other changes below - that's much of the point of tests -- you can know that you haven't broken anything when you refactor!

