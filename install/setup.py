#!/usr/bin/env python2.7

# setup.py
# By: Samuel Maciel Sampaio <samukasmk@gmail.com> [20130928]
# Objective: Build your virtualenv sandbox with easy setup tools scripts.

import os
import subprocess
from setuptools import setup

orig_folder = os.path.abspath(os.path.dirname(__file__))
garbage_build_folder = os.path.join(orig_folder, 'garbage-build')

try:
    os.mkdir(garbage_build_folder)
except OSError:
    if os.path.isdir(garbage_build_folder) == False:
        print 'Path: ' + str(garbage_build_folder) + ' exists, but is not a Folder.'
        print 'Please remove it, to continue the installation'
        raise SystemExit(1)

os.chdir(garbage_build_folder)

setup(name='MyAppExampleWithSetupToolsScripts',
      version='1.8',
      description='Example of to build your Virtualenv with Setup Tools Scripts.',
      author='Samuel Maciel Sampaio',
      author_email='samukasmk@gmail.com',
      url='https://github.com/samukasmk/setup_tools_scripts',
      install_requires=['pip', 'virtualenv'],
     )

try:
    venv_folder = os.path.join(garbage_build_folder, '../', '../', 'venv')
    subprocess.call(['virtualenv-2.7', '--no-site-packages', venv_folder])
except OSError, error_msg:
    #print error_msg
    print '\n\nError in VirtualEnv creation:' + str(error_msg)
    print 'Please check if VirtualEnv was properly installed.'
    raise SystemExit(2)
except:
    print '\n\nError in VirtualEnv creation, please check if VirtualEnv was properly installed.'
    raise SystemExit(3)


try:
    subprocess.call([ os.path.join(venv_folder, 'bin/python'), os.path.join(orig_folder, 'setup-venv.py'), 'install'])
except:
    print '\n\Error in building Virtualenv, required packages installation failed.\nBuilding Virtualenv failed.\n\nPlease check if virtualenv was properly installed.'
    raise SystemExit(3)

try:
    os.rmdir(garbage_build_folder)
except:
    pass


my_app_example_1_src = os.path.join(orig_folder, '../', 'my_app_example1.py')
my_app_example_1_dst = '/usr/bin/my_app_example1.py'


my_app_example_2_src = os.path.join(orig_folder, '../', 'my_app_example2.py')
my_app_example_2_dst = '/usr/bin/my_app_example2'

apps_list = [
                [my_app_example_1_src, my_app_example_1_dst],
                [my_app_example_2_src, my_app_example_2_dst]
            ]


for link_app_src, link_app_dst in apps_list:

    if os.path.exists(link_app_dst) == False:
        try:
            os.symlink(link_app_src, link_app_dst)
        except Exception, e:
            print '\n\nError in Symlink Creation (' +link_app_src+ ') -> ('+link_app_dst+'): ' +str(e)
            raise SystemExit(4)

    elif os.path.islink(link_app_dst) == True and (os.readlink(link_app_dst) == link_app_src) == True:
        print 'Symlink is created - OK: (' +link_app_src+ ') -> ('+link_app_dst+')'

    else:
        try:
            os.remove(link_app_dst)
        except Exception, e:
            print '\n\nError on Removing wrong path: ('+link_app_dst+'): ' +str(e)
            print 'Please run '
            raise SystemExit(4)

        # Creates the link
        try:
            os.symlink(link_app_src, link_app_dst)
        except Exception, e:
            print '\n\nError in Symlink Creation (' +link_app_src+ ') -> ('+link_app_dst+'): ' +str(e)
            raise SystemExit(4)