"""
This is a setup.py script originally generated by py2applet. It is ONLY 
good for building a Mac OS X applet bundle.

Usage:
    python setup-pkg.py py2app
"""

from setuptools import setup
from version import VER

VER += '.0'
APP = ['Network Remote.pyw']
DATA_FILES = ['Network Remote.help']
PLIST = {'CFBundleVersion': VER, 'CFBundleShortVersionString': VER,
         'CFBundleIdentifier': 'com.wmcbrine.networkremote',
         'CFBundleHelpBookFolder': 'Network Remote.help',
         'CFBundleHelpBookName': 'Network Remote Help',
         'NSHumanReadableCopyright': '2008-2020 William McBrine',
         'LSApplicationCategoryType': 'public.app-category.utilities'}
OPTIONS = {'includes': 'zeroconf', 'semi_standalone': False,
           'site_packages': False, 'argv_inject': ['-g', '-t'],
           'plist': PLIST, 'iconfile': 'remote.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
