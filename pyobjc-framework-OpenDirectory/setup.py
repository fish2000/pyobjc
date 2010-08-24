''' 
Wrappers for the 'OpenDirectory' and 'CFOpenDirectory' frameworks on 
MacOSX 10.6 and later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.6',
    name='pyobjc-framework-OpenDirectory',
    version="2.3.2a0",
    description = "Wrappers for the framework OpenDirectory on Mac OS X",
    packages = [ "OpenDirectory", "CFOpenDirectory" ],
    install_requires = [ 
        'pyobjc-core>=2.3.2a0',
        'pyobjc-framework-Cocoa>=2.3.2a0',
    ],
)
