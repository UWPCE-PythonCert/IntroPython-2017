.. _git:

############
Intro to Git
############

What is Git?
------------

A "version control system"

Why Version Control?
--------------------

.. figure:: http://phdcomics.com/comics/archive/phd101212s.gif

   "Piled Higher and Deeper" by Jorge Cham: www.phdcomics.com

A history of everything everyone does to 'your' code

A graph of "states" in which the code has existed

That last one is a bit tricky, and is not necessary to understand right out of the gate. When you are ready, you can look at this supplement to gain a better understanding:

:ref:`git_overview`

There other versioning systems, such as Mercurial and Subversion (and commercial offerings), but Git is the most popular.

It is incredibly important to learn and understand versioning control to work as a developer today, so we have incorporated Git into our work flow for submitting students' work in this class.


Setting up Git
--------------

You should have git installed on your machine and accessible from the command line. If you don't have git working on the command line, revisit the appropriate instructions for your platform here: :ref:`installing_python`.

Once git is installed and working, there is a little bit of setup for git that you should only have to do once:

Letting git know your identity
..............................

.. code-block:: bash

   $ git config --global user.name "Marie Curie"
   $ git config --global user.email "marie@radioactive.com"

(using your email and name, of course)

Editor
------

* git needs an editor occasionally
* default is VI, which is not very intuitive to non-Unix Geeks
* Nano is simple, easy solution for Macs and Linux
* Nano no longer available for windows, use Sublime or Notepad++

For windows users: :ref:`install_nano_win`

Once you have chosen/installed an editor, configure git to use it:

(full notes here: `GitHub help on Editors <https://help.github.com/articles/associating-text-editors-with-git/>`_)

nano:

``$ git config --global core.editor "nano -w"``

sublime (mac):

``$ git config --global core.editor "subl -n -w"``

sublime (win):

``$ git config --global core.editor "'c:/program files/sublime text 2/sublime_text.exe' -w"``

Notepad++ (Win):

``$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"``

Atom:

``git config --global core.editor "atom --wait"``

Repositories
------------

A repository is just a collection of files that 'belong together'.

Since ``git`` is a *distributed* versioning system, there is no **central**
repository that serves as the one to rule them all. This simply means that all repositories should look the same.

However, to keep things sane, there is generally one "central" repository chosen that users check with for changes. For us this is the one hosted on GitHub.

Working with Remotes
--------------------

With git, you work with *local* repositories and the *remotes* that they are connected to.

Git uses shortcuts to address *remotes*. Cloned repositories get an *origin* shortcut for free:

.. code-block:: bash

  $ git remote -v
  origin  https://github.com/UWPCE-PythonCert-ClassRepos/ClassRepoTemplate.git (fetch)
  origin  https://github.com/UWPCE-PythonCert-ClassRepos/ClassRepoTemplate.git (push)

This shows that the local repo on my machine *originated* from one in
the UWPCE-PythonCert-ClassRepos GitHub account (it shows up twice, because there is a shortcut for both fetch from and push to this remote).

GitHub forks
------------

You can work on any project you wish to that has a public repository on GitHub. However, since you won't have permission to edit most projects directly, there is such a thing as *forking* a project.

When you *fork* a repository, you make a copy of that repository in your own (GitHub) account.

When you have made changes that you believe the rest of the community will want to adopt, you make a *pull request* to the original project. The maintainer(s) of that project than have the option of accepting your changes, in which case your changes will become part of that project.

This is how we will be working in this class. When you are ready to submit an assignment, you will make a *pull request* to main class repo, and your instructors can review it.

The class repositories are on *GitHub* in the *UWPCE-PythonCert-ClassRepos* organization:

.. figure:: /_static/remotes_start.png
   :width: 50%
   :class: center

Each class with have repository created specifically for it, called something like: "Wi2018-Online".

In examples below it is called IntroToPython, so replace that in your head with the name of your classes repository.

This class repository will include examples and relevant materials (and some exercise solutions) will be added throughout the class.

There will be a folder called students at the top level, and everyone will create their own directory within it.

