.. _how_to_run_a_python_file:

How to run a python file
========================

A file with python code in it is a 'module' or 'script'

(more on the distinction later on...)

It should be named with the ``.py`` extension: ``some_name.py``

If you want to run the code directly (it is a script), you have a couple options:

1) call python on the command line, and pass in your module name

.. code-block:: bash

  $ python the_name_of_the_script.py

2) On \*nix (linux, OS-X, Windows bash), you can make the file "executable"::

       chmod +x the_file.py

   And make sur it has a "shebang" line at the top::

       #!/usr/bin/env python

   Then you can run it directly::

       ./the_file.py

3) On Windows, the `.py` extensions can be associated with the python interpreter, so it can be run directly. This is clunkier than the \*nix "shebang line" approach, so don't recommend it -- but it is an option.

4) run ``iPython``, and run it from within iPython with the ``run`` command

.. code-block:: ipython

  In [1]: run the_file.py

5) Various IDEs (PyCharm, IDLE, etc) have a way to run the module you are currently editing --if you use one of these tools, learn how to do that. MAke sure that it is using the Python that you want it to be.

Making sure you are set up correctly
------------------------------------

Create a file called ``install_test.py``, with the following content:

.. code-block:: python

    #!/usr/bin/env python

    import sys
    print("This is my first python program")

    version = sys.version_info

    if version.major == 3:
        if version.minor != 6:
            print("You should be running version 3.6")
        else:
            print("You are running python3.6 -- all good!")
    else:
        print("You need to run Python 3!")
        print("This is version: {}.{}".format(version.major, version.minor))

Run it with your version of python by one (or more) of the above methods. It should result in::

    This is my first python program
    You are running python3.6 -- all good!

If you get something else -- figure out why and fix it!


