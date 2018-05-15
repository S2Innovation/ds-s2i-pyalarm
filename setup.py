#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup
from setuptools import find_packages

setup_dir = os.path.dirname(os.path.abspath(__file__))

# make sure we use latest info from local code
sys.path.insert(0, setup_dir)

readme_filename = os.path.join(setup_dir, 'README.rst')
with open(readme_filename) as file:
    long_description = file.read()


scripts = [
  './bin/PyAlarm',
  ]

author = 'Sergi Rubio'
email = 'srubio@cells.es'
download_url = 'https://github.com/tango-controls/panic'
description = 'PyAlarm is the alarm device server'
entry_points = {'console_scripts': ['pyalarm = pyalarm.PyAlarm:main',]},

setup(
    name="pyalarm",
    version=1.0,
    author = author,
    author_email = email,
    maintainer = author,
    maintainer_email = email,
    description = description,
    long_description = long_description,
    download_url = download_url,
    packages=find_packages(),
    # entry_points=entry_points,
    scripts=scripts,
    include_package_date=True,
    license='none',
    url='www.tango-controls.org',
    platforms="All Platforms"
)