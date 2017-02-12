from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPNowPlayingInfoCenter (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(MediaPlayer.MPNowPlayingInfoMediaTypeNone, 0)
            self.assertEqual(MediaPlayer.MPNowPlayingInfoMediaTypeAudio, 1)
            self.assertEqual(MediaPlayer.MPNowPlayingInfoMediaTypeVideo, 2)
            self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStateUnknown, 0)
            self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStatePlaying, 1)
            self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStatePaused, 2)
            self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStateStopped, 3)
            self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStateInterrupted, 4)

            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyElapsedPlaybackTime, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyPlaybackRate, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyDefaultPlaybackRate, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyPlaybackQueueIndex, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyPlaybackQueueCount, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyChapterNumber, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyChapterCount, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyIsLiveStream, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyAvailableLanguageOptions, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyCurrentLanguageOptions, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoCollectionIdentifier, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyExternalContentIdentifier, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyExternalUserProfileIdentifier, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyPlaybackProgress, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyMediaType, unicode)
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyAssetURL, unicode)

if __name__ == "__main__":
    main()
