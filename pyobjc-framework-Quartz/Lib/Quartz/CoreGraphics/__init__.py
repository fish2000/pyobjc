'''
Python mapping for the CoreGraphics framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import sys
import objc
import CoreFoundation

from Quartz.CoreGraphics import _metadata
from Quartz.CoreGraphics._inlines import _inline_list_


sys.modules['Quartz.CoreGraphics'] = mod = objc.ObjCLazyModule('Quartz.CoreGraphics',
    "com.apple.CoreGraphics",
    objc.pathForFramework("/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreGraphics.framework"),
    _metadata.__dict__, _inline_list_, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( CoreFoundation,))


def _load(mod):
    import Quartz
    Quartz.CoreGraphics = mod

    import Quartz.CoreGraphics._callbacks as m
    for nm in dir(m):
        if nm.startswith('_'): continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._doubleindirect as m
    for nm in dir(m):
        if nm.startswith('_'): continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._sortandmap as m
    for nm in dir(m):
        if nm.startswith('_'): continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._coregraphics as m
    for nm in dir(m):
        if nm.startswith('_'): continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._contextmanager as m
    for nm in dir(m):
        if nm.startswith('_'): continue
        setattr(mod, nm, getattr(m, nm))

    mod.setCGPathElement(mod.CGPathElement)
    del mod.setCGPathElement

    # a #define
    mod.kCGEventFilterMaskPermitAllEvents = (
                    mod.kCGEventFilterMaskPermitLocalMouseEvents | 
                    mod.kCGEventFilterMaskPermitLocalKeyboardEvents | 
                    mod.kCGEventFilterMaskPermitSystemDefinedEvents)

    def CGEventMaskBit(eventType):
        return (1 << eventType)
    mod.CGEventMaskBit = CGEventMaskBit


    # Some pseudo-constants
    mod.kCGBaseWindowLevel = mod.CGWindowLevelForKey(mod.kCGBaseWindowLevelKey)
    mod.kCGMinimumWindowLevel = mod.CGWindowLevelForKey(mod.kCGMinimumWindowLevelKey)
    mod.kCGDesktopWindowLevel = mod.CGWindowLevelForKey(mod.kCGDesktopWindowLevelKey)
    mod.kCGDesktopIconWindowLevel = mod.CGWindowLevelForKey(mod.kCGDesktopIconWindowLevelKey)
    mod.kCGBackstopMenuLevel = mod.CGWindowLevelForKey(mod.kCGBackstopMenuLevelKey)
    mod.kCGNormalWindowLevel = mod.CGWindowLevelForKey(mod.kCGNormalWindowLevelKey)
    mod.kCGFloatingWindowLevel = mod.CGWindowLevelForKey(mod.kCGFloatingWindowLevelKey)
    mod.kCGTornOffMenuWindowLevel = mod.CGWindowLevelForKey(mod.kCGTornOffMenuWindowLevelKey)
    mod.kCGDockWindowLevel = mod.CGWindowLevelForKey(mod.kCGDockWindowLevelKey)
    mod.kCGMainMenuWindowLevel = mod.CGWindowLevelForKey(mod.kCGMainMenuWindowLevelKey)
    mod.kCGStatusWindowLevel = mod.CGWindowLevelForKey(mod.kCGStatusWindowLevelKey)
    mod.kCGModalPanelWindowLevel = mod.CGWindowLevelForKey(mod.kCGModalPanelWindowLevelKey)
    mod.kCGPopUpMenuWindowLevel = mod.CGWindowLevelForKey(mod.kCGPopUpMenuWindowLevelKey)
    mod.kCGDraggingWindowLevel = mod.CGWindowLevelForKey(mod.kCGDraggingWindowLevelKey)
    mod.kCGScreenSaverWindowLevel = mod.CGWindowLevelForKey(mod.kCGScreenSaverWindowLevelKey)
    mod.kCGCursorWindowLevel = mod.CGWindowLevelForKey(mod.kCGCursorWindowLevelKey)
    mod.kCGOverlayWindowLevel = mod.CGWindowLevelForKey(mod.kCGOverlayWindowLevelKey)
    mod.kCGHelpWindowLevel = mod.CGWindowLevelForKey(mod.kCGHelpWindowLevelKey)
    mod.kCGUtilityWindowLevel = mod.CGWindowLevelForKey(mod.kCGUtilityWindowLevelKey)
    mod.kCGAssistiveTechHighWindowLevel = mod.CGWindowLevelForKey(mod.kCGAssistiveTechHighWindowLevelKey)
    mod.kCGMaximumWindowLevel = mod.CGWindowLevelForKey(mod.kCGMaximumWindowLevelKey)

    mod.CGSetLocalEventsFilterDuringSupressionState = mod.CGSetLocalEventsFilterDuringSuppressionState

_load(mod)
