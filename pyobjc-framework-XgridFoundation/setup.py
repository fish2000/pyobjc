'''
Wrappers for the "XgridFoundation" framework on MacOSX. This framework
supports the development of applications that monitor or control jobs
processed by Xgrid clusters.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="3.3a0"

setup(
    name='pyobjc-framework-XgridFoundation',
    description = "Wrappers for the framework XgridFoundation on Mac OS X",
    max_os_level='10.7',
    packages = [ "XgridFoundation" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
