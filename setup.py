#!/usr/bin/env python

import imp

from setuptools import setup, find_packages

version = imp.load_source('brunel_hand.version', 'brunel_hand/version.py')

setup(
    name='brunel_hand',
    version=version.version,
    packages=find_packages(),

    install_requires=[
        'numpy',
        'pyserial>3',
    ],

    extra_require={
        'tests': [],
    },

    author='Pollen Robotics',
    author_email='contact@pollen-robotics.com',
    description='Python library for controlling the Brunel hand by Open Bionics.',
    url='https://github.com/pollen-robotics/brunel_hand',
    license='Apache License Version 2.0',
)
