:orphan:

.. _script_properties:

##########
Properties
##########

With Rick Riehle

Requires a feed to my laptop.

Status:  Filmed w Ryan on 2017-12-12


Introduction
============

Python has a unique way to manage access to object attributes.

<Outline the talk>

We are going to start with standard attributes, nothing fancy, simply define an attribute in your class and use it.  Then we're going to see some of the limitations of that.  Then we'll look at setters and getters and how they might be done in Python.  We will see limitations there too.  Finally we'll look at Properties.  Once we get to Properties we'll see that in a sense we will have come full circle back to where we started, because accessing properties is just like accessing simple attributes, yet we get the benefits of setters and getters.

<Describe the game>

I have in mind a simple game.

Fighter guy
	1.  SimpleFighterGuy
	2.  GetterSetterFighterGuy
	3.  PropertyFighterGuy

Health attribute represented as a PERCENTAGE.
	1.  An army of fighter guys!

I want to be able to interact with the attributes of my fighter guys in as straightforward a manner as possible.

To make this possible we are going to evolve our FighterGuy class from simple attributes through setters and getters to properties.


Attributes
==========

First, simple attributes.

Code!


Private attributes, Python style
--------------------------------

Python does not have any concept of public or private.  There is a convention to put a single underscore in front of attribute names, and that is a convention, a sort of coded message, from the maintainer of the class to the user or consumer of the class to leave it alone.  The maintainer of the class in effect is saying, "Use this directly at your own risk, I need this for me, it's not for you and I am making no guarantees of how it will behave in the future or even if it will exist in the future."

Code!


Setters and Getters
===================

Many languages have Setters and Getters, Java, C#, C++, Ruby, JavaScript.  Many programmers when they come to Python from these languages continue to create them and use them without taking them all the way to Python Properties.  It's a marker of someone coming in from one of these other languages and it's a sort of advanced rookie mistake.  "Oh your class has a setter and a getter... great... where are the properties?"

Code!


Properties
==========

Enter properties.  I'm going to make one simple change to this class to turn our attributes and our setter and getter into Properties and then let's see how they work.

Code!


The Property Decorator
----------------------

If you're already familiar with Python Decorators, great.  If not we will eventually get to them.  For now just follow along and know that the decorator style of doing this is exactly the same as calling the property function.  The decorator is "syntactic sugar."

Code!


Conclusion
==========

Notice how we've come full circle.  The way we access our attributes now that they have been turned into properties is exactly how we would have accessed them before when they were simple attributes -- in other words the external API, the way we access them, has not changed -- and yet we have complete control over their permissible values just as we would with setters and getters.  I can't stress this enough.  All the simplicity of standard attribute access, all the control of setters and getters, none of the awkwardness of setters and getters.
