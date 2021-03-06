from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    SCNAnimationEventBlock = b'v@@Z'

    class TestSCNAnimationHelper (SceneKit.NSObject):
        def isAnimationForKeyPaused_(self, k): return 1
        def removeAnimationForKey_fadeOutDuration_(self, k, d): pass
        def setSpeed_forAnimationKey_(self, s, k): pass

    class TestSCNAnimation (TestCase):
        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed("SCNAnimatable")

        @min_os_level('10.10')
        def testProtocolMethods(self):
            self.assertResultIsBOOL(TestSCNAnimationHelper.isAnimationForKeyPaused_)
            self.assertArgHasType(TestSCNAnimationHelper.removeAnimationForKey_fadeOutDuration_, 1, objc._C_CGFloat)
            self.assertArgHasType(TestSCNAnimationHelper.setSpeed_forAnimationKey_, 0, objc._C_CGFloat)

        def testMethods(self):
            self.assertArgIsBOOL(SceneKit.CAAnimation.setUsesSceneTimeBase_, 0)
            self.assertResultIsBOOL(SceneKit.CAAnimation.usesSceneTimeBase)

        @min_os_level('10.9')
        def testMethods10_9(self):
            self.assertArgIsBlock(SceneKit.SCNAnimationEvent.animationEventWithKeyTime_block_, 1, SCNAnimationEventBlock)


if __name__ == "__main__":
    main()
