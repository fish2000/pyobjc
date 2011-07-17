# Place holder for real tests.
from PyObjCTools.TestSupport import *
import objc

from Foundation import NSLocalizedString, NSAutoreleasePool

class TestNSLocalizedString(TestCase):
    def testBasic(self):
        # This is mostly a regression tests, the function used to crash on
        # this...
        if objc.platform != 'MACOSX':
            return

        pool = NSAutoreleasePool.alloc().init()
        s = NSLocalizedString(u"hello world", u"")
        del pool
        self.assertEqual (s, u"hello world")
        # XXX : Since we get the same object back, it's still unicode
        #self.assertEqual (s.nsstring().description(), u"hello world")

if __name__ == '__main__':
    main( )
