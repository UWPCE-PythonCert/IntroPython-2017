#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(name='leankitbackend',
      install_requires=['PTable>=0.8', 'xlsxwriter', 'asyncio',
                        'request', 'requests', 'aiohttp'],
      version='1.0',
      description='Python Distribution Utilities',
      author='Guillaume THOMAS',
      author_email='guillaume.thomas@dell.com',
      url='https://github.west.isilon.com/eng-tools/Lenkit_Backend',
      # packages=find_packages()
      )