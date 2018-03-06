#!/usr/bin/env python
"""

setup.py for mailroom app

"""

import os

from setuptools import setup

def get_version():
    """
    Reads and returns the version string the from package __init__
    """
    with open(os.path.join("mailroom", "__init__.py")) as init:
        for line in init:
            parts = line.strip().split("=")
            if parts[0].strip() == "__version__":
                return parts[-1].strip().strip("'").strip('"')
    return None

setup(
    name="mailroom",
    version=get_version(),
    author="Matt Maeda",
    author_email="matt@casamaeda.com",
    packages=['mailroom',
              'mailroom/test'],
    scripts=['bin/mailroom'],
    package_data={"mailroom": ["data/sample_data.json"]},
    license="LICENSE.txt",
    description="Mailroom app for python class",
    long_description=open("README.txt").read()
)
