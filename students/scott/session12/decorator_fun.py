#!/usr/bin/env python

def logged_func(func):
    def logged(*args, **kwargs):
        print("Function {} called".format(func.__name__))
        if args:
            print("\twith args: {}".format(args))
        if kwargs:
            print("\twith kwargs: {}".format(kwargs))
        result = func(*args, **kwargs)
        print("\t Result --> {}".format(result))
        return result
    return logged

@logged_func
def add(a, b):
    return a+b

add(6,3)

