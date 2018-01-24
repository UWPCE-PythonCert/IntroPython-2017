from setuptools import setup

setup(
	name='mailprog',
	author='Morgan H',
	packages=['mailprog'],
	include_package_data=True,
	package_data={'donors':['mailprog/data/donors.txt']},
	version="1.2",
	scripts=['bin/mailroom.py']
	)