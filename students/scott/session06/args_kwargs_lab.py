#!/usr/bin/python

"""args kwargs lab exercise from session 06 of uw python class
"""

def fun(fore_color = 'blue', 
         back_color = 'red', 
         link_color = 'yellow',
         visited_color = 'green'):
    return (fore_color, back_color, link_color, visited_color)

def fun2(*args, **kwargs):
    return (args, kwargs)
