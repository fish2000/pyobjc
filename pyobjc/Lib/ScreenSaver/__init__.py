"""
Python mapping for the ScreenSaver framework on MacOS X

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


# Load the ScreenSaver framework, and gather all classes defined there
import objc as _objc

import AppKit as _AppKit

# Custom method signature (undocumented class, this is a guess)
_objc.setSignatureForSelector("ScreenSaverUserInfo", "loginUserName:andID:", "v@:o^@o^I")

_objc.loadBundle(
    "ScreenSaver",
    globals(),
    bundle_path="/System/Library/Frameworks/ScreenSaver.framework"
)

# NOTE: One MacOSX 10.2.4 the framework doesn't define constants,
# therefore there is no _ScreenSaver module.

# Define useful utility methods here
