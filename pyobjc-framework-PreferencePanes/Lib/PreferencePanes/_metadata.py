# This file is generated by objective.metadata
#
# Last update: Fri May 25 17:46:49 2012

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
constants = '''$NSPrefPaneHelpMenuAnchorKey$NSPrefPaneHelpMenuInfoPListKey$NSPrefPaneHelpMenuTitleKey$NSPreferencePaneCancelUnselectNotification$NSPreferencePaneDoUnselectNotification$'''
enums = '''$NSUnselectCancel@0$NSUnselectLater@2$NSUnselectNow@1$'''
misc.update({'kNSPrefPaneHelpMenuAnchorKey': 'anchor', 'kNSPrefPaneHelpMenuTitleKey': 'title', 'kNSPrefPaneHelpMenuInfoPListKey': 'NSPrefPaneHelpAnchors'})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSPreferencePane', b'autoSaveTextFields', {'retval': {'type': 'Z'}})
    r(b'NSPreferencePane', b'isSelected', {'retval': {'type': 'Z'}})
    r(b'NSPreferencePane', b'replyToShouldUnselect:', {'arguments': {2: {'type': 'Z'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
