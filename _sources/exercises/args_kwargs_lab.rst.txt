.. _exercise_args_kwargs_lab:

Args and Kwargs LAB
===================

Goal:
-----

Develop an understanding of using advanced argument passing and parameter definitons.

If this is all confusing -- you may want to review this:

http://stupidpythonideas.blogspot.com/2013/08/arguments-and-parameters.html

Note:

This is not all that clearly specified -- the goal is for you to
experiment with various ways to define and call functions, so you
can understand what's possible, and what happens with each call.
It is also entirely silly, since the function does not do anything 
at all, but it will teach you about using parameters effectively.

Procedure
---------

We are going to do this as test driven development. So your first task for
each assignment below is to write a test that will ensure your code does what
we are telling you it should do.

**Keyword arguments:**

* Write a function that has four optional parameters (with defaults):

  - `fore_color`
  - `back_color`
  - `link_color`
  - `visited_color`

* Have it return the colors (use strings for the colors)

* Call it with a couple different parameters set
  IOW, write tests that verify that all of the following work as advertised:
  
  - using just positional arguments:

    - ``func('red', 'blue', 'yellow', 'chartreuse')``

  - using just keyword arguments:

    -  ``func(link_color='red', back_color='blue')``

  - using a combination of positional and keyword

    -  ````func('purple', link_color='red', back_color='blue')``

  - using ``*some_tuple`` and/or ``**some_dict``

    - ``regular = ('red', 'blue')``

    - ``links = {'link_color': 'chartreuse'}``

    - ``func(*regular, *links)``


**Generic parameters:**

* Write a new function with the parameters as:

``*args`` and ``**kwargs``

* Have it return the colors (use strings for the colors)

* Call it with the same various combinations of arguments used above.

*  Also have it print `args` and `kwargs` directly, so you can be sure you understand what's going on.

* Note that in general, you can't know what will get passed into ``**kwargs`` So maybe adapt your function to be able to do something reasonable with any keywords.
