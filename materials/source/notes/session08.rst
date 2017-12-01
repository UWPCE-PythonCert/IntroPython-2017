
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

Let's take a look at the past lightning talks list -- make sure we haven't missed anyone.


Issues that came up during the week.
====================================

What to test? And how?
----------------------

Make sure you test what matters about a function's result -- it's easiest (particularly if you wrote the code first) to simply match results, but your system will be more flexible if you test for the parts that matter, and won't change.

Ideally, your tests should be as isolated as possible. So if you, for instance, need to test that the correct letter is generated from a donor object, then create a donor object in the test, and pass that in, rather than using pulling it from the donor_db -- that way, the donor_db could be broken, and the individual tests will pass.

If the object(s) you need to create are complex, then you can use "fixtures" to set things up for you. We'll get into that in the next quarter.

This will start to make more and more sense as we do more testing -- and particularly when we do TDD and write the tests along with the code.

Example:
........

.. code-block:: python

    def test_p_tag():
        assert Para.tag == 'p'

I know I started out that way -- 'cause there wasn't anything else to test. But this is really testing an implementation detail -- the Para elements has a attribute named "tag" that is 'p'. But is that a public part of the API? do we care? -- No. What we care about is that the correct tag gets rendered, so a test for THAT makes more sense:

.. code-block:: python

    def test_render_para():
        my_stuff = 'spam, spam, spam'
        p = Para(my_stuff)
        more_stuff = 'eggs, eggs, eggs'
        p.append(more_stuff)
        contents = render_element(p).strip()
        assert contents.startswith('<p>')
        assert contents.endswith('</p>')
        assert my_stuff in contents
        assert more_stuff in contents


Do you always need an __init__?
-------------------------------

No -- you don't :-)

The ONLY thing "special" about __init__ is that it is automatically called when an instance is created.  Other than that, it's a regular method. So if you don't define one, then the superclass' __init__ will be called.

That's what inheritance is all about -- the subclass inherits ALL the superclasses methods -- including __init__.

So never write an __init__ that does nothing but call the superclass __init__

Subclasses and ``self``
-----------------------

``self`` is the first parameter in all methods. But why??

``self`` is the "current" instance of the object. This means that you don't know at code writing time what type it is -- is it the current class? some subclass?

Let's experiment with that.

html_render
-----------

Let's look at up to step 3....

And move along...

Lightning Talks
---------------

Circle class....





