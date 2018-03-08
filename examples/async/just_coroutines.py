#!/usr/bin/env python3

"""
Just coroutines...

Some experimental code working with coroutines by themselves, outside of an
async framework or event loop.
"""

async def corout():
    print("running corout")
    return "something returned"

# Note that the returned value gets tacked on to the StopIteration

async def corout2():
    print("running corout2")
    await corout()

# # make a coroutine
# cr = corout2()

# # run it with a send:
# cr.send(None)

# # Now we have a a coroutine with an await in it -- let's make it do a little something:

# from types import coroutine

# # applying the coroutine decorator makes a generator a coroutine, and thus
# # an awaitable object.
# @coroutine
# def do_nothing():
#     """
#     Here is one that does absolutely nothing
#     but it can be awaited.
#     """
#     yield


# # now we can make another coroutine that awaits on that:
# async def do_a_few_things(num=3):
#     # a loop for multiple things
#     for i in range(num):
#         print(f"in the loop for the {i}th time")
#         res = await do_nothing()
#         print("res is:", res)

# # create it:
# daft = do_a_few_things(5)

# # and run it:
# daft.send(None)

# # That just went into the loop:

# # to keep going, we keep calling send() until we get the StopIteration:
# while True:
#     try:
#         daft.send(None)
#     except StopIteration:
#         print("The awaitable is complete")
#         break

# # this looks a lot like generators, doesn't it?? We'll get to the difference.the

# # but first, we're passing in None to the ``.send()`` method -- it, in fact,
# # requires a value -- but what is that value used for?

# # It is "sent" as you might imagine, into the coroutine, and can be captured in
# # the coroutine from the await statement:

# # thing_sent = await awaitable

# # meanwhile, if the awaitable "returned" something -- it is passed back to the send() call.send

# # This is a while lot like generators:

# # In [104]: def gen():
# #      ...:     for i in range(3):
# #      ...:         res = yield i
# #      ...:         print(f"loop: {i}, result: {res}")
# #      ...:
# #      ...:
# #      ...:

# # In [105]: g = gen()

# # In [106]: g.send(None)
# # Out[106]: 0

# # In [107]: g.send(45)
# # loop: 0, result: 45
# # Out[107]: 1

# # In [108]: g.send(55)
# # loop: 1, result: 55
# # Out[108]: 2

# # So how does this work with coroutines?
# # You don't -- coroutines do not support sending data in - they pass out results to
# # the main loop, and then finally return something.

# # -- I can't figure out how to get the value passed in to send!

# # but we can nest these a bit, and see how each item is passed up the chain
# # one at a time.

# print("\n\n*********\n\n")


# @coroutine
# def nothing():
#     yield
#     return ("returned from nothing")


# @coroutine
# def count(num):
#     """
#     Here is one that does absolutely nothing
#     but it can be awaited.
#     """
#     for i in range(num):
#         yield f"count: {i}"

# async def do_a_few_things(num=3, name="no_name"):
#     # a loop for multiple things
#     for i in range(num):
#         print(f'in the "{name}" loop for the {i}th time')
#         from_await = await nothing()
#         print("value returned from await:", from_await)

# # create it:
# daft = do_a_few_things(5, "first one")

# # and start it off:
# daft.send(None)

# # That just went into the loop:

# # to keep going, we keep calling send() until we get the StopIteration:
# i = 0
# while True:
#     i+=1
#     print(f"{i}th time in the outer while loop")
#     try:
#         res = daft.send(i)
#         print("result of send:", res)
#     except StopIteration:
#         print("The awaitable is complete")
#         break

# # ## OK, now we have what we need to make something that might
# # # look like a task loop


# print("\n\n*********\n\n")


# @coroutine
# def nothing():
#     yield
#     return ("returned from nothing")


# @coroutine
# def count(num):
#     """
#     Here is one that does absolutely nothing
#     but it can be awaited.
#     """
#     for i in range(num):
#         yield f"count: {i}"

# async def do_a_few_things(num=3, name="no_name"):
#     # a loop for multiple things
#     for i in range(num):
#         print(f'in the "{name}" loop for the {i}th time')
#         from_await = await nothing()
#         print("value returned from await:", from_await)

# # create a bunch of tasks:
# tasks = [do_a_few_things(3, "first task"),
#          do_a_few_things(5, "second task"),
#          do_a_few_things(2, "third task"),
#          ]

# # First start tem all off:
# for task in tasks:
#     task.send(None)

# # now keep a lop going until all the tasks are gone:
# i = 0
# while tasks:
#     i += 1
#     print(f"{i}th time in the outer while loop")
#     task_copy = tasks[:]
#     tasks = []
#     for task in task_copy:
#         try:
#             res = task.send(i)
#             print("result of send:", res)
#             # put it back on the task list
#             tasks.append(task)
#         except StopIteration:
#             print("The awaitable is complete")
#             break

