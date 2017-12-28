#!/usr/bin/env python3

"""
kwargs exercise a thing 
"""

def fun( fore_color="blue",
        back_color="red",
        link_color="yellow",
        visited_color="green",
        **kwargs ):
    print("kwargs are:", kwargs)
    return (fore_color, back_color, link_color, visited_color)

def fun2( *args, **kwargs):
    return (args, kwargs)
