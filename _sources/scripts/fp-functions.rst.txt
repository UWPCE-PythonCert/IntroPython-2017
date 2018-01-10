:orphan:

.. _fp-functions:

##################################
Functional Programming - Functions
##################################

With Rick Riehle

Status:  Filmed with Ryan on 2017-12-12

[Required: some fancy weatherman style overlay for the math notation?]


We have been working with functions since the early lessons of the curriculum. Let’s step back for a moment to frame them in the context of Functional Programming.

Remember from the mathematical definition that functions take arguments and return a single, deterministic output, and for a given set of arguments the same value is always returned.

Functions in Python start here, and indeed when programming according to the Functional Programming paradigm they tend to stay here and not go much beyond. Let's think about that.

[title: Multiple return values?]

Python allows us to do a lot with functions. We can return two or more values from a function for instance. This doesn't necessarily violate the stated definition, but multiple return values, even if they are returned in a tuple which as you know is immutable, might muddy the water and bring into question the deterministic aspect of the definition where each input or sets of inputs maps to exactly one output. Okay, set that in back of your mind for now.

[title: Functions versus Methods]

[Read]

Recall that when a "function" is defined within a class we no longer call it a function, but instead refer to it as a method. This is not an accident. The return values from methods can and indeed are typically based on data, or state information, that the class, or really, the object at this point, is carrying. That being the case we have clearly violated the textbook definition of a function. In other words, a method is explicitly not a function, even though they have the same structure and do the same sorts of things. The difference is that a method, which again is embedded in an object or class, is likely going to factor in the rest of the object's current state information when returning values, and thus we no longer have the property of a clean single input or set of inputs mapping to a single output.

[Show: Function vs Method example] ::

    def my_function(x, y):
        """ This is a function, because it is not a member of a class. """
        return x + y

    class MyClass(object):
        z = randint(0, 999)
        def my_method(self, x, y):
    	    """
    	    This is not a function,
    	    because it is a member of a class,
    	    and thus will likely use the class's internal state in its calculations.
    	    """
        	return x + y + self.z

[title: Scope]

[Show: Function Scope example]

Keep in mind also that Python has scoping rules that allow functions to see outside of their definitions. Let's say that a function adds i to one of its arguments before returning a value, and that i is not defined locally within the function. In that case something beyond the function could modify the value of i between calls and thus the function would return a different result. In other words your function doesn't always return the same output for a given set of inputs. This is a violation of the one-output-per-set-of-inputs mathematical definition.

[title: Functional Programming in Python is a Discipline]

In functional programming we avoid these sorts of situations. In Python, if we are to develop in a functional style, we need to be cognizant of our goals, we need to adopt the practices and habits of the culture, because Python does not force these habits upon us. It is up to us to adopt them.

[title: Functions as First Class Language Constructs]

What does it mean that this or that is a first-class language construct?

Well, in Python what do we have that are first class language constructs?

Strings. You can create them and name them or leave them unnamed. You can save them in compound, higher-order data structures such as lists and sets. You can pass them around between functions.

Lists, Tuples, Dictionaries, Sets. These are all first class language constructs.

Likewise in Python you can define functions. You can name them with def or leave them unnamed with lambda. You can save them in lists or tuples. You can pass them around to other functions. They can become members of objects as methods when you define them inside of classes… notwithstanding the definitional caveats we’ve already discussed.

Recognize that most of what we’re going to discuss in the rest of the material on functional programming would not be possible if functions were not first-class language constructs. When we’re using map, filter and reduce we’re passing functions to them. When we’re working with comprehensions we’ll be passing functions around. Closures and Decorators rely on the ability to pass functions to other functions. It’s all based on the fact that Python supports functions as first class language constructs.

[title: Composition]

Composition is one of those shared ideas between the two programming paradigms we're discussing, yet it refers to completely different things depending on the paradigm we’re discussing.

[title: Object Oriented Composition]

In some object oriented languages, Python included, you can compose classes to get features of multiple classes in one class. This is called Class or Object Composition. Indeed there’s a design pattern that says to prefer composition over inheritance.

[title: Functional Composition]

We are talking about an entirely different, though perfectly familiar type of composition when thinking from the functional perspective. Remember again from high-school math, functional composition.

[show the following simple formulas]

	y = f(x)

	z = g(y)

We don’t really need the y here. Instead we can compose the two functions together to get the result we’re looking for….

[show the additional formula along with the previous two]

	z = g(f(x))

Cleaner, easier to read, fewer moving parts.

[show this Wikipedia page: https://en.wikipedia.org/wiki/Arity]

For this to work the Arity of the functions needs to be consistent. Arity refers to the number and type of arguments to a function. In terms of math this is a science. In terms of programming I think of it as artful simplicity. It will become important when we get to closures and decorators

[show this Wikipedia page: https://en.wikipedia.org/wiki/Currying]

For this to work really well the arity of the functions involved best be reduced to one -- one argument, all of the same type.  This is called function currying or simply currying.  We'll get to it.  Consider it a sneak preview for now.

[title: Okay, enough! We get it!]

Alright. I suppose I’ve hammered on this well enough at this point: functions are important when programming in accordance with a functional programming style. And not just functions in all of Python’s flamboyant, flexible glory, but in the restrictive, technical, mathematical sense of a function. Keep it in mind as you’re working through the material.
