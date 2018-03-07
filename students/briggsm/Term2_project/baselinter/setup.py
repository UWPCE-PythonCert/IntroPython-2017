#!/usr/bin/env python

'''
Base Linter
Version 0.1 Feb 15, 2018
'''

from setuptools import setup

setup(name='Base Linter',
      version='0.1',
      description='Base linter checks for words from a list of word sets in a text.',
      long_description=open('readme.md').read(),
      url='https://github.com/mattbriggs',
      author='Matt Briggs',
      author_email='matt_d_briggs@hotmail.com',
      license='MIT',
      packages=['baselinter'],
      scripts=['baselinter\\baselinter.py'],
      package_data={'baselinter': ['data\\guide-amhomo.json']},
      install_requires=[
          'datetime',
      ],
      zip_safe=False)