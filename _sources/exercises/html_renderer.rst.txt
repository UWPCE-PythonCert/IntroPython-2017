.. _exercise_html_renderer:

######################
HTML Renderer Exercise
######################

Ever need to generate some HTML?

And not want to write all those tags yourself?

HTML Renderer
=============

Goal:
------

The goal is to create a set of classes to render html pages -- in a "pretty printed" way.

i.e. nicely indented and human readable.

We'll try to get to all the features required to render this file:

:download:`sample_html.html  <../examples/html_render/sample_html.html>`

Take a look at it by opening it in your text editor. And also in a browser to see how it's rendered.

If you don't know html -- just look at the example and copy that. And you can read the: :ref:`html_primer` at the end of this page for enough to do this exercise.

The exercise is broken down into a number of steps -- each requiring a few more OO concepts in Python.


General Instructions:
---------------------

You can start with the framework in:

:download:`html_render.py  <../examples/html_render/html_render.py>`

For each step, add the required functionality. There is example code to run your code for each step in:

:download:`run_html_render.py  <../examples/html_render/run_html_render.py>`

You should be able to run that code at each step, uncommenting each new step in ``run_html_render.py`` as you go.

It builds up an html tree, and then calls the ``render()`` method of your element to render the page.

It uses a ``StringIO`` object (like a file, but in memory) to render to memory, then dumps it to the console, and writes a file. Take a look at the render_page function at the top of the file to make sure you understand it.

The html generated at each step will be in the files: ``test_html_ouput?.html``

Unit tests
----------

Use "test driven development":

In addition to checking if the output is what you expect with the running script -- you should also write unit tests as you go.

Each new line of code should have a test that will run it -- *before* you write that code.

That is:

  1. write a test that exercises the next step in your process
  2. run the tests -- the new test will fail
  3. write your code...
  4. run the tests. If it still fails, go back to step 3...

A start of a test file is provided here:

:download:`test_html_render.py  <../examples/html_render/test_html_render.py>`

It has a few tests for the first few steps -- uncomment them as you go along.

But it is NOT comprehensive -- you will need to add more tests at every step!

You can run ``pytest`` on that test file first thing -- it should pass two tests (that you can create an Element object --not that it works) and fail one -- one that actually starts to test functionality.

Step 1:
-------

Create an ``Element`` class for rendering an html element (xml element).

It should have class attributes for the tag name ("html" first) and the indentation (spaces to indent for pretty printing)

The initializer signature should look like

.. code-block:: python

    Element(content=None)

where ``content`` is expected to be a string -- and defaults to nothing.

It should have an ``append`` method that can add another string to the content.

(The ``html_render.py`` file you downloaded above should have a skeleton for this class in it.)

So your class will need a way to store the content in a way that you can keep adding more to it.

An ``Element`` object has to collect a bunch of sub-elements, in order, and you need to be able to append new ones to it -- sounds like a like a ``list``? So should it subclass from ``list``?

Ask yourself -- does this make sense? an "Element *is* a list" -- no.

But "An Element *uses* a list" makes perfect sense.

If the *is* phrase makes sense, then subclassing would makes sense. If the *uses* phrase makes sense, *then* you would want to subclass.

So no -- you don't want ``Element`` to subclass from list.

It should have a ``render(file_out, cur_ind = "")`` method that renders the tag and the strings in the content.

``file_out`` could be any open, writable file-like object ( i.e. have a ``write()`` method ). This is what you get from the ``open()`` function -- but there are other kinds of file-like objects. The html will be rendered to this file.

``cur_ind`` is a string with the current level of indentation in it: the amount that the entire tag should be indented for pretty printing.

 - This is a little tricky: ``cur_ind`` will be the amount that this element should be indented already. It will be from zero (an empty string) to a lot of spaces, depending on how deep it is in the tree. You could use an integer for the number of spaces to indent -- or keep it simple and just use a string with 2, or 4 or ?? spaces in it.

The amount of each level of indentation should be set by the class attribute: ``indent``

NOTE: don't worry too much about indentation at this stage -- the primary goal is to get proper, compliant html. i.e. the opening and closing tags rendered correctly. Worry about cleaning up the indentation once you've got that working. See :ref:`html_render_note_on_indentation` below for more explanation.

So this ``render()`` method takes a file-like object, and calls its ``write()`` method, writing the html for a tag. Something like::

    <html>
        Some content. Some more content.
    <\html>

You should now be able to render an html tag with text in it as content.

See: step 1. in ``run_html_render.py`` and the test code.

Step 2:
-------

