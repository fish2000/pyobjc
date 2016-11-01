import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSearchCallHistoryIntentResponse (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeUnspecified, 0)
            self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeReady, 1)
            self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeContinueInApp, 2)
            self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeFailure, 3)
            self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeFailureRequiringAppLaunch, 4)


if __name__ == "__main__":
    main()
