.. _git:

############
Intro to Git
############

What is Git?
------------

A "version control system"

Why Version Control?
--------------------

.. figure:: ../_static/phd101212s.gif

   "Piled Higher and Deeper" by Jorge Cham: www.phdcomics.com

A history of everything everyone does to 'your' code

A graph of "states" in which the code has existed

That last one is a bit tricky, and is not necessary to understand right out of the gate. When you are ready, you can look at this supplement to gain a better understanding:

:ref:`git_overview`

There other versioning systems, such as Mercurial and Subversion (and commercial offerings), but Git is the most popular.

It is incredibly important to learn and understand versioning control to work as a developer today, so we will be incorporating Git into our work flow.


Setting up Git
--------------

You should have git installed on your machine and accessible from the command line. There will be a little bit of setup for git that you should only have to do once.

.. code-block:: bash

   $ git config --global user.name "Marie Curie"
   $ git config --global user.email "marie@radioactive.com"


Editor
------

* git needs an editor occasionally
* default is VI, which is not very intuitive to non-Unix Geeks
* Nano is simple, easy solution for Macs and Linux
* Nano no longer available for windows, use Sublime or Notepad++

For windows users:
 https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/installing/git_editor_windows.html

Once you have chosen/installed an editor, configure git to use it:

nano
``$ git config --global core.editor "nano -w"``

sublime (mac)
``$ git config --global core.editor "subl -n -w"``

sublime (win)
``$ git config --global core.editor "'c:/program files/sublime text 2/sublime_text.exe' -w"``

Notepad++ (Win)
``$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"``

Repositories
------------

A repository is just a collection of files that 'belong together'.

Since ``git`` is a *distributed* versioning system, there is no **central**
repository that serves as the one to rule them all. This simply means that all repositories should look the same.

However, to keep things sane, there is generally one "central" repository chosen that users check with for changes, for us this is GitHub.

Working with Remotes
--------------------

With git, you work with *local* repositories and *remotes* that they are connected to.

.. rst-class:: build
.. container::

   Git uses shortcuts to address *remotes*. Cloned repositories get an *origin* shortcut for free:

   .. code-block:: bash

      $ git remote -v
      origin  https://github.com/UWPCE-PythonCert/IntroPython-2017.git (fetch)
      origin  https://github.com/UWPCE-PythonCert/IntroPython-2017.git (push)

   This shows that the local repo on my machine *originated* from the one in
   the UWPCE-PythonCert gitHub account (it shows up twice, because there is
   a shortcut for both fetch from and push to this remote)

.. rst-class:: build
.. container::

    You can work on any project you wish to that has a public repository on Github. However, since you won't have permission to edit most projects directly, there is such a thing as *forking* a project.

    When you *fork* a repository, you make a copy of that repository in your own (Github) account.

    When you have made changes that you believe the rest of the community will want to adopt, you make a *pull request* to the original project. The maintainer(s) of that project than have the option of accepting your changes, in which case your changes will become part of that project.

    This is how we will be working in this class. When you want feedback on your work, you will make a *pull request* to the instructors.


Our class materials reside in a repository on *Github* in the *UWPCE-PythonCert* organization:

.. figure:: /_static/remotes_start.png
   :width: 50%
   :class: center


Note that we will be using a different repository for class assignments than the repository for the class materials (this repository).

It will be a repository that is created just for this class, and will be called IntroPython-*quarter*.

In examples below it is called IntroToPython, so replace that in your head with the name of this year's repository. :)

This new repository will include examples and we will add relevant materials (and exercise solutions) to it throughout the quarter.

There will be a folder called students at the top level, and everyone will create their own directory within it.

So, everyone will commit to this repository, and everyone will have access to everyone's code.

This will make it easier to collaborate. Weirdly enough, collaborating is important for developing code, both for class and in the *real world*.

We will do a live demo of setting up a machine for working with this repository now.

The first thing we have to do is on the Github website. We will create a fork of the class repository from the ``UWPCE-PythonCert`` account on GitHub into your personal account. Please create a gitHub account if you don't have one already.

