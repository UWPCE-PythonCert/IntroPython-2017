
:orphan:

.. _notes_session07:

####################
Notes for Session 07
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Brian Nagata

Rajaramesh V Yaramati

Zandra Eng


Issues that came up during the week.
====================================

Mutating vs. re-assigning
-------------------------

I've seen code like this in a few trigram solutions::

  output = output + [follower]

(``output`` is a list of strings, follower is a single string)

What it does is add a new item to a list.

But is that an efficient way to do that?

If you are adding one element to a list -- append() is the way to go. This works fine, but it's creating a whole new list just to throw it away again:

output_list.append (random_trigram_followers)

and if you are adding another list of objects, you want to use extend(). The way it is now, you are actually doing:

1) create a list with random_trigram_followers in it.
2) create a new list with the contents of output_list the new list.
3) re-assign the name output_list to that new list.
4) throw away the original output_list and the temporary list you created for random_trigram_followers

That's a LOT of overhead!

Be cognizant of when you are mutating (changing) an object vs creating a new one and assigning it to the same name. When you do assignment (=) you are probably creating a new object.


+= is different -- it is the "in_place" operator, so:

a_list += another_list

does not create an new lists -- it adds to the original list "in place" -- it is identical to:

a_list.extend(another_list)

And is an efficient operation.
