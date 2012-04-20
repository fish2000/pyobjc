# This file is generated by objective.metadata
#
# Last update: Thu Mar  8 12:28:35 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$$'''
enums = '''$QLPreviewViewStyleCompact@1$QLPreviewViewStyleNormal@0$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'acceptsPreviewPanelControl:', {'retval': {'type': b'Z'}})
    r('QLPreviewPanel', b'enterFullScreenMode:withOptions:', {'retval': {'type': b'Z'}})
    r('QLPreviewPanel', b'isInFullScreenMode', {'retval': {'type': b'Z'}})
    r('QLPreviewPanel', b'sharedPreviewPanelExists', {'retval': {'type': b'Z'}})
    r('QLPreviewView', b'autostarts', {'retval': {'type': b'Z'}})
    r('QLPreviewView', b'setAutostarts:', {'arguments': {2: {'type': b'Z'}}})
    r('QLPreviewView', b'setShouldCloseWithWindow:', {'arguments': {2: {'type': b'Z'}}})
    r('QLPreviewView', b'shouldCloseWithWindow', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'numberOfPreviewItemsInPreviewPanel:', {'required': True, 'retval': {'type': sel32or64(b'i', b'l')}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'previewItemDisplayState', {'retval': {'type': b'@'}})
    r('NSObject', b'previewItemTitle', {'retval': {'type': b'@'}})
    r('NSObject', b'previewItemURL', {'retval': {'type': b'@'}})
    r('NSObject', b'previewPanel:handleEvent:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'previewPanel:previewItemAtIndex:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'i', b'l')}}})
    r('NSObject', b'previewPanel:sourceFrameOnScreenForPreviewItem:', {'required': False, 'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'previewPanel:transitionImageForPreviewItem:contentRect:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': sel32or64(b'^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'^{CGRect={CGPoint=dd}{CGSize=dd}}')}}})
    r('NSObject', b'setPreviewItemDisplayState:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'setPreviewItemTitle:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'setPreviewItemURL:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'acceptsPreviewPanelControl:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'beginPreviewPanelControl:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'endPreviewPanelControl:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
protocols={'QLPreviewPanelController': objc.informal_protocol('QLPreviewPanelController', [objc.selector(None, 'beginPreviewPanelControl:', b'v@:@', isRequired=False), objc.selector(None, 'acceptsPreviewPanelControl:', b'Z@:@', isRequired=False), objc.selector(None, 'endPreviewPanelControl:', b'v@:@', isRequired=False)])}
expressions = {}

# END OF FILE
