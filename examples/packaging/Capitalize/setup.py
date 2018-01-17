#!/usr/bin/env python

"""
This is about as simple a setup.py as you can have

It installs the capitalize module and script

"""

import os
from setuptools import setup


def get_version():
    """
    Reads the version string from the package __init__ and returns it
    """
    with open(os.path.join("capitalize", "__init__.py")) as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None


setup(
    name='Capitalize',
    version=get_version(),
    author='Chris Barker',
    author_email='PythonCHB@gmail.com',
    packages=['capitalize',
              'capitalize/test'],
    scripts=['bin/cap_script'],
    license='LICENSE.txt',
    description='Not very useful capitalizing module and script',
    long_description=open('README.txt').read(),
)
