from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSMethodSignature (TestCase):

    def testTypes(self):
        o = NSObject.instanceMethodSignatureForSelector_('description')

        m = NSMethodSignature.signatureWithObjCTypes_.__metadata__()
        self.assertEqual(m['arguments'][2]['type'], 'n^t')

        m = o.methodReturnType.__metadata__()
        self.assertEqual(m['retval']['type'], '^t')
        m = o.getArgumentTypeAtIndex_.__metadata__()
        self.assertEqual(m['retval']['type'], '^t')

    def testUsing(self):
        o = NSMethodSignature.signatureWithObjCTypes_('^v@:@o^i')
        self.assertIsInstance(o, NSMethodSignature)
        v = o.methodReturnType()
        self.assertEqual(v, '^v')
        self.assertIsInstance(v, str)
        v = o.getArgumentTypeAtIndex_(0)
        self.assertEqual(v, '@')
        self.assertIsInstance(v, str)
        v = o.getArgumentTypeAtIndex_(3)
        self.assertEqual(v, 'o^i')
        self.assertIsInstance(v, str)
    def testMethods(self):
        self.assertResultHasType(NSMethodSignature.getArgumentTypeAtIndex_, '^' + objc._C_CHAR_AS_TEXT)
        self.assertResultIsNullTerminated(NSMethodSignature.getArgumentTypeAtIndex_)
        self.assertResultHasType(NSMethodSignature.methodReturnType, '^' + objc._C_CHAR_AS_TEXT)
        self.assertResultIsNullTerminated(NSMethodSignature.methodReturnType)
        self.assertResultIsBOOL(NSMethodSignature.isOneway)

            
if __name__ == "__main__":
    main()
