#!/usr/bin/env python3

def func(fore_color="black", back_color="white", link_color="blue",
        visited_color="purple"):
    return (fore_color, back_color, link_color, visited_color)


def func_kwargs(*args, **kwargs):
    return func(*args, **kwargs)