Note: You do not have to use your real name to set up your git account.

.. figure:: /_static/remotes_fork.png
   :width: 50%
   :class: center

Everyone should now have a copy of the class repository in their account on the GitHub website.

The next step is to make a *clone* of your fork on your own computer, which means that **your fork** in github is the *origin* (Demo):

.. figure:: /_static/remotes_clone.png
   :width: 50%
   :class: center

Since you are working on a repository that you do not own, you will need to make a git shortcut to the
original repository, so that you can get changes made by other contributors before you start working.

You can add *remotes* at will, to connect your *local* repository or to other
copies of it in different remote locations.

.. rst-class:: build
.. container::

    This allows you to grab changes made to the repository in these other
    locations.

    For our class, we will add an *upstream* remote to our local copy that points to the original copy of the material in the ``UWPCE-PythonCert`` account, and we will call it, appropriately, "upstream"

    .. code-block:: bash

        $ git remote add upstream https://github.com/UWPCE-PythonCert/IntroPython2015.git

        $ git remote -v
        origin  https://github.com/PythonCHB/IntroPython2015.git (fetch)
        origin  https://github.com/PythonCHB/IntroPython2015.git (push)
        upstream    https://github.com/UWPCE-PythonCert/IntroPython2015.git (fetch)
        upstream    https://github.com/UWPCE-PythonCert/IntroPython2015.git (push)

This should leave you in a situation that looks like this:

.. figure:: /_static/remotes_upstream.png
    :width: 50%
    :class: center

To get the updates from your new remote, you'll need first to fetch everything:

.. code-block:: bash

    $ git fetch --all
    Fetching origin
    Fetching upstream
    ...

Then you can see the branches you have locally available:

.. code-block:: bash

  $ git branch -a
  * master
    remotes/origin/HEAD -> origin/master
    remotes/origin/master
    remotes/upstream/master

Finally, you can fetch and then merge changes from the upstream master.

Start by making sure you are on your own master branch:

.. code-block:: bash

    $ git checkout master

This is **really really** important. Take the time to ensure you are where you think you are, iow, that your origin is your own github repository and that you are working on master from that remote.
You can use :bash:`git remote -v` and :bash:`git branch -a` to verify.

Now, fetch the upstream master branch and merge it into your master.
You can do this in one step with:

.. code-block:: bash

  $ git pull upstream master
  Updating 3239de7..9ddbdbb
  Fast-forward
   Examples/README.rst              |  4 ++++
  ...
   create mode 100644 Examples/README.rst
  ...


Now all the changes from *upstream* are present in your local clone.
You should do this pull everytime you start to work on code.

In order to preserve the changes made by others in your fork on GitHub, you'll have to push:

.. code-block:: bash

    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 10 commits.
      (use "git push" to publish your local commits)
    $ git push origin master
    Counting objects: 44, done.
    ...
    $

(A simple ``git push`` will usually do the right thing)

You are now set up to work with this repository, and the next steps will be similar every time you work on code.

:ref:`git_workflow`

Additional Notes:

Because of the way we have set up the class, you will be able
to see all work submitted to us from everyone in the class in
the students directory on your machine. This is not a bad thing.
And the files tend to be small.

We encourage sharing of knowledge in this class. Helping your
fellow students will also help you to better understand. Share
your code, and get use to giving/receiving feedback on how to
improve your code, if you are not already.

Each repository will have a directory called ``.git`` that is normally
not seen. This directory is how git keeps track of everything. Leave it alone. :)

Please do not set up a git repository inside another git repository, this can lead to heartache.

Absolutely, do NOT set up a git repository in your home root directory.
This will put everything in your home directory up on GitHub, and you do not want that.

Setting up new repositories can be confusing because when you clone a git repository it creates
the directory that will be the repository, but when you are creating a new
repository, you need to first be **IN** the directory in which you want the
repository to be rooted. Please ask if this does not make sense.

Additional Resources:

git tutorial:
https://try.github.io/levels/1/challenges/1

basic git commands:
https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
