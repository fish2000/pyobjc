'''
Python mapping for the ImageKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import sys
import objc
import Cocoa
import Quartz.QuartzCore

from Quartz.ImageKit import _metadata

sys.modules['Quartz.ImageKit'] = mod = objc.ObjCLazyModule('Quartz.ImageKit',
    "com.apple.imageKit",
    objc.pathForFramework("/System/Library/Frameworks/Quartz.framework/Frameworks/ImageKit.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( Cocoa, Quartz.QuartzCore,))
