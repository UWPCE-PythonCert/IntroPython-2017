#!/usr/bin/env python
"""

setup.py for stock screener app

"""

import os

from setuptools import setup

def get_version():
    """
    Reads and returns the version string the from package __init__
    """
    with open(os.path.join("stockscreener", "__init__.py")) as init:
        for line in init:
            parts = line.strip().split("=")
            if parts[0].strip() == "__version__":
                return parts[-1].strip().strip("'").strip('"')
    return None

setup(
    name="screener",
    version=get_version(),
    author="Matt Maeda",
    author_email="matt@casamaeda.com",
    packages=['stockscreener',
              'exchange'],
    scripts=['bin/screener'],
    license="LICENSE.txt",
    description="Stock screener app",
    long_description=open("README.md").read()
)
