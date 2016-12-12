'''
Wrappers for the "Photos" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-Photos',
    version="3.2.1",
    description = "Wrappers for the framework Photos on Mac OS X",
    long_description=__doc__,
    packages = [ "Photos" ],
    setup_requires = [
        'pyobjc-core>=3.2.1',
    ],
    install_requires = [
        'pyobjc-core>=3.2.1',
        'pyobjc-framework-Cocoa>=3.2.1',
    ],
    min_os_level="10.11",
    ext_modules = [
        Extension("Photos._Photos",
            [ "Modules/_Photos.m" ],
            extra_link_args=["-framework", "Photos"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_Photos')
            ]
        ),
    ],

)