Note that you can use any name you want for your personal working directory -- it can be your first name, you full name, or maybe your gitHub handle if you want to remain anonymous. Just make sure you let your instructors know what name you've used so that they can credit you for your work.

Everyone will commit to this repository, and everyone will have access to everyone's code.

This will make it easier to collaborate. Weirdly enough, collaborating is important for developing code, both for class and in the *real world*.

Setting up Your Fork of the Class Repository
--------------------------------------------

The first thing we have to do is on the GitHub website. You will create a fork of the class repository from the ``UWPCE-PythonCert-ClassRepos`` account on GitHub into your personal account.

Before you can do that, you need to create a GitHub account, if you don't have one already.  Your gitHub id will be associated with this class' public repo, so it is up to you if you want to use your real name for your gitHub account, or an alias to maintain your privacy.

Once you are logged in to your gitHub account, go to the appropriate class repository here:

https://github.com/UWPCE-PythonCert-ClassRepos

Once in the repo for your class, click on the "fork" button in the upper right of the page to create a fork in your gitHub account. You will now have a copy of the class repo, and can then set up your personal machine to connect to that copy.

.. figure:: /_static/remotes_fork.png
   :width: 50%
   :class: center

Everyone should now have a copy of the class repository in their account on the GitHub website.

The next step is to make a *clone* of your fork on your own computer, which means that **your fork** in GitHub is the *origin*:

.. figure:: /_static/remotes_clone.png
   :width: 50%
   :class: center

Since you are working on a repository that you do not own, you will need to make a git shortcut to the original repository, so that you can get changes made by other contributors (i.e. the instructors and other students) before you start working.

Adding a remote
...............

You can add *remotes* at will, to connect your *local* repository to other
copies of it in different remote locations.

This allows you to grab changes made to the repository in these other
locations.

For this class, you will add an *upstream* remote to our local copy that points to the original copy of the material in the
``UWPCE-PythonCert-ClassRepos`` account, and we will call it, appropriately, "upstream"

.. code-block:: bash

    $ git remote add upstream https://github.com/UWPCE-PythonCert-ClassRepos/ClassRepoTemplate

remember to use the name of your class -- you can get the url by going to the class repo on gitHub and clicking "clone or download"

Your local setup should now look something like this:

.. code-block:: bash

    $ git remote -v
    origin  https://github.com/your_github_id/ClassRepoTemplate (fetch)
    origin  https://github.com/your_github_id/ClassRepoTemplate (push)
    upstream    https://github.com/UWPCE-PythonCert-ClassRepos/ClassRepoTemplate (fetch)
    upstream    https://github.com/UWPCE-PythonCert-ClassRepos/ClassRepoTemplate (push)

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

This is **really really** important. Take the time to ensure you are where you think you are, in other words, that your origin is your own GitHub repository and that you are working on master from that remote.
You can use `git remote -v` and `git branch -a` to verify.

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
You should do this pull every time you start to work on code.

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

Go now to this page: :ref:`git_workflow`, where you will learn what to do each time you have work to submit for review.


Privacy Note:
.............

Because of the way we have set up the class, you will be able
to see all work submitted to us from everyone in the class in
the students directory on your machine. This is not a bad thing.
And the files tend to be small.

We encourage sharing of knowledge in this class. Helping your
fellow students will also help you to better understand. Share
your code, and get used to giving / receiving feedback on how to
improve your code, if you are not already.

However, you are free to use any name you like for your working directory -- it does not have to be your real name, if you want to keep your privacy.

Structure of multiple git repos
-------------------------------

Each repository will have a directory called ``.git`` that is normally
not seen. This directory is how git keeps track of everything. Leave it alone. :)

Please do not set up a git repository inside another git repository, this can lead to heartache.

Absolutely, do NOT set up a git repository in your home root directory.
This will put everything in your home directory up on GitHub, and you do not want that.

Setting up new repositories can be confusing because when you clone a git repository it creates the directory that will be the repository, but when you are creating a new repository, you need to first be **IN** the directory in which you want the repository to be rooted. Please ask if this does not make sense.

Additional Resources:

git tutorial:
https://try.github.io/levels/1/challenges/1

basic git commands:
https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
