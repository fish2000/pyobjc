
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestIconsCore (TestCase):
    def testConstants(self):
        self.assertEqual(kGenericDocumentIconResource, -4000)
        self.assertEqual(kGenericStationeryIconResource, -3985)
        self.assertEqual(kGenericEditionFileIconResource, -3989)
        self.assertEqual(kGenericApplicationIconResource, -3996)
        self.assertEqual(kGenericDeskAccessoryIconResource, -3991)
        self.assertEqual(kGenericFolderIconResource, -3999)
        self.assertEqual(kPrivateFolderIconResource, -3994)
        self.assertEqual(kFloppyIconResource, -3998)
        self.assertEqual(kTrashIconResource, -3993)
        self.assertEqual(kGenericRAMDiskIconResource, -3988)
        self.assertEqual(kGenericCDROMIconResource, -3987)
        self.assertEqual(kDesktopIconResource, -3992)
        self.assertEqual(kOpenFolderIconResource, -3997)
        self.assertEqual(kGenericHardDiskIconResource, -3995)
        self.assertEqual(kGenericFileServerIconResource, -3972)
        self.assertEqual(kGenericSuitcaseIconResource, -3970)
        self.assertEqual(kGenericMoverObjectIconResource, -3969)

        self.assertEqual(kGenericPreferencesIconResource, -3971)
        self.assertEqual(kGenericQueryDocumentIconResource, -16506)
        self.assertEqual(kGenericExtensionIconResource, -16415)
        self.assertEqual(kSystemFolderIconResource, -3983)
        self.assertEqual(kHelpIconResource, -20271)
        self.assertEqual(kAppleMenuFolderIconResource, -3982)
        self.assertEqual(genericDocumentIconResource, kGenericDocumentIconResource)
        self.assertEqual(genericStationeryIconResource, kGenericStationeryIconResource)
        self.assertEqual(genericEditionFileIconResource, kGenericEditionFileIconResource)
        self.assertEqual(genericApplicationIconResource, kGenericApplicationIconResource)
        self.assertEqual(genericDeskAccessoryIconResource, kGenericDeskAccessoryIconResource)
        self.assertEqual(genericFolderIconResource, kGenericFolderIconResource)
        self.assertEqual(privateFolderIconResource, kPrivateFolderIconResource)
        self.assertEqual(floppyIconResource, kFloppyIconResource)
        self.assertEqual(trashIconResource, kTrashIconResource)
        self.assertEqual(genericRAMDiskIconResource, kGenericRAMDiskIconResource)
        self.assertEqual(genericCDROMIconResource, kGenericCDROMIconResource)
        self.assertEqual(desktopIconResource, kDesktopIconResource)
        self.assertEqual(openFolderIconResource, kOpenFolderIconResource)
        self.assertEqual(genericHardDiskIconResource, kGenericHardDiskIconResource)
        self.assertEqual(genericFileServerIconResource, kGenericFileServerIconResource)
        self.assertEqual(genericSuitcaseIconResource, kGenericSuitcaseIconResource)
        self.assertEqual(genericMoverObjectIconResource, kGenericMoverObjectIconResource)
        self.assertEqual(genericPreferencesIconResource, kGenericPreferencesIconResource)
        self.assertEqual(genericQueryDocumentIconResource, kGenericQueryDocumentIconResource)
        self.assertEqual(genericExtensionIconResource, kGenericExtensionIconResource)
        self.assertEqual(systemFolderIconResource, kSystemFolderIconResource)
        self.assertEqual(appleMenuFolderIconResource, kAppleMenuFolderIconResource)
        self.assertEqual(kStartupFolderIconResource, -3981)
        self.assertEqual(kOwnedFolderIconResource, -3980)
        self.assertEqual(kDropFolderIconResource, -3979)
        self.assertEqual(kSharedFolderIconResource, -3978)
        self.assertEqual(kMountedFolderIconResource, -3977)
        self.assertEqual(kControlPanelFolderIconResource, -3976)
        self.assertEqual(kPrintMonitorFolderIconResource, -3975)
        self.assertEqual(kPreferencesFolderIconResource, -3974)
        self.assertEqual(kExtensionsFolderIconResource, -3973)
        self.assertEqual(kFontsFolderIconResource, -3968)
        self.assertEqual(kFullTrashIconResource, -3984)
        self.assertEqual(startupFolderIconResource, kStartupFolderIconResource)
        self.assertEqual(ownedFolderIconResource, kOwnedFolderIconResource)
        self.assertEqual(dropFolderIconResource, kDropFolderIconResource)
        self.assertEqual(sharedFolderIconResource, kSharedFolderIconResource)
        self.assertEqual(mountedFolderIconResource, kMountedFolderIconResource)
        self.assertEqual(controlPanelFolderIconResource, kControlPanelFolderIconResource)
        self.assertEqual(printMonitorFolderIconResource, kPrintMonitorFolderIconResource)
        self.assertEqual(preferencesFolderIconResource, kPreferencesFolderIconResource)
        self.assertEqual(extensionsFolderIconResource, kExtensionsFolderIconResource)
        self.assertEqual(fontsFolderIconResource, kFontsFolderIconResource)
        self.assertEqual(fullTrashIconResource, kFullTrashIconResource)
        self.assertEqual(kSystemIconsCreator, fourcc(b'macs'))

        self.assertEqual(kClipboardIcon, fourcc(b'CLIP'))
        self.assertEqual(kClippingUnknownTypeIcon, fourcc(b'clpu'))
        self.assertEqual(kClippingPictureTypeIcon, fourcc(b'clpp'))
        self.assertEqual(kClippingTextTypeIcon, fourcc(b'clpt'))
        self.assertEqual(kClippingSoundTypeIcon, fourcc(b'clps'))
        self.assertEqual(kDesktopIcon, fourcc(b'desk'))
        self.assertEqual(kFinderIcon, fourcc(b'FNDR'))
        self.assertEqual(kComputerIcon, fourcc(b'root'))
        self.assertEqual(kFontSuitcaseIcon, fourcc(b'FFIL'))
        self.assertEqual(kFullTrashIcon, fourcc(b'ftrh'))
        self.assertEqual(kGenericApplicationIcon, fourcc(b'APPL'))
        self.assertEqual(kGenericCDROMIcon, fourcc(b'cddr'))
        self.assertEqual(kGenericControlPanelIcon, fourcc(b'APPC'))
        self.assertEqual(kGenericControlStripModuleIcon, fourcc(b'sdev'))
        self.assertEqual(kGenericComponentIcon, fourcc(b'thng'))
        self.assertEqual(kGenericDeskAccessoryIcon, fourcc(b'APPD'))
        self.assertEqual(kGenericDocumentIcon, fourcc(b'docu'))
        self.assertEqual(kGenericEditionFileIcon, fourcc(b'edtf'))
        self.assertEqual(kGenericExtensionIcon, fourcc(b'INIT'))
        self.assertEqual(kGenericFileServerIcon, fourcc(b'srvr'))
        self.assertEqual(kGenericFontIcon, fourcc(b'ffil'))
        self.assertEqual(kGenericFontScalerIcon, fourcc(b'sclr'))
        self.assertEqual(kGenericFloppyIcon, fourcc(b'flpy'))
        self.assertEqual(kGenericHardDiskIcon, fourcc(b'hdsk'))
        self.assertEqual(kGenericIDiskIcon, fourcc(b'idsk'))
        self.assertEqual(kGenericRemovableMediaIcon, fourcc(b'rmov'))
        self.assertEqual(kGenericMoverObjectIcon, fourcc(b'movr'))
        self.assertEqual(kGenericPCCardIcon, fourcc(b'pcmc'))
        self.assertEqual(kGenericPreferencesIcon, fourcc(b'pref'))
        self.assertEqual(kGenericQueryDocumentIcon, fourcc(b'qery'))
        self.assertEqual(kGenericRAMDiskIcon, fourcc(b'ramd'))
        self.assertEqual(kGenericSharedLibaryIcon, fourcc(b'shlb'))
        self.assertEqual(kGenericStationeryIcon, fourcc(b'sdoc'))
        self.assertEqual(kGenericSuitcaseIcon, fourcc(b'suit'))
        self.assertEqual(kGenericURLIcon, fourcc(b'gurl'))
        self.assertEqual(kGenericWORMIcon, fourcc(b'worm'))
        self.assertEqual(kInternationalResourcesIcon, fourcc(b'ifil'))
        self.assertEqual(kKeyboardLayoutIcon, fourcc(b'kfil'))
        self.assertEqual(kSoundFileIcon, fourcc(b'sfil'))
        self.assertEqual(kSystemSuitcaseIcon, fourcc(b'zsys'))
        self.assertEqual(kTrashIcon, fourcc(b'trsh'))
        self.assertEqual(kTrueTypeFontIcon, fourcc(b'tfil'))
        self.assertEqual(kTrueTypeFlatFontIcon, fourcc(b'sfnt'))
        self.assertEqual(kTrueTypeMultiFlatFontIcon, fourcc(b'ttcf'))
        self.assertEqual(kUserIDiskIcon, fourcc(b'udsk'))
        self.assertEqual(kUnknownFSObjectIcon, fourcc(b'unfs'))
        self.assertEqual(kInternationResourcesIcon, kInternationalResourcesIcon)
        self.assertEqual(kInternetLocationHTTPIcon, fourcc(b'ilht'))
        self.assertEqual(kInternetLocationFTPIcon, fourcc(b'ilft'))
        self.assertEqual(kInternetLocationAppleShareIcon, fourcc(b'ilaf'))
        self.assertEqual(kInternetLocationAppleTalkZoneIcon, fourcc(b'ilat'))
        self.assertEqual(kInternetLocationFileIcon, fourcc(b'ilfi'))
        self.assertEqual(kInternetLocationMailIcon, fourcc(b'ilma'))
        self.assertEqual(kInternetLocationNewsIcon, fourcc(b'ilnw'))
        self.assertEqual(kInternetLocationNSLNeighborhoodIcon, fourcc(b'ilns'))
        self.assertEqual(kInternetLocationGenericIcon, fourcc(b'ilge'))
        self.assertEqual(kGenericFolderIcon, fourcc(b'fldr'))
        self.assertEqual(kDropFolderIcon, fourcc(b'dbox'))
        self.assertEqual(kMountedFolderIcon, fourcc(b'mntd'))
        self.assertEqual(kOpenFolderIcon, fourcc(b'ofld'))
        self.assertEqual(kOwnedFolderIcon, fourcc(b'ownd'))
        self.assertEqual(kPrivateFolderIcon, fourcc(b'prvf'))
        self.assertEqual(kSharedFolderIcon, fourcc(b'shfl'))
        self.assertEqual(kSharingPrivsNotApplicableIcon, fourcc(b'shna'))
        self.assertEqual(kSharingPrivsReadOnlyIcon, fourcc(b'shro'))
        self.assertEqual(kSharingPrivsReadWriteIcon, fourcc(b'shrw'))
        self.assertEqual(kSharingPrivsUnknownIcon, fourcc(b'shuk'))
        self.assertEqual(kSharingPrivsWritableIcon, fourcc(b'writ'))
        self.assertEqual(kUserFolderIcon, fourcc(b'ufld'))
        self.assertEqual(kWorkgroupFolderIcon, fourcc(b'wfld'))
        self.assertEqual(kGuestUserIcon, fourcc(b'gusr'))
        self.assertEqual(kUserIcon, fourcc(b'user'))
        self.assertEqual(kOwnerIcon, fourcc(b'susr'))
        self.assertEqual(kGroupIcon, fourcc(b'grup'))
        self.assertEqual(kAppearanceFolderIcon, fourcc(b'appr'))
        self.assertEqual(kAppleExtrasFolderIcon, cast_int(0x616578C4))
        self.assertEqual(kAppleMenuFolderIcon, fourcc(b'amnu'))
        self.assertEqual(kApplicationsFolderIcon, fourcc(b'apps'))
        self.assertEqual(kApplicationSupportFolderIcon, fourcc(b'asup'))
        self.assertEqual(kAssistantsFolderIcon, cast_int(0x617374C4))
        self.assertEqual(kColorSyncFolderIcon, fourcc(b'prof'))
        self.assertEqual(kContextualMenuItemsFolderIcon, fourcc(b'cmnu'))
        self.assertEqual(kControlPanelDisabledFolderIcon, fourcc(b'ctrD'))
        self.assertEqual(kControlPanelFolderIcon, fourcc(b'ctrl'))
        self.assertEqual(kControlStripModulesFolderIcon, cast_int(0x736476C4))
        self.assertEqual(kDocumentsFolderIcon, fourcc(b'docs'))
        self.assertEqual(kExtensionsDisabledFolderIcon, fourcc(b'extD'))
        self.assertEqual(kExtensionsFolderIcon, fourcc(b'extn'))
        self.assertEqual(kFavoritesFolderIcon, fourcc(b'favs'))
        self.assertEqual(kFontsFolderIcon, fourcc(b'font'))
        self.assertEqual(kHelpFolderIcon, cast_int(0xC4686C70))
        self.assertEqual(kInternetFolderIcon, cast_int(0x696E74C4))
        self.assertEqual(kInternetPlugInFolderIcon, cast_int(0xC46E6574))
        self.assertEqual(kInternetSearchSitesFolderIcon, fourcc(b'issf'))
        self.assertEqual(kLocalesFolderIcon, cast_int(0xC46C6F63))
        self.assertEqual(kMacOSReadMeFolderIcon, cast_int(0x6D6F72C4))
        self.assertEqual(kPublicFolderIcon, fourcc(b'pubf'))
        self.assertEqual(kPreferencesFolderIcon, cast_int(0x707266C4))
        self.assertEqual(kPrinterDescriptionFolderIcon, fourcc(b'ppdf'))
        self.assertEqual(kPrinterDriverFolderIcon, cast_int(0xC4707264))
        self.assertEqual(kPrintMonitorFolderIcon, fourcc(b'prnt'))
        self.assertEqual(kRecentApplicationsFolderIcon, fourcc(b'rapp'))
        self.assertEqual(kRecentDocumentsFolderIcon, fourcc(b'rdoc'))
        self.assertEqual(kRecentServersFolderIcon, fourcc(b'rsrv'))
        self.assertEqual(kScriptingAdditionsFolderIcon, cast_int(0xC4736372))
        self.assertEqual(kSharedLibrariesFolderIcon, cast_int(0xC46C6962))
        self.assertEqual(kScriptsFolderIcon, cast_int( 0x736372C4))
        self.assertEqual(kShutdownItemsDisabledFolderIcon, fourcc(b'shdD'))
        self.assertEqual(kShutdownItemsFolderIcon, fourcc(b'shdf'))
        self.assertEqual(kSpeakableItemsFolder, fourcc(b'spki'))
        self.assertEqual(kStartupItemsDisabledFolderIcon, fourcc(b'strD'))
        self.assertEqual(kStartupItemsFolderIcon, fourcc(b'strt'))
        self.assertEqual(kSystemExtensionDisabledFolderIcon, fourcc(b'macD'))
        self.assertEqual(kSystemFolderIcon, fourcc(b'macs'))
        self.assertEqual(kTextEncodingsFolderIcon, cast_int(0xC4746578))
        self.assertEqual(kUsersFolderIcon, cast_int(0x757372C4))
        self.assertEqual(kUtilitiesFolderIcon, cast_int(0x757469C4))
        self.assertEqual(kVoicesFolderIcon, fourcc(b'fvoc'))
        self.assertEqual(kAppleScriptBadgeIcon, fourcc(b'scrp'))
        self.assertEqual(kLockedBadgeIcon, fourcc(b'lbdg'))
        self.assertEqual(kMountedBadgeIcon, fourcc(b'mbdg'))
        self.assertEqual(kSharedBadgeIcon, fourcc(b'sbdg'))
        self.assertEqual(kAliasBadgeIcon, fourcc(b'abdg'))
        self.assertEqual(kAlertCautionBadgeIcon, fourcc(b'cbdg'))
        self.assertEqual(kAlertNoteIcon, fourcc(b'note'))
        self.assertEqual(kAlertCautionIcon, fourcc(b'caut'))
        self.assertEqual(kAlertStopIcon, fourcc(b'stop'))
        self.assertEqual(kAppleTalkIcon, fourcc(b'atlk'))
        self.assertEqual(kAppleTalkZoneIcon, fourcc(b'atzn'))
        self.assertEqual(kAFPServerIcon, fourcc(b'afps'))
        self.assertEqual(kFTPServerIcon, fourcc(b'ftps'))
        self.assertEqual(kHTTPServerIcon, fourcc(b'htps'))
        self.assertEqual(kGenericNetworkIcon, fourcc(b'gnet'))
        self.assertEqual(kIPFileServerIcon, fourcc(b'isrv'))
        self.assertEqual(kToolbarCustomizeIcon, fourcc(b'tcus'))
        self.assertEqual(kToolbarDeleteIcon, fourcc(b'tdel'))
        self.assertEqual(kToolbarFavoritesIcon, fourcc(b'tfav'))
        self.assertEqual(kToolbarHomeIcon, fourcc(b'thom'))
        self.assertEqual(kAppleLogoIcon, fourcc(b'capl'))
        self.assertEqual(kAppleMenuIcon, fourcc(b'sapl'))
        self.assertEqual(kBackwardArrowIcon, fourcc(b'baro'))
        self.assertEqual(kFavoriteItemsIcon, fourcc(b'favr'))
        self.assertEqual(kForwardArrowIcon, fourcc(b'faro'))
        self.assertEqual(kGridIcon, fourcc(b'grid'))
        self.assertEqual(kHelpIcon, fourcc(b'help'))
        self.assertEqual(kKeepArrangedIcon, fourcc(b'arng'))
        self.assertEqual(kLockedIcon, fourcc(b'lock'))
        self.assertEqual(kNoFilesIcon, fourcc(b'nfil'))
        self.assertEqual(kNoFolderIcon, fourcc(b'nfld'))
        self.assertEqual(kNoWriteIcon, fourcc(b'nwrt'))
        self.assertEqual(kProtectedApplicationFolderIcon, fourcc(b'papp'))
        self.assertEqual(kProtectedSystemFolderIcon, fourcc(b'psys'))
        self.assertEqual(kRecentItemsIcon, fourcc(b'rcnt'))
        self.assertEqual(kShortcutIcon, fourcc(b'shrt'))
        self.assertEqual(kSortAscendingIcon, fourcc(b'asnd'))
        self.assertEqual(kSortDescendingIcon, fourcc(b'dsnd'))
        self.assertEqual(kUnlockedIcon, fourcc(b'ulck'))
        self.assertEqual(kConnectToIcon, fourcc(b'cnct'))
        self.assertEqual(kGenericWindowIcon, fourcc(b'gwin'))
        self.assertEqual(kQuestionMarkIcon, fourcc(b'ques'))
        self.assertEqual(kDeleteAliasIcon, fourcc(b'dali'))
        self.assertEqual(kEjectMediaIcon, fourcc(b'ejec'))
        self.assertEqual(kBurningIcon, fourcc(b'burn'))
        self.assertEqual(kRightContainerArrowIcon, fourcc(b'rcar'))
        self.assertEqual(kIconServicesNormalUsageFlag, 0)
        self.assertEqual(kIconServicesNoBadgeFlag, 1)
        self.assertEqual(kIconServicesUpdateIfNeededFlag, 2)
        self.assertEqual(kIconServicesCatalogInfoMask, 531550)

    @onlyOn32Bit
    def testFunctions32(self):
        # Not tested, deprecated function
        GetIconRefFromFile
        self.assertArgIsOut(GetIconRefFromFolder, 5)

        RegisterIconRefFromResource
        OverrideIconRefFromResource
        FlushIconRefs
        FlushIconRefsByVolume

        self.assertArgIsOut(RegisterIconRefFromIconFile, 3)

        ReadIconFile
        WriteIconFile

    def testFunctions(self):
        self.assertArgIsOut(GetIconRef, 3)
        err, icon = GetIconRef(0, kSystemIconsCreator, kShortcutIcon, None)
        self.assertIsInstance(err, (int, long))
        self.assertIsInstance(icon, IconRef)

        try:
            self.assertArgIsOut(GetIconRefOwners, 1)
            err, cnt = GetIconRefOwners(icon, None)
            self.assertIsInstance(err, (int, long))
            self.assertIsInstance(cnt, (int, long))

            err = AcquireIconRef(icon)
            self.assertEqual(err, 0)

            err = ReleaseIconRef(icon)
            self.assertEqual(err, 0)

            self.assertArgIsOut(GetIconRefFromFolder, 5)

            self.assertArgHasType(GetIconRefFromFileInfo, 2, objc._C_IN + objc._C_PTR + objc._C_UNICHAR)
            self.assertArgIsOut(GetIconRefFromFileInfo, 6)
            self.assertArgIsOut(GetIconRefFromFileInfo, 7)

            self.assertArgIsOut(GetIconRefFromTypeInfo, 5)

            self.assertArgIsIn(GetIconRefFromIconFamilyPtr, 0)
            self.assertArgIsOut(GetIconRefFromIconFamilyPtr, 2)

            self.assertArgIsOut(GetIconRefFromComponent, 1)

            # XXX: Untested for now...
            RegisterIconRefFromIconFamily
            RegisterIconRefFromFSRef
            UnregisterIconRef
            UpdateIconRef
            OverrideIconRef
            RemoveIconRefOverride

            self.assertArgIsOut(CompositeIconRef, 2)

            self.assertArgIsOut(IsIconRefComposite, 1)
            self.assertArgIsOut(IsIconRefComposite, 2)

            self.assertResultIsBOOL(IsValidIconRef)
            self.assertResultIsBOOL(IsDataAvailableInIconRef)

            self.assertArgIsBOOL(SetCustomIconsEnabled, 1)
            self.assertArgIsOut(GetCustomIconsEnabled, 1)
            self.assertArgHasType(GetCustomIconsEnabled, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)


            # Untested...
            ReadIconFromFSRef

        finally:
            err = ReleaseIconRef(icon)
            self.assertEqual(err, 0)

    def testOpaque(self):
        self.assertIsOpaquePointer(IconRef)


if __name__ == "__main__":
    main()
