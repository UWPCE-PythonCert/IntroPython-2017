'''
Mailroom
Version 0.7 Feb 19, 2018
'''

from setuptools import setup

setup(name='mailroom',
      version='0.7',
      description='Simple app for managing donations for a non-profit.',
      url='https://github.com/mattbriggs',
      author='Matt Briggs',
      author_email='matt_d_briggs@hotmail.com',
      license='MIT',
      packages=['mailroom'],
      scripts=['bin/ui.py'],
      package_data={'mailroom': ['data\\mailroomdata.json']},
      install_requires=[
          'PrettyTable',
      ],
      zip_safe=False)