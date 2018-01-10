.. _context_managers:

################
Context Managers
################

**Repetition in code stinks (DRY!)**

A large source of repetition in code deals with the handling of external
resources.

As an example, how many times do you think you might type the following
code:

.. code-block:: python

    file_handle = open('filename.txt', 'r')
    file_content = file_handle.read()
    file_handle.close()
    # do some stuff with the contents

What happens if you forget to call ``.close()``?

What happens if reading the file raises an exception?


Resource Handling
-----------------

Leaving an open file handle laying around is bad enough. What if the resource
is a network connection, or a database cursor?

You can write more robust code for handling your resources:

.. code-block:: python

    try:
        file_handle = open('filename.txt', 'r')
        file_content = file_handle.read()
    finally:
        file_handle.close()
    # do something with file_content here

But what exceptions do you want to catch?  And do you really want to have to
remember to type all that **every** time you open a resource?


Starting in version 2.5, Python provides a structure for reducing the
repetition needed to handle resources like this.


**Context Managers**

You can encapsulate the setup, error handling and teardown of resources in a
few simple steps.

The key is to use the ``with`` statement.

``with`` a little help
----------------------

Since the introduction of the ``with`` statement in `pep343`_, the above six
lines of defensive code have been replaced with this simple form:

.. code-block:: python

    with open('filename', 'r') as file_handle:
        file_content = file_handle.read()
    # do something with file_content

``open`` builtin is defined as a *context manager*.

The resource it returns (``file_handle``) is automatically and reliably closed
when the code block ends.

.. _pep343: http://legacy.python.org/dev/peps/pep-0343/


At this point in Python history, many functions you might expect to behave this way do:

* ``open`` and works as a context manager.
* networks connections via ``socket`` do as well.
* most implementations of database wrappers can open connections or cursors as
  context managers.
* ...

* But what if you are working with a library that doesn't support this
  (``urllib``)?


Close It Automatically
----------------------

There are a couple of ways you can go.

If the resource in questions has a ``.close()`` method, then you can simply use
the ``closing`` context manager from ``contextlib`` to handle the issue:

.. code-block:: python

    from urllib import request
    from contextlib import closing

    with closing(request.urlopen('http://google.com')) as web_connection:
        # do something with the open resource
    # and here, it will be closed automatically

But what if the thing doesn't have a ``close()`` method, or you're creating
the thing and it shouldn't have a close() method?

(full confession: urlib.request was not a context manager in py2 -- but it is in py3)

Do It Yourself
--------------

You can also define a context manager of your own.

The interface is simple.  It must be a class that implements two
more of the nifty python *special methods*

**__enter__(self)**  Called when the ``with`` statement is run, it should
return something to work with in the created context.

**__exit__(self, e_type, e_val, e_traceback)**  Clean-up that needs to
happen is implemented here.

The arguments will be the exception raised in the context.

If the exception will be handled here, return True. If not, return False.

Let's see this in action to get a sense of what happens.

An Example
----------

Consider this code:

.. code-block:: python

    class Context(object):
        """from Doug Hellmann, PyMOTW
        https://pymotw.com/3/contextlib/#module-contextlib
        """
        def __init__(self, handle_error):
            print('__init__({})'.format(handle_error))
            self.handle_error = handle_error

        def __enter__(self):
            print('__enter__()')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
            return self.handle_error

:download:` <../examples/context_managers/context_manger.py>`

.. ``Examples/Session10/context_managers.py``

This class doesn't do much of anything, but playing with it can help
clarify the order in which things happen:

.. code-block:: ipython

    In [46]: with Context(True) as foo:
       ....:     print('This is in the context')
       ....:     raise RuntimeError('this is the error message')
    __init__(True)
    __enter__()
    This is in the context
    __exit__(<type 'exceptions.RuntimeError'>, this is the error message, <traceback object at 0x1049cca28>)

.. container::

    Because the exit method returns True, the raised error is 'handled'.


What if we try with ``False``?

.. code-block:: ipython

    In [47]: with Context(False) as foo:
       ....:     print('This is in the context')
       ....:     raise RuntimeError('this is the error message')
    __init__(False)
    __enter__()
    This is in the context
    __exit__(<type 'exceptions.RuntimeError'>, this is the error message, <traceback object at 0x1049ccb90>)
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    <ipython-input-47-de2c0c873dfc> in <module>()
          1 with Context(False) as foo:
          2     print 'This is in the context'
    ----> 3     raise RuntimeError('this is the error message')
          4
    RuntimeError: this is the error message

The ``contextmanager`` decorator
--------------------------------

``contextlib.contextmanager`` turns generator functions into context managers.

Consider this code:

.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def context(boolean):
        print("__init__ code here")
        try:
            print("__enter__ code goes here")
            yield object()
        except Exception as e:
            print("errors handled here")
            if not boolean:
                raise e
        finally:
            print("__exit__ cleanup goes here")


The code is similar to the class defined previously.

And using it has similar results.  We can handle errors:

.. code-block:: ipython

    In [96]: with context(True):
       ....:     print("in the context")
       ....:     raise RuntimeError("error raised")
       ....:
    __init__ code here
    __enter__ code goes here
    in the context
    errors handled here
    __exit__ cleanup goes here


Or, we can allow them to propagate:

.. code-block:: ipython

    In [51]: with context(False):
       ....: print("in the context")
       ....: raise RuntimeError("error raised")
    __init__ code here
    __enter__ code goes here
    in the context
    errors handled here
    __exit__ cleanup goes here
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    <ipython-input-51-641528ffa695> in <module>()
          1 with context(False):
          2     print "in the context"
    ----> 3     raise RuntimeError("error raised")
          4
    RuntimeError: error raised

You can even use context managers with ``yield``:

.. code-block:: python

    @pytest.fixture
    def example_fixture(request):
        # setup code here
        with open("a_test_filename") as test_file:
            yield test_file  # provide the fixture value

And that's it!

When the fixture is first invoked, it will yield the test_file.
It will then save the state, with the file open until ``next()``
is called again - time for the teardown.

But there is no more code after the yield -- so it falls out of the
context manager, and the file is closed.