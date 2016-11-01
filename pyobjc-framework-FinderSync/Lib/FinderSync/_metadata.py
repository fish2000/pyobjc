# This file is generated by objective.metadata
#
# Last update: Wed Dec 31 16:56:15 2014

import objc, sys

if sys.maxsize > 2 ** 32:
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
enums = '''$FIMenuKindContextualMenuForContainer@1$FIMenuKindContextualMenuForItems@0$FIMenuKindContextualMenuForSidebar@2$FIMenuKindToolbarItemMenu@3$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'beginObservingDirectoryAtURL:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'endObservingDirectoryAtURL:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'menuForMenuKind:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'Q'}}})
    r(b'NSObject', b'requestBadgeIdentifierForURL:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'toolbarItemImage', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'toolbarItemName', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'toolbarItemToolTip', {'required': False, 'retval': {'type': b'@'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
