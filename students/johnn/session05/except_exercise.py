#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']

try:
    joke = fun(first_try[0])
    joke = fun(first_try[1])
except NameError:
    print("Whoops!  There is no joke for: spam")

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to next_joke.

# If there are no exceptions, call the more_fun function with the last
# language in the list regardless of whether there was an exception

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

# call more_fun() with each lang
for lang in langs:
    try:
        next_joke = more_fun(lang)
    except IndexError:
        continue
    finally:
        # it doesn't appear from the assignment sample output it was
        # envisioned this would be in a loop, so only run last_fun()
        # if we're trying the last language.
        if lang == langs[-1]:
            last_fun()
