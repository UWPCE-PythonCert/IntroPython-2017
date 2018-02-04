:orphan:

.. _notes_session14:

############################
Notes for Quarter 2, class 4
############################

Questions that came up
======================

More on Decorators
------------------

Eric found this decorator in *Core Python Programming* by Wesley Chun.

.. code-block:: Python

    #! /usr/bin/env python

    from time import time

    def logged(when):
        def log(f, *args, **kargs):
            print('''Called
                function: %s
                args: %r
                kargs: %r''' % (f, args, kargs))

        def pre_logged(f):
            def wrapper(*args, **kargs):
                log(f, *args, **kargs)
                return f(*args, **kargs)
            return wrapper

        def post_logged(f):
            def wrapper(*args, **kargs):
                now = time()
                try:
                    return f(*args, **kargs)
                finally:
                    log(f, *args, **kargs)
                    print("time delta: %s" % (time() - now))
            return wrapper

        try:
            return {"pre": pre_logged,
                    "post": post_logged}[when]
        except KeyError as e:
            raise (ValueError(e), 'must be "pre" or "post" ')


    @logged("post")
    def hello(name):
        print("Hello, ", name)

    hello("World")

There's a lot of layers of nesting in there -- let's figure it out!

Context Managers
----------------

Any questions?

Let's take a look at my solutions.


