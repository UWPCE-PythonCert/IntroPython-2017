#!/usr/bin/env python

def func(fore_color='red', back_color='blue', link_color='yellow', visited_color='green'):
    return (fore_color, back_color, link_color, visited_color)

def func2(*args, **kwargs):
    return (args, kwargs)


print(func())