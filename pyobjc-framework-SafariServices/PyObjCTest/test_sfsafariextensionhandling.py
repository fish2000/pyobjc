import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariExtensionHandlingHelper (SafariServices.NSObject):
        def validateToolbarItemInWindow_validationHandler_(self, w, h): pass
        def validateContextMenuItemWithCommand_inPage_userInfo_validationHandler_(self, a, b, c, d): pass

    class TestSFSafariExtensionHandling (TestCase):
        @min_os_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('SFSafariExtensionHandling')

        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(TestSFSafariExtensionHandlingHelper.validateToolbarItemInWindow_validationHandler_, 1, b'vZ@')

            self.assertArgIsBlock(TestSFSafariExtensionHandlingHelper.validateContextMenuItemWithCommand_inPage_userInfo_validationHandler_, 3, b'vZ@')




if __name__ == "__main__":
    main()

