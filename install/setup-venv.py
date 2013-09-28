#!/usr/bin/env python2.7

# setup-env.py
# By: Samuel Maciel Sampaio <samukasmk@gmail.com> [20130928]
# Objective: Build your virtualenv sandbox with easy setup tools scripts.

import os
from setuptools import setup

orig_folder = os.path.abspath(os.path.dirname(__file__))
garbage_build_folder = os.path.join(orig_folder, 'garbage-build')

try:
    os.mkdir(garbage_build_folder)
except:
    if os.path.isdir(garbage_build_folder) == False:
        print 'Path: ' + str(garbage_build_folder) + ' exists, but is not a Folder.'
        print 'Please remove it, to continue the installation'
        raise SystemExit(1)

os.chdir(garbage_build_folder)

setup(name='MyAppExampleWithSetupToolsScripts_VirtualEnv',
      version='1.0',
      description='Example of to build your Virtualenv with Setup Tools Scripts.',
      author='Samuel Maciel Sampaio',
      author_email='samukasmk@gmail.com',
      url='https://github.com/samukasmk/setup_tools_scripts',
      install_requires=['my_package_dependency_1==1.0',
                        'my_package_dependency_2==1.2',
                        #...
                        # Real Example:
                        'requests==1.2.3',
                        'boto==2.10.0']
     )

try:
    os.rmdir(garbage_build_folder)
except:
    pass