Composition
===========

Composition does virtually the same thing as multiple inheritance, in the sense that it allows your class to reuse the functionality of other classes.

With inheritance you are thinking in terms of 'is-a' relationships.

With composition you are thinking in terms of 'has-a' relationships.

Composition is more explicit than inheritance and it avoids the complexity of super().  It of course also gains nothing from super()'s superpowers.

An example
----------

.. code-block:: python

    class Other(object):

        def __init__(self):
            print("Other __init__()")


    class MyComposedClass(object):
    """ I inherit from object """

        def __init__(self):
            self.other = Other()  # I contain Other()

Remember: 'has-a' not 'is-a'
