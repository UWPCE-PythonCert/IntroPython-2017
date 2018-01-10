.. _python_for_windows:

#############################
Setting up Windows for Python
#############################

Getting The Tools
==================

Python
-------

There are a number of Python distributions available -- many designed for easier support of scientific programming:

- Anaconda
- Enthought Canopy
- Python(x,y)
- etc....

But for basic use, the installer from python.org is the way to go, and that is what we will be using in this program.

https://www.python.org/downloads/

You want the installer for Python 3.6 -- probably 64 bit, though if you have a 32 bit system, you can get that.
There is essentially no difference for the purposes of this course.

Double click and install.


Terminal
---------

If you are confident in your use of the "DOS Box" or "powershell", command lines, feel free to use one of those. However, your life may be easier if you install "Git Bash", as then you can follow unix-style terminal instructions exactly, and do not have to translate. Also, your instructors are more experienced with Bash.

From now on, if you hear the terms "bash", "shell" or "terminal", or "commandline" know that this is the application that is being referred to. We will use those tems interchangably to mean ANY command line.

When you install Git Bash, you are installing git (and a git gui) as well, thus killing two birds with one stone!

https://git-for-windows.github.io/

You can use this git with the DOS box or Powershell as well.

This is also a good bet for running Python -- If you use the Git Bash shell, you can use the same commands as Linux and OS-X users. Regardless of which shell you choose, you will need to add Python to your environment. It is possible that this was done during the installation of Python. If you type 'which python' into your terminal, and get back the answer '/c/python34/python', then you are good to go, otherwise, follow the instructions here:

http://www.computerhope.com/issues/ch000549.htm

You will want to add:

``C:\Python36``

and

``C:\Python36\Scripts``

to ``PATH``

Once you have done that, you should be able to type ``python`` at the command prompt, and get something like:

::

  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  [GCC 4.2.1 (Windows build 7584) (dot 3)] on win64
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

This is the Python interpreter.

Type ``ctrl+Z`` to get out (or ``exit()``)


git
----

If you installed Git Bash, you will already have git, both usable in the terminal and as a gui, and can safely skip this section. If not, you still need a git client. You can use the above link and install git (it will install the bash shell as well, of course, but you can use your shell of choice instead).

There is also TortoiseGit:

https://code.google.com/p/tortoisegit/

which integrates git with the file manager. Feel free to use this if you already have an understanding of how git works, but for the purposes of learning, it may be better to use a command line client (git Bash above).


pip
---

``pip`` is the Python package installer. It is updated faster than Python itself, so once you have Python you want to get the latest version of pip working::

  $ python -m ensurepip --upgrade

It should download and install the latest ``pip``.

You can now use pip to install other packages.

Using pip:
----------

To use pip to install a package, you invoke it with this command::

  python -m pip install the_name_of_the_package

Where ``python`` is the command you use to invoke the Python you want to use (could be ``python3``)

**NOTE:** You will frequently see advice to use pip like so::

  $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

  $ python -m pip install something_or_other

calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of Python that you are running.


iPython
--------

One extra package we are going to use from the beginning in the program is ``iPython``::

  $ python -m pip install ipython[all]

(It will install a LOT -- if it fails, try leaving the ``[all]`` off)

You should now be able to run ``iPython`` from the git bash shell::

    $ ipython
    Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
    (or from the DOS box or PowerShell prompt)

We will use this as our default Python interpreter.


Testing it out
--------------

To be ready for the program, you need to have:
 - python
 - pip
 - iPython
 - git

All available from the command line.

To try it out, you should be able to run all of these commands, and get something like the following results:

(recall that you can get out of the python or iPython command lines with ``ctrl+Z``)

For Python:

::

  MacBook-Pro:PythonCertDevel Chris$ python
  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> ^D

For iPython:

::

  MacBook-Pro:PythonCertDevel Chris$ ipython
  Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  Type 'copyright', 'credits' or 'license' for more information
  IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

  In [1]:

  Do you really want to exit ([y]/n)? y

For pip:

::

  MacBook-Pro:PythonCertDevel Chris$ python -m pip --version
  pip 9.0.1 from /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (python 3.6)

For git:

::

  MacBook-Pro:PythonCertDevel Chris$ git --version
  git version 2.11.0 (Apple Git-81)
