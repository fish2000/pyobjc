from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPRemoteControlTypes (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(MediaPlayer.MPShuffleTypeOff, 0)
            self.assertEqual(MediaPlayer.MPShuffleTypeItems, 1)
            self.assertEqual(MediaPlayer.MPShuffleTypeCollections, 2)
            self.assertEqual(MediaPlayer.MPRepeatTypeOff, 0)
            self.assertEqual(MediaPlayer.MPRepeatTypeOne, 1)
            self.assertEqual(MediaPlayer.MPRepeatTypeAll, 2)
            self.assertEqual(MediaPlayer.MPChangeLanguageOptionSettingNone, 0)
            self.assertEqual(MediaPlayer.MPChangeLanguageOptionSettingNowPlayingItemOnly, 1)
            self.assertEqual(MediaPlayer.MPChangeLanguageOptionSettingPermanent, 2)

if __name__ == "__main__":
    main()
