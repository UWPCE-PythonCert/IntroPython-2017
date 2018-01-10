:orphan:

Moved to Google Docs

.. _fp-intro:

#####################################
Functional Programming - Introduction
#####################################

With Rick Riehle

Programming Paradigms
=====================

Functional Programming is an alternative to Object Oriented Programming, which is to say that it takes a different perspective. As to a definition, that can be rather tricky. Definitions--by definition--are a statement of the exact meaning of a word; an exact statement or description of the nature, scope or meaning of something. I looked it up. What we're talking about here is more akin to two constellations of related ideas. I tend to picture a three dimensional space with the Functional Programming cloud here and a separate Object Oriented cloud coalescing over here. There are ideas that are somewhere in the middle between the two, and those might represent either equally shared ideas or in some cases, when you drill into them, you might find different approaches to address the one thing, the one idea. Let's think of it in another way.

Programming paradigms are like cultures. They coalesce around certain values and tend to have unique aesthetics. The people of these cultures generally need to solve the same problems, but they often find different solutions, or prefer one approach to another due to their differential weighting of cultural values. In some cases a given culture might not even recognize a problem that another culture considers among its first priorities to solve. Cultures can have variations and can mix, borrowing ideas from one another as they see fit. Let's consider an example. There is, arguably, a North American culture with Canada, Mexico and the United States interacting with each other in commerce, academics, politics and in the general exchange of ideas. However, the three clearly have distinct ways of solving problems. And then, within any one country, there are sub cultures and cross-cutting cultures. The Northwest of the United States for instance has a culture which is different from the culture in the Southwest. Indeed the Northwestern United States likely has more in common with British Columbia in Canada than it has with Florida or Alabama in the Southeastern US.

This is all to say that to try to define--to actually nail down a definition--of Object Oriented Programming, Functional Programming, or of any other paradigm is perhaps a misguided errand. It is perhaps better to think of them as constellations of ideas or as rich cultures that help you think about solutions to the problems you're trying to solve with software.

Objects and Functions
=====================

Give me one of the main ideas or the main things in OBJECT Oriented programs. I'll give you two seconds. No I won't. Objects. In python perhaps we talk and even think more often about classes, but when we instantiate a class, when we make an instance of a class, we have an object.

Give me one of the main ideas in FUNCTIONal programming. Two seconds, time's up. Functions. Since we discuss objects and classes elsewhere let's jump into functions first.

Functions
---------

Let's start with high school math. As you will recall, functions take arguments and return a value. The strict definition can be found on `Wikipedia <https://en.wikipedia.org/wiki/Function_(mathematics)>`

Function
  In mathematics, a function is a relation between a set of inputs and a set of permissible outputs with the property that each input is related to exactly one output.

So functions take arguments and return a single, deterministic output, and for a given set of arguments the same value is always returned.

Functions in Python start here, and indeed when programming according to the Functional Programming paradigm they tend to stay here and not go much beyond. Let's think about that.

Python allows us to do a lot with functions. We can return two or more values from a function for instance. This doesn't necessarily violate the stated definition, but multiple return values, even if they are returned in a tuple which as you know is immutable, might muddy the water and bring into question the deterministic aspect of the definition where each input or sets of inputs maps to exactly one output. Okay, set that in back of your mind for now.

Recall that when a "function" is defined within a class we no longer call it a function, but instead refer to it as a method. This is not an accident. The return values from methods can and indeed are typically based on data, or state information, that the class, or really, the object at this point, is carrying. That being the case we have clearly violated the textbook definition of a function. In other words, a method is explicitly not a function, even though they have the same structure and do the same sorts of things. The difference is that a method, which again is embedded in an object or class, is likely going to factor in the rest of the object's current state information when returning values, and thus we no longer have the property of a clean single input or set of inputs mapping to a single output.

Keep in mind also that Python has scoping rules that allow functions to see outside of their definitions. Let's say that a function adds i to one of its arguments before returning a value, and that i is not defined locally within the function. In that case something beyond the function could modify the value of i between calls and thus the function would return a different result. In other words your function doesn't always return the same output for a given set of inputs. This is a violation of the one-output-per-set-of-inputs mathematical definition.

In functional programming we avoid these sorts of situations. In Python, if we are to develop in a functional style, we need to be cognizant of our goals, we need to adopt the practices and habits of the culture, because Python does not force these habits upon us. It is up to us to adopt them.

Composition
===========

.. Composition is one of those equally shared ideas between the two programming paradigms we're discussing, yet it refers to completely different things between the two.

.. In some object oriented languages, Python included, you can compose classes to get features of multiple classes in one class. Indeed there is a design pattern that recommends to prefer composition over inheritance.

.. We are talking about an entirely different, though perfectly familiar type of composition when thinking from the functional perspective.


Mutability vs Immutability
==========================


Managing State
==============


Control Flow verses Data Flow
=============================


What is the point?
==================

Why does any of this matter? Good question.

In a certain sense Python doesn't take a strong stance with is programming paradigm. I mean it does in the sense that exploring the interpreter and the way objects are constructed from classes--indeed the way that EVERYthing in Python is an object that can be inspected and interacted with--in that sense it is very object oriented.

On the other hand it borrows freely and liberally from other programming languages and it doesn't get hung up on the fact that some of these language features and programming idioms come from beyond its native object orientation. In that sense it is very practical, open and un-opinionated.

But is that good? Let's think about it. The language isn't forcing upon you any particular strategies with regard to programming techniques. Instead, it's giving you tools and allowing you to make your own decisions. What could possibly go wrong? We're all adults here, right?

Some functional languages are obsessive in their management of state. They don't let you create a bunch of objects with mutating state to set them all free and loose, knocking into each other like balls on a billiard table. Instead they force you to stick to a certain programming paradigm, a certain constellation of ideas, a certain cultural approach with how to handle problems, and promise to help you handle certain types of problems easily and very well.

They tell you to favor composable functions, functions in the mathematical sense, over objects and classes.

They tell you to prefer immutability over mutability in your choices of data objects and algorithms and they give you the tools to accomplish the task.

They tell you to focus on data flow rather than control flow and they provide syntax that makes that sane and possible.

In Python ultimately it means that the choice among these techniques is yours. A long time ago one of Python's prime directives was that there should be one and preferably only one obvious way to do a thing. That's not the case anymore. The language has grown and now in some cases it gives you different syntax--multiple ways--of doing exactly the same thing.

Python leaves it to you to decide which strategy is best for your particular situation. Knowing how these constellations of ideas are related and support each other, understanding the rich cultures behind them and the problems they were designed to solve, will help you make the choice.

