#!/usr/bin/env python

import os

from setuptools import setup

def get_version():
    """read the version string from the package and returns it"""
    with open(os.path.join("labyrinth", "__init__.py")) as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None

setup(
    name='labyrinth',
    version=get_version(),
    author='Tian Yen',
    author_email='tianchu@uw.edu',
    packages=['labyrinth',
              'labyrinth/test'],
    scripts=['bin/labyrinth'],
    package_data={'labyrinth': ['sprites/end_rect.png',
                                'sprites/panda_player.png',
                                'sprites/wall.png']},
    license='LICENSE.txt',
    description='Simple labyrinth game',
    long_description=open('README.rst').read(),
)
