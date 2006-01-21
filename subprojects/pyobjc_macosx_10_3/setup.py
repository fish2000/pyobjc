#!/usr/bin/env python

import os, sys
__file__ = os.path.abspath(__file__)
dn = os.path.dirname
SRCDIR = dn(dn(dn(__file__)))
sys.path.insert(0, SRCDIR)
os.chdir(SRCDIR)

import ez_setup
ez_setup.use_setuptools()

import sys
import os
import glob
import site

# Add our utility library to the path
site.addsitedir(os.path.abspath('source-deps'))
sys.path.insert(1, 'setup-lib')

from pyobjc_commands import extra_cmdclass
from if_framework import *
from compile_ffi import *
from pyobjc_metadata import *
from srcpath import srcpath, modpath, libpath, buildpath

from setuptools import setup
import os


pkg('Foundation')
pkg('AppKit')
pkg('AddressBook')
pkg('SecurityInterface')
pkg('ExceptionHandling')
pkg('PreferencePanes')
pkg('ScreenSaver', no_extension=True)
pkg('Message', no_extension=True)
pkg('InterfaceBuilder')
pkg('WebKit')

packages = []
extensions = []
for name, (pkgs, exts) in PACKAGES.iteritems():
    packages.extend(pkgs)
    extensions.extend(exts)

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, libpath(pkg.replace('.', '/'))) for pkg in packages])

package_dir[''] = libpath()

dist = setup(
    name="pyobjc_macosx_10_3",
    version=package_version(),
    description="Python<->ObjC Interoperability Module",
    long_description=LONG_DESCRIPTION,
    author="bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email="pyobjc-dev@lists.sourceforge.net",
    url="http://pyobjc.sourceforge.net/",
    platforms=['MacOS X'],
    ext_modules=extensions,
    packages=packages,
    package_dir=package_dir,
    cmdclass=extra_cmdclass,
    classifiers=CLASSIFIERS,
    license='MIT License',
    download_url='http://pyobjc.sourceforge.net/software/index.php',
    setup_requires=["pyobjc_core"],
    install_requires=["pyobjc_core"],
    entry_points={
        'console_scripts': [
            "nibclassbuilder = PyObjCTools.NibClassBuilder:commandline",
        ],
    },
    zip_safe=False,
)
