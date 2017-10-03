.. _git_workflow:

Git Workflow
============

Here is an example of the steps you should take every time you write code. In the following instructions, we 
are very explicit for those new to git/bash, so once you have created your home directory within the students 
directory, this overview may be all you need for future work.


.. code-block:: bash

    [make sure you are on correct branch]
    $ git checkout master

    [get any changes from class repository]
    $ git pull upstream master

    [if there are changes, go ahead and push them to your repository]
    $ git push

    [make sure you are in your student directory, do work]
    [verify you are happy with changes]
    $ git status

    [add your changes to what will be committed]
    $ git add .

    [add a good commit message]
    $ git commit -m 'I wrote some Python.'

    [push your changes to your remote github account]
    $ git push

    [make a pull request on the GitHub website]


In this example, we will be setting up an individual folder for yourself inside our class repository, initiated with a README. 

When you start a new project, you should create a folder within this folder for that particular project.
Note that when you start doing projects on your own, you will want to create a whole new repository for each project.

So, once you have created your directory, and are starting a new project, this will look something like this (for marie_curie working on her mailroom exercise):

students/marie_curie/mailroom

Regardless of what you are working on, first make sure you don't have anything in your repository that you forgot to commit:

.. rst-class:: build
.. container::

    .. code-block:: bash

        $ cd IntroPythonXXXX
        $ git status

Note that when git status tells you that 'Your branch is up-to-date with 'origin/master',
that does NOT mean that you are up-to-date with stuff that has been pushed to the github repository,
only, confusingly, with what your local machine currently knows about.

So, your next step is to make sure you have any changes that other people have made recently to the *remote* repository. 

    .. code-block:: bash

        $ git pull upstream master

    upstream is the name we gave to the respoitory as it sits in the UW github site. If you get an error message,
    check with the :ref:`git` documentation to make sure you set up the upstream shortcut correctly.

    master is the branch that you are currently pulling from that server,
    for the purpose of this class, we will always use master

If there are changes upstream that you do not have, it is a good idea to go ahead and push these changes to
your github account right away so they don't confuse things:

    .. code-block:: bash

        $ git push origin master

Note: A simple `git push` will usually do the right thing.

For this example, you are making your personal directory, in the future you will cd into your directory, 
and create a directory for the current project (or just cd to the current project).

    .. code-block:: bash

        $ cd students

    .. code-block:: bash

        $ mkdir marie_curie

    .. code-block:: bash

        $ cd marie_curie

Now you can do your coding. For this example, that is simply adding a readme.

    .. code-block:: bash

        $ echo "# Python code for UWPCE-PythonCert class, written by Marie Curie" >> README.rst

Once you are done coding, always a good idea to look at what you have done.

.. rst-class:: build
.. container::

    Check the status

    .. code-block:: bash

        $ git status

    Add anything you want to commit to your commit:

    .. code-block:: bash

        $ git add README.rst

    Make your commit with a summary of what you have done:

    .. code-block:: bash

        $ git commit -m 'added a readme file'

    Push your changes:

    .. code-block:: bash

        $ git push origin master

    origin is the default name given by git refering to the server you cloned (in this case your github repository)

    master is the branch that you are currently pushing to that server

Go onto GitHub, and make a pull request!

https://help.github.com/articles/creating-a-pull-request-from-a-fork/

(This will be a pull request from a fork rather than from a branch)

You've pushed your own changes to that fork, and then issued pull requests to have that work merged back to the ``UWPCE-PythonCert`` original. An instructor will look at your code, make comments and approve your pull.



