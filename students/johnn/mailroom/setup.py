from setuptools import setup

setup(
    name='mailroom',
    version='1.0.0',
    author='johnn',
    author_email='jnav@uw.edu',
    packages=['mailroom', 'tests'],
    scripts=['bin/mailroom'],
    url='https://github.com/johnnzz/IntroPython-2017/tree/master/students/johnn/mailroom',
    description='Mailroom 2000',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