Create a couple subclasses of ``Element``, for each of ``<html>``, ``<body>``, and ``<p>`` tags. All you should have to do is override the ``tag`` class attribute (you may need to add a ``tag`` class attribute to the ``Element`` class first, if you haven't already).

Now you can render a few different types of element.

Note: So why are we subclassing here? Because: "a body element *is* an ``Element``" makes perfect sense -- that's when you want to subclass. Another way to think about it is that you want to subclass to make a specialized version of something.

You may note not that the ``Element`` class really doesn't do anything by itself -- it needs a tag (at least) to be a proper element. This is what's called a "Base Class". It contains functionality required by various subclasses, but may not do anything on its own.

Extend the ``Element.render()`` method so that it can render other elements inside the tag in addition to strings. A recursion-like approach should do it. i.e. it can call the ``render()`` method of the elements it contains. You'll need to be smart about setting the ``cur_ind`` optional parameter -- so that the nested elements get indented correctly (again, this is a secondary concern...get correct html first).

Figure out a way to deal with the fact that the contained elements could be either simple strings or ``Element`` s with render methods (there are a few ways to handle that...). Think about "Duck Typing" and EAFP. See the section :ref:`notes_on_handling_duck_typing` and the end of the Exercise for more.

You should now be able to render a basic web page with an ``<html>`` tag around the whole thing, a ``<body>`` tag inside, and multiple ``<p>`` tags inside that, with text inside that. And all indented nicely.

See: :download:`test_html_output2.htm  <../examples/html_render/test_html_output2.html>`

NOTE: when you run step 2 in ``run_html_render.py``, you will want to comment out step 1 -- that way you'll only get one set of output.

Step 3:
-------

Create a ``<head>`` element -- a simple subclass.

Create a ``OneLineTag`` subclass of ``Element``:

* It should override the render method, to render everything on one line -- for the simple tags, like::

    <title> PythonClass - Session 6 example </title>

Create a ``Title`` subclass of ``OneLineTag`` class for the title.

You should now be able to render an html doc with a head element, with a
title element in that, and a body element with some ``<P>`` elements and some text.

See :download:`test_html_output3.htm  <../examples/html_render/test_html_output3.html>`

Step 4:
-------

Extend the ``Element`` class to accept a set of attributes as keywords to the
constructor, e.g. ``run_html_render.py``

.. code-block:: python

    Element("some text content", id="TheList", style="line-height:200%")

html elements can take essentially any attributes -- so you can't hard-code these particular ones (remember ``**kwargs``? )

The render method will need to be extended to render the attributes properly.

You can now render some ``<p>`` tags (and others) with attributes.

See: :download:`test_html_output4.htm  <../examples/html_render/test_html_output4.html>`


NOTE: if you do "proper" CSS+html, then you wouldn't specify style directly in element attributes.

Rather you would set the "class" attribute::

  <p class="intro">
    This is my recipe for making curry purely with chocolate
  </p>

However, if you try this as a keywork argument in Python:

.. code-block:: ipython

   In [1]: P("some content", class="intro")
   File "<ipython-input-1-7d9a6b30cd26>", line 1
     P("some content", class="intro")
                          ^
   SyntaxError: invalid syntax

Huh?

"class" is a reserved work in Python -- for making classes.
So it can't be used as a keywork argument.

But it's a fine key in a dict, so you can put it in a dict, and pass it in with ``**``:

.. code-block:: python

    attrs = {'class': 'intro'}
    P("some content", **attrs)

You could also special-case this in your code -- so your users could use "clas"
with one s, and you could tranlate it in the generated html.


Step 5:
--------

Create a ``SelfClosingTag`` subclass of Element, to render tags like::

   <hr /> and <br /> (horizontal rule and line break).

You will need to override the render method to render just the one tag and
attributes, if any.

Note that self closing tags can't have any content. Make sure that your SelfClosingTag element raises an exception if someone tries to put in any content -- probably a ``TypeError``.

Create a couple subclasses of ``SelfClosingTag`` for ``<hr />`` and ``<br />``

Note that you now have a couple render methods -- is there repeated code in them?

Can you refactor the common parts into a separate method that all the render methods can call? And do all your tests still pass (you do have tests for everything, don't you?) after refactoring?

See: :download:`test_html_output5.htm  <../examples/html_render/test_html_output5.html>`

Step 6:
-------

Create an ``A`` class for an anchor (link) element. Its constructor should look like::

    A(self, link, content)

where ``link`` is the link, and ``content`` is what you see. It can be called like so::

    A("http://google.com", "link to google")

You should be able to subclass from ``Element``, and only override the ``__init__`` --- calling the ``Element`` ``__init__`` from the  ``A __init__``

You can now add a link to your web page.

See: :download:`test_html_output6.htm  <../examples/html_render/test_html_output6.html>`

Step 7:
--------

Create ``Ul`` class for an unordered list (really simple subclass of ``Element``).

Create ``Li`` class for an element in a list (also really simple).

Add a list to your web page.

Create a ``Header`` class -- this one should take an integer argument for the
header level. i.e <h1>, <h2>, <h3>, called like

.. code-block:: python

   H(2, "The text of the header")

for an <h2> header.

It can subclass from ``OneLineTag`` -- overriding the ``__init__``, then calling the superclass ``__init__``

See: :download:`test_html_output7.htm  <../examples/html_render/test_html_output7.html>`

Step 8:
--------

Update the ``Html`` element class to render the "<!DOCTYPE html>" tag at the head of the page, before the html element.

You can do this by subclassing ``Element``, overriding ``render()``, but then calling the ``Element`` render from the new render.

Create a subclass of ``SelfClosingTag`` for ``<meta charset="UTF-8" />`` (like for ``<hr />`` and ``<br />`` and add the meta element to the beginning of the head element to give your document an encoding.

The doctype and encoding are HTML 5 and you can check this at:

http://validator.w3.org/#validate_by_input

You now have a pretty full-featured html renderer -- play with it, add some
new tags, etc....

See :download:`test_html_output8.htm  <../examples/html_render/test_html_output8.html>`

.. _html_render_note_on_indentation:

Note on Indentation
===================

Indentation is not strictly required for html -- html ignores most whitespace.

But it can make it much easier to read for humans, and it's a nice exercise to see how one might make it nice.

There is also more than one way to indent html -- so you have a bit of flexibility here.

So:

* You probably  want ``cur_ind`` to be an optional argument to render -- so it will not indent if nothing is passed in. And that lets you write the code without indentation first if you like.

* But ultimately, you want your code to USE the ``cur_ind`` parameter -- it is supposed to indicate how much this entire tag is already indented.

* When a given element gets rendered, you don't know where it is in a potentially deeply nested hierarchy -- it could be at the top level or ten levels deep. passing ``cur_ind`` into the render method is how this is communicated.

* You have (at least) two options for how to indicate level of indentation:

  - It could be a integer indicating number of levels of indentation.
  - It could, more simply, be a bunch of spaces.

* You want to have the amount of spaces per indentation defined as a class attribute of the base class (the ``Element`` class). That way, you could change it in one place, and it would change everywhere and remain consistent.

* Be sure to test that the indentation of the result changes if you change the class attribute!


.. _notes_on_handling_duck_typing:

Notes on handling "duck typing"
===============================


In this exercise, we need to deal with the fact that XML (and thus HTML) allows *either* plain text *or* other tags to be the content of a tag. Our code also needs to handle the fact that there are two possible types that we need to be able to render.

There are two primary ways to address this (and multiple ways to actually write the code for each of these).

1) Make sure that the content only has renderable objects in it.

2) Make sure the render() method can handle either type on the fly.

The difference is where you handle the multiple types -- in the render method itself, or ahead of time, when you append new content to the Element.

The ahead of time option:
-------------------------

You can handle it ahead of time by creating a simple object that wraps a string and gives it a render method. As simple as:

.. code-block:: python

  class TextWrapper:
      """
      A simple wrapper that creates a class with a render method
      for simple text
      """
      def __init__(self, text):
          self.text = text

      def render(self, file_out, current_ind=""):
          file_out.write(current_ind)
          file_out.write(self.text)


You could require your users to use the wrapper, so instead of just appending a string, they would do:

.. code-block:: python

    an_element.append(TextWrapper("the string they want to add"))

But this is not very Pythonic style -- it's OO heavy. Strings for text are so common you want to be able to simply use them:

.. code-block:: python

    an_element.append("the string they want to add")

So much easier.

To accomplish this, you can update the ``append()`` method to put this wrapper around plain strings when something new is added.


Checking if it's the right type
-------------------------------

How do you decide if the wrapper is required?

**Checking it it's an instance of Element:**

You could check and see if the object being appended is an Element:

.. code-block:: python

    if isinstance(content, Element):
        self.content.append(content)
    else:
        self.content.append(TextWrapper(content))

This would work well, but closes the door to using any other type that may not be a strict subclass of Element, but can render itself. Not too bad in this case, but in general, frowned upon in Python.


Alternatively, you could check for the string type:

.. code-block:: python

    if isinstance(content, str):
        self.content.append(TextWrapper(content))
    else:
        self.content.append(content)

I think this is a little better -- strings are a pretty core type in Python, so it's not likely that anyone is going to need to use a "string-like" object.

Duck Typing
-----------

The Python model of duck typing is: If quacks like a duck, then treat it like a duck.

But in this case, we're not actually rendering the object at this stage, so calling the method isn't appropriate.

**Checking for an attribute**

Instead of calling the method, see if it's there. You can do that with ``hasattr()``

check if the passed-in object has a ``render`` attribute:

.. code-block:: python

    if hasattr(content, 'render'):
        self.content.append(content)
    else:
        self.content.append(TextWrapper(str(content))


Note that I added a ``str()`` call too -- so you can pass in anything -- it will get stringified -- this will be ugly for many objects, but will work fine for numbers and other simple objects.

This is my favorite.


Duck Typing on the Fly
----------------------

The other option is to simply put both elements and text in the content list, and figure out what to do in the ``render()`` method.

Again, you could type check -- but I prefer the duck typing approach, and EAFP:

.. code-block:: python

    try:
        content.render(out_file)
    except AttributeError:
        outfile.write(content)

If content is a simple string then it won't have a render method, and an ``AttributeError`` will be raised.

You can catch that, and simply write the content directly instead.


You may want to turn it into a string, first::

    outfile.write(str(content))

Then you could write just about anything -- numbers, etc.


Where did the Exception come from?
----------------------------------

**Caution**

If the object doesn't have a ``render`` method, then an AttributeError will be raised. But what if it does have a render method, but that method is broken?

Depending on what's broken, it could raise any number of exceptions. Most will not get caught by the except clause, and will halt the program.

But if, just by bad luck, it has an bug that raises an ``AttributeError`` -- then this could catch it, and try to simply write it out instead. So you may get something like: ``<html_render.H object at 0x103604400>`` in the middle of your html.

**The beauty of testing**

If you have a unit test that calls every render method in your code -- then it should catch that error, and in the unit test it will be clear where it is coming from.


.. _html_primer:

HTML Primer
============


The very least you need to know about html to do this assignment.


If you are familiar with html, then this will all make sense to you. If you have never seen html before, this might be a bit intimidating, but you really don't need to know much to do this assignment.

First of all, sample output from each step is provided. So all you really need to do is look at that, and make your code do the same thing. But it does help understand a little bit about what you trying to do.

HTML
----

HTML is "Hyper Text Markup Language". Hypertext, because it can contain links
to other pages, and markup language means that text is "marked up" with
instructions about how to format the text, etc.

Here is a good basic intro:

http://www.w3schools.com/html/html_basic.asp

And there are countless others online.

As html is XML -- the XML intro is a good source of the XML syntax, too:

http://www.w3schools.com/xml/default.asp

But here is a tiny summary of just what you need to know for this project.

Elements
--------

Modern HTML is a particular dialect of XML (eXtensible Markup Language),
which is itself a special case of SGML (Standard Generalized Markup Language)

It inherits from SGML a basic structure: each piece of the document is an element. Each element is described by a "tag". Each tag has a different meaning, but they all have the same structure::

    <some_tag> some content </some_tag>

That is, the tag name is surrounded by < and >, which marks the beginning of
the element, and the end of the element is indicated by the same tag with a slash.

The real power is that these elements can be nested arbitrarily deep. In order to keep that all readable, we often want to indent the content inside the tags, so it's clear what belongs with what. That is one of the tricky bits of this assignment.


Basic tags
----------

.. code-block:: html

    <html> is the core tag indicating the entire document </html>

    <p> is a single paragraph of text </p>

    <body> is the tag that indicated the text of the document </body>

    <head> defines the header of the document -- a place for metadata </head>

Attributes:
------------

In addition to the tag name and the content, extra attributes can be attached to a tag. These are added to the "opening tag", with name="something", another_name="something else" format:

.. code-block:: html

    <p style="text-align: center" id="intro">

There can be all sorts of stuff stored in attributes -- some required for specific tags, some extra, like font sizes and colors. Note that since tags can essentially have any attributes, your code will need to support that -- doesn't it kind of look like a dict? And keyword arguments?

Special Elements
----------------

The general structure is everything in between the opening and closing tag. But some elements don't really have content -- just attributes. So the slash goes at the end of the tag, after the attributes. We can call these self-closing tags:

.. code-block:: html

   <meta charset="UTF-8" />

To make a link, you use an "anchor" tag: ``<a>``. It requires attributes to indicate what the link is:

.. code-block:: html

    <a href="http://google.com"> link </a>

The ``href`` attribute is the link (hyper reference).

lists
-----

To make a bulleted list, you use a <ul> tag (unordered list), and inside that, you put individual list items <li>:

.. code-block:: html

        <ul style="line-height:200%" id="TheList">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
        </ul>

Note that the list itself *and* the list items can both take various attributes (all tags can...)

Section Headers are created with "h" tags: <h1> is the biggest (highest level), and there is <h2>, <h3>, etc. for sections, sub sections, subsub sections...

.. code-block:: html

    <h2> PythonClass -- Example </h2>

I think that's all you need to know!
