#!/usr/bin/env python

from setuptools import setup

setup(
    name='pt',
    version='0.2.2',
    install_requires=[
        'Click',
        'requests'
    ],
    author='Egis Software',
    url='http://papertrail.co.za',
    description='Papertrail Command Line Utils',
    packages=['pt'],
    entry_points='''
    [console_scripts]
    pt=pt.pt:papertrail
    '''
)