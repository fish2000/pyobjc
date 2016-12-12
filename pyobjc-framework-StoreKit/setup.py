'''
Wrappers for the "StoreKit" framework on MacOS X 10.7 or later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.3a0"

setup(
    name='pyobjc-framework-StoreKit',
    description = "Wrappers for the framework StoreKit on Mac OS X",
    min_os_level='10.7',
    packages = [ "StoreKit" ],
    ext_modules = [
        Extension("StoreKit._StoreKit",
            [ "Modules/_StoreKit.m" ],
            extra_link_args=["-framework", "StoreKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_StoreKit')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
