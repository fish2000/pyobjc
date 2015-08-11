from PyObjCTools.TestSupport import *
import Cocoa

class TestProtocolsExisting (TestCase):

    @min_sdk_level('10.10')
    def testProtocols10_10(self):
        objc.protocolNamed('NSAlertDelegate')
        objc.protocolNamed('NSApplicationDelegate')
        objc.protocolNamed('NSCollectionViewDelegate')
        objc.protocolNamed('NSDatePickerCellDelegate')
        objc.protocolNamed('NSDockTilePlugIn')
        objc.protocolNamed('NSDrawerDelegate')
        objc.protocolNamed('NSImageDelegate')
        objc.protocolNamed('NSPageControllerDelegate')
        objc.protocolNamed('NSPathCellDelegate')
        objc.protocolNamed('NSSoundDelegate')
        objc.protocolNamed('NSSpeechRecognizerDelegate')
        objc.protocolNamed('NSSpeechSynthesizerDelegate')
        objc.protocolNamed('NSTextFinderClient')
        objc.protocolNamed('NSTextStorageDelegate')
        objc.protocolNamed('NSTokenFieldCellDelegate')
        objc.protocolNamed('NSTokenFieldDelegate')
        objc.protocolNamed('NSUserInterfaceItemSearching')

    @min_os_level('10.6')
    def testProtocols10_6(self):
        objc.protocolNamed('NSAnimatablePropertyContainer')
        objc.protocolNamed('NSAnimationDelegate')
        objc.protocolNamed('NSBrowserDelegate')
        objc.protocolNamed('NSChangeSpelling')
        objc.protocolNamed('NSColorPickingCustom')
        objc.protocolNamed('NSColorPickingDefault')
        objc.protocolNamed('NSComboBoxCellDataSource')
        objc.protocolNamed('NSComboBoxDataSource')
        objc.protocolNamed('NSComboBoxDelegate')
        objc.protocolNamed('NSControlTextEditingDelegate')
        objc.protocolNamed('NSDraggingInfo')
        objc.protocolNamed('NSGlyphStorage')
        objc.protocolNamed('NSIgnoreMisspelledWords')
        objc.protocolNamed('NSInputServerMouseTracker')
        objc.protocolNamed('NSInputServiceProvider')
        objc.protocolNamed('NSLayoutManagerDelegate')
        objc.protocolNamed('NSMatrixDelegate')
        objc.protocolNamed('NSMenuDelegate')
        objc.protocolNamed('NSOpenSavePanelDelegate')
        objc.protocolNamed('NSOutlineViewDataSource')
        objc.protocolNamed('NSOutlineViewDelegate')
        objc.protocolNamed('NSPasteboardItemDataProvider')
        objc.protocolNamed('NSPasteboardReading')
        objc.protocolNamed('NSPasteboardWriting')
        objc.protocolNamed('NSPathControlDelegate')
        objc.protocolNamed('NSPrintPanelAccessorizing')
        objc.protocolNamed('NSRuleEditorDelegate')
        objc.protocolNamed('NSSplitViewDelegate')
        objc.protocolNamed('NSTabViewDelegate')
        objc.protocolNamed('NSTableViewDataSource')
        objc.protocolNamed('NSTableViewDelegate')
        objc.protocolNamed('NSTextAttachmentCell')
        objc.protocolNamed('NSTextDelegate')
        objc.protocolNamed('NSTextFieldDelegate')
        objc.protocolNamed('NSTextInput')
        objc.protocolNamed('NSTextInputClient')
        objc.protocolNamed('NSTextViewDelegate')
        objc.protocolNamed('NSToolbarDelegate')
        objc.protocolNamed('NSUserInterfaceValidations')
        objc.protocolNamed('NSValidatedUserInterfaceItem')
        objc.protocolNamed('NSWindowDelegate')

    @min_os_level('10.7')
    def testProtocols10_7(self):
        objc.protocolNamed('NSDraggingDestination')
        objc.protocolNamed('NSDraggingSource')
        objc.protocolNamed('NSPopoverDelegate')
        objc.protocolNamed('NSTextFinderBarContainer')
        objc.protocolNamed('NSTextLayoutOrientationProvider')
        objc.protocolNamed('NSUserInterfaceItemIdentification')
        objc.protocolNamed('NSWindowRestoration')

    @min_sdk_level('10.8')
    def testProtocols10_8(self):
        objc.protocolNamed('NSSharingServiceDelegate')
        objc.protocolNamed('NSSharingServicePickerDelegate')

if __name__ == "__main__":
    main()
