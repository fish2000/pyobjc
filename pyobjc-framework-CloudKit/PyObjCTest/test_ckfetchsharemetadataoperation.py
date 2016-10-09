import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchShareMetadataOperation (TestCase):
        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertArgIsBlock(CloudKit.CKFetchShareMetadataOperation.setPerShareMetadataBlock_, 0, b"v@@@")
            self.assertResultIsBlock(CloudKit.CKFetchShareMetadataOperation.perShareMetadataBlock, b"v@@@")

            self.assertArgIsBlock(CloudKit.CKFetchShareMetadataOperation.setFetchShareMetadataCompletionBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKFetchShareMetadataOperation.fetchShareMetadataCompletionBlock, b"v@")

            self.assertResultIsBOOL(CloudKit.CKFetchShareMetadataOperation.shouldFetchRootRecord)
            self.assertArgIsBOOL(CloudKit.CKFetchShareMetadataOperation.setShouldFetchRootRecord_, 0)

if __name__ == "__main__":
    main()
