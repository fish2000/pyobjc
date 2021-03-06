'''
Wrappers for the "IMServicePlugIn" framework on MacOS X. The Address Book is
a centralized database for contact and other information for people. Appliations
that make use of the IMServicePlugIn framework all use the same database.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.3a0"

setup(
    name='pyobjc-framework-IMServicePlugIn',
    description = "Wrappers for the framework IMServicePlugIn on Mac OS X",
    min_os_level='10.7',
    packages = [ "IMServicePlugIn" ],
    ext_modules = [
        Extension("IMServicePlugIn._IMServicePlugIn",
            [ "Modules/_IMServicePlugIn.m" ],
            extra_link_args=["-framework", "GameKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_IMServicePlugIn')
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
