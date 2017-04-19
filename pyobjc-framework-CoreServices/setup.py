'''
Wrappers for the "CoreServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="3.3a0"

setup(
    name='pyobjc-framework-CoreServices',
    description = "Wrappers for the framework CoreServices on Mac OS X",
    packages = [ "CoreServices" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-DictionaryServices>='+VERSION,
        'pyobjc-framework-FSEvents>='+VERSION,
        'pyobjc-framework-LaunchServices>='+VERSION,
        'pyobjc-framework-SearchKit>='+VERSION,
    ],
    long_description=__doc__,
)
