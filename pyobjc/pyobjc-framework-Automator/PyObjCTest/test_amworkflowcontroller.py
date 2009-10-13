
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflowController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(AMWorkflowController.canRun)
        self.failUnlessResultIsBOOL(AMWorkflowController.isRunning)

if __name__ == "__main__":
    main()
