:orphan:

.. _notes_session15:

############################
Notes for Quarter 2, class 5
############################


Exercises:

Look in the examples/logging foler.

In example.py, a logging system is set up that logs to a file, and also the console.

It calls a fake "application" that does things in random order, logging as it goes...

Let's go check it out!


Debugging exercise
------------------

Find the wikidef app in the examples/debugging folder

See if you can find the bug and get the app working. Use whatever debugging
technique(s) you prefer.

To run the app::

    python define.py interesting_topic

where interesting_topic is a topic of interest, like python. ;-)

Once it is working again:
Using (i)pdb in module mode (python -m pdb ) to find the name of the server and the Content-Type that
wikipedia is using by looking at response.headers in Wikipedia.article. What type of object is response.headers?

You can enter the debugger by running::

    python -m pdb ./define.py robot

(define.py takes the first sys arg and finds articles on wikipedia on that topic)

You can get to the code by walking through each line with 's'tep and
'n'ext commands, or by setting a breakpoint and 'c'ontinuing.

What's the result?

You may also want to take a look at long_loop.py and see if you can answer the questions there.

