from setuptools import setup

setup(
   name='mailroom',
   version='0.1.0',
   author='Eowyn',
   author_email='aac@example.com',
   packages=['mailroom'],
   scripts=['bin/mailroom'],
   url='https://github.com/Eowyn42/IntroPython-2017/tree/master/students/eowyn/session10',
   #license='LICENSE.txt',
   description='Donation manager',
   #long_description=open('README.txt').read(),
   install_requires=[
       "pytest",
   ],
)
