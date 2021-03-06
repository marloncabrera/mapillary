#!/usr/bin/python
# coding: utf8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

version = '0.0.2'
requires = [
    'pytest>=2.6.4',
    'requests>=2.5.1',
    'exifread>=2.0.0',
    'gpxpy>=0.9.8',
    'python-dateutil>=2.4.0']

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()


setup(
    name='mapillary',
    version=version,
    description="Useful tools and scripts related to Mapillary",
    long_description=readme,
    url='https://github.com/mapillary/mapillary_tools',
    download_url='https://github.com/mapillary/mapillary_tools/tarball/master',
    license=license,
    entry_points='''
        [console_scripts]
        mapillary=mapillary.cli:cli
    ''',
    packages=['mapillary'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'mapillary': 'mapillary'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='mapillary',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
