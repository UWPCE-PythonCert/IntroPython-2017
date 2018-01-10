#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        pass

    def append(self, new_content):
        pass

    def render(self, file_out, cur_ind=""):
        file_out.write("just something as a place holder...")
