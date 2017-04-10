"""Setuptools installation script for the babou package."""

import os
from setuptools import setup, find_packages


# Root directory of project (== directory of script)
root_dir = os.path.dirname(__file__)


# Read readme file for long description
with open(os.path.join(root_dir, 'README.md')) as fobj:
	readme_contents = fobj.read()


setup(
	name='babou',
	version='0.0.1',
	description='Implementation of the surreal numbers in Python.',
	long_description=readme_contents,
	url='https://github.com/jlumpe/babou',
	author='Jared Lumpe',
	author_email='mjlumpe@gmail.com',
	keywords='surreal numbers math',
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Education',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Education',
		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Mathematics',
	],
	packages=find_packages(),
)
