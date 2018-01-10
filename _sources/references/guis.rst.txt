#########################
Graphical User Interfaces
#########################

It's likely that if you want other users to use your code that aren't system administrators and the like, that you'll want a graphical way for users to interact with your code -- a *Graphical User Interface*, or GUI.


There are now two distinct categories of GUIs:

Browser based
=============

This of for "web apps" that usually run on a server and have multiple users -- but you can use the same techniques, running the server locally and letting your user use the browser as a front end.

Advantages:
 - There is a LOT of effort going into nifty GUI stuff with Javascript in the browser, so you can leverage all that.
 - It opens the door to a server version -- if you may go that way.
 - Particularly good if you need a server and local version - same code!

Disadvantages:
- you need to write the front-end in html/Javascript -- big deal if you don't know those already.
- you need to write client-server communication code -- this can be a substantial effort, depending on complexity

Desktop GUI
===========

Use a GUI toolkit that's a python library. This gives you a traditional desktop app - GUI and rest of the code all in one.

Advantages:

 - Can have a regular old look and feel

 - Can have better performance -- no need to move data back and forth between the GUI and the app

 - can be easier to write:

    - all Python

    - no client-server communication code -- you can just access the variables.

Disadvantages:

  - none of the advantages of a browser based solution :-)

For a full-fledged app, make that choice.

Hybrid
======

Then there is a somewhat quick and dirty method:

Jupyter Notebook and Jupyter widgets.

http://jupyter.org/
http://jupyter.org/widgets.html

This is a browser-based solution, but where someone else has already written all the html/javascript for you.

A Jupyter notebook is an in browser way to mix code, documentation, and output all in one page. And with the Jupyter Widgets, you can also add graphical user input. It exposes the code to your users, which is good or bad, depending on what you want :-)

Desktop GUI options in Python
=============================

PyGTK:
  native on Unix/Linux, semi-native-ish on Windows, horribly non-native on the Mac (If you can even get it to work)

PyQT / PySide:
  wrapper around the QT framework -- almost native on all three platforms -- maybe licensing issues

TkInter:
  Comes with the standard library -- kind of klunky and not very native anywhere.

wxPython:
  Native on all three major platforms

PyGame:
  Layer on top of OpenGL for games -- not well maintained these days :-(

Native GUIs:
  Cocoa (PyObjC), PythonWin -- good if you really only care about one platform, though PYthonWin is pretty low level and klunky.

Kivy:
  for touchscreen (mobile) platforms -- not at all native, but a good option for touchscreen games.

BeeWare Toga:
  New kid on the block, seeking to be one solution for desktop and GUI -- wasn't pretty incomplete last I looked, which was a while ago.

How to decide?
--------------

With all these choices -- hard to decide.

The quickest / easiest way to get something working: tkInter -- if a Jupyter notebook is not right for your use case.

The most complete robust for Desktop GUIs: wxPYthon or PyQT if the licensing works for you (GPL, I think) PyQT is supposed to be pretty nice. I personally use wxPython (mostly for historical reasons), so a good option also.
