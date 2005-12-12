#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import sys
import os
import glob
import site

# If true we'll build universal binaries on systems with the 10.4u SDK running
# OS X 10.4 or later.
# 
# NOTE: This is an experimental feature.
AUTO_UNIVERSAL = 0

# Add our utility library to the path
site.addsitedir(os.path.abspath('source-deps'))
sys.path.insert(1,
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'setup-lib')))

from pyobjc_commands import extra_cmdclass
from if_framework import *
from compile_ffi import *
from pyobjc_metadata import *
from srcpath import srcpath, modpath, libpath, buildpath

from setuptools import setup, Extension, Distribution
import os


CorePackages = ['objc']
objcExtension = Extension("objc._objc",
    FFI_SOURCE + glob.glob(modpath('objc', '*.m')),
    extra_compile_args=CFLAGS + FFI_CFLAGS,
    extra_link_args=ldflags('objc') + LDFLAGS,
)

CoreExtensions =  [objcExtension]

for test_source in glob.glob(modpath('objc', 'test', '*.m')):
    name, ext = os.path.splitext(os.path.basename(test_source))

    if name != 'ctests':
        ext = Extension('objc.test.' + name,
            [test_source],
            extra_compile_args=['-I' + modpath('objc')] + CFLAGS,
            extra_link_args=ldflags('objc'))
    else:
        ext = Extension('objc.test.' + name,
            [test_source] + FFI_SOURCE,
            extra_compile_args=['-I' + modpath('objc')] + CFLAGS + FFI_CFLAGS,
            extra_link_args=ldflags('objc') + LDFLAGS)

    CoreExtensions.append(ext)

    
pkg('CoreFoundation',
    Extension("PyObjCTools._machsignals",
        [modpath('CoreFoundation/machsignals.m')],
        extra_compile_args=['-I' + modpath('objc')] + CFLAGS,
        extra_link_args=ldflags('CoreFoundation') + LDFLAGS,
        **deps('CoreFoundation')
    ),
    no_extension=True,
    no_package=True,
)


pkg('Foundation')
pkg('AppKit')
pkg('AddressBook')
pkg('SecurityInterface')
pkg('ExceptionHandling')
pkg('PreferencePanes')
pkg('ScreenSaver', no_extension=True)
pkg('Message', no_extension=True)
pkg('InterfaceBuilder')
pkg('SenTestingKit')
pkg('WebKit')
pkg('XgridFoundation')
pkg('CoreData')
pkg('DiscRecording')
pkg('DiscRecordingUI')
pkg('SyncServices')
pkg('Automator')
pkg('QTKit')
pkg('Quartz')
pkg('OSAKit')
pkg('AppleScriptKit')

packages = ['PyObjCTools', 'PyObjCTools.XcodeSupport'] + CorePackages
extensions = [] + CoreExtensions
for name, (pkgs, exts) in PACKAGES.iteritems():
    packages.extend(pkgs)
    extensions.extend(exts)

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, libpath(pkg.replace('.', '/'))) for pkg in packages])

for aPackage in package_dir.keys():
    testDir = os.path.join(package_dir[aPackage], 'test')
    if os.path.isdir(testDir):
        packageName = '%s.test' % aPackage
        package_dir[packageName] = testDir
        packages.append(packageName)

package_dir[''] = libpath()

dist = setup(
    name="pyobjc",
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
    setup_requires=[
        "py2app>=0.3.dev-r610,==dev",
        "bdist_mpkg>=0.3,==dev",
    ],
    extras_require={
        'XcodeSupport': [
            "py2app>=0.3.dev-r610,==dev",
            "altgraph>=0.6.6,==dev",
        ],
    },
    entry_points={
        'console_scripts': [
            "nibclassbuilder = PyObjCTools.NibClassBuilder:commandline",
        ],
    },
    zip_safe=False,
)

if 'install' in sys.argv:
    import textwrap
    print textwrap.dedent(
    """
    **NOTE**

    Installing PyObjC with "setup.py install" *does not* install the following:
    
    - py2app (bdist_mpkg, modulegraph, altgraph, ...) and its tools
    - Xcode templates
    - Documentation
    - Example code

    The recommended method for installing PyObjC is to do:
        
        $ python setup.py bdist_mpkg --open

    This will create and open an Installer metapackage that contains PyObjC,
    py2app, and all the goodies!
    """)
