'''
Wrappers for the "Collaboration" framework in MacOSX 10.5 or later. The
Collaboration framework provides access to identities, and manages
user interface elements for selecting identities.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="3.3a0"

setup(
    name='pyobjc-framework-Collaboration',
    description = "Wrappers for the framework Collaboration on Mac OS X",
    min_os_level='10.5',
    packages = [ "Collaboration" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-'+VERSION,
    ],
    long_description=__doc__,
)
