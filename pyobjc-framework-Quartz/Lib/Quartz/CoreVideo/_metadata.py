# This file is generated by objective.metadata
#
# Last update: Thu May 24 15:42:18 2012

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'CVTimeStamp': objc.createStructType('CVTimeStamp', b"sel32or64('{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', '{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}')", ['version', 'videoTimeScale', 'videoTime', 'hostTime', 'rateScalar', 'videoRefreshPeriod', 'smpteTime', 'flags', 'reserved']), 'CVPlanarPixelBufferInfo_YCbCrBiPlanar': objc.createStructType('CVPlanarPixelBufferInfo_YCbCrBiPlanar', b'{CVPlanarPixelBufferInfo_YCbCrBiPlanar={CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}}', []), 'CVPlanarPixelBufferInfo_YCbCrPlanar': objc.createStructType('CVPlanarPixelBufferInfo_YCbCrPlanar', b'{CVPlanarPixelBufferInfo_YCbCrPlanar={CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}}', ['componentInfoY', 'componentInfoCb', 'componentInfoCr']), 'CVPlanarComponentInfo': objc.createStructType('CVPlanarComponentInfo', b'{CVPlanarComponentInfo=iI}', ['offset', 'rowBytes']), 'CVTime': objc.createStructType('CVTime', b'{_CVTime=qii}', ['timeValue', 'timeScale', 'flags']), 'CVSMPTETime': objc.createStructType('CVSMPTETime', b"sel32or64('{CVSMPTETime=ssLLLssss}', '{CVSMPTETime=ssIIIssss}')", ['subframes', 'subframeDivisor', 'counter', 'type', 'flags', 'hours', 'minutes', 'seconds', 'frames']), 'CVPlanarPixelBufferInfo': objc.createStructType('CVPlanarPixelBufferInfo', b'{CVPlanarPixelBufferInfo=[1{CVPlanarComponentInfo=iI}]}', ['componentInfo'])})
constants = '''$kCVBufferMovieTimeKey@^{__CFString=}$kCVBufferNonPropagatedAttachmentsKey@^{__CFString=}$kCVBufferPropagatedAttachmentsKey@^{__CFString=}$kCVBufferTimeScaleKey@^{__CFString=}$kCVBufferTimeValueKey@^{__CFString=}$kCVImageBufferCGColorSpaceKey@^{__CFString=}$kCVImageBufferChromaLocationBottomFieldKey@^{__CFString=}$kCVImageBufferChromaLocationTopFieldKey@^{__CFString=}$kCVImageBufferChromaLocation_Bottom@^{__CFString=}$kCVImageBufferChromaLocation_BottomLeft@^{__CFString=}$kCVImageBufferChromaLocation_Center@^{__CFString=}$kCVImageBufferChromaLocation_DV420@^{__CFString=}$kCVImageBufferChromaLocation_Left@^{__CFString=}$kCVImageBufferChromaLocation_Top@^{__CFString=}$kCVImageBufferChromaLocation_TopLeft@^{__CFString=}$kCVImageBufferChromaSubsamplingKey@^{__CFString=}$kCVImageBufferChromaSubsampling_411@^{__CFString=}$kCVImageBufferChromaSubsampling_420@^{__CFString=}$kCVImageBufferChromaSubsampling_422@^{__CFString=}$kCVImageBufferCleanApertureHeightKey@^{__CFString=}$kCVImageBufferCleanApertureHorizontalOffsetKey@^{__CFString=}$kCVImageBufferCleanApertureKey@^{__CFString=}$kCVImageBufferCleanApertureVerticalOffsetKey@^{__CFString=}$kCVImageBufferCleanApertureWidthKey@^{__CFString=}$kCVImageBufferColorPrimariesKey@^{__CFString=}$kCVImageBufferColorPrimaries_EBU_3213@^{__CFString=}$kCVImageBufferColorPrimaries_ITU_R_709_2@^{__CFString=}$kCVImageBufferColorPrimaries_SMPTE_C@^{__CFString=}$kCVImageBufferDisplayDimensionsKey@^{__CFString=}$kCVImageBufferDisplayHeightKey@^{__CFString=}$kCVImageBufferDisplayWidthKey@^{__CFString=}$kCVImageBufferFieldCountKey@^{__CFString=}$kCVImageBufferFieldDetailKey@^{__CFString=}$kCVImageBufferFieldDetailSpatialFirstLineEarly@^{__CFString=}$kCVImageBufferFieldDetailSpatialFirstLineLate@^{__CFString=}$kCVImageBufferFieldDetailTemporalBottomFirst@^{__CFString=}$kCVImageBufferFieldDetailTemporalTopFirst@^{__CFString=}$kCVImageBufferGammaLevelKey@^{__CFString=}$kCVImageBufferICCProfileKey@^{__CFString=}$kCVImageBufferPixelAspectRatioHorizontalSpacingKey@^{__CFString=}$kCVImageBufferPixelAspectRatioKey@^{__CFString=}$kCVImageBufferPixelAspectRatioVerticalSpacingKey@^{__CFString=}$kCVImageBufferPreferredCleanApertureKey@^{__CFString=}$kCVImageBufferTransferFunctionKey@^{__CFString=}$kCVImageBufferTransferFunction_EBU_3213@^{__CFString=}$kCVImageBufferTransferFunction_ITU_R_709_2@^{__CFString=}$kCVImageBufferTransferFunction_SMPTE_240M_1995@^{__CFString=}$kCVImageBufferTransferFunction_SMPTE_C@^{__CFString=}$kCVImageBufferTransferFunction_UseGamma@^{__CFString=}$kCVImageBufferYCbCrMatrixKey@^{__CFString=}$kCVImageBufferYCbCrMatrix_ITU_R_601_4@^{__CFString=}$kCVImageBufferYCbCrMatrix_ITU_R_709_2@^{__CFString=}$kCVImageBufferYCbCrMatrix_SMPTE_240M_1995@^{__CFString=}$kCVIndefiniteTime@{_CVTime=qii}$kCVOpenGLBufferHeight@^{__CFString=}$kCVOpenGLBufferInternalFormat@^{__CFString=}$kCVOpenGLBufferMaximumMipmapLevel@^{__CFString=}$kCVOpenGLBufferPoolMaximumBufferAgeKey@^{__CFString=}$kCVOpenGLBufferPoolMinimumBufferCountKey@^{__CFString=}$kCVOpenGLBufferTarget@^{__CFString=}$kCVOpenGLBufferWidth@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeAutomatic@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeBestPerformance@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeHighestQuality@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeKey@^{__CFString=}$kCVPixelBufferBytesPerRowAlignmentKey@^{__CFString=}$kCVPixelBufferCGBitmapContextCompatibilityKey@^{__CFString=}$kCVPixelBufferCGImageCompatibilityKey@^{__CFString=}$kCVPixelBufferExtendedPixelsBottomKey@^{__CFString=}$kCVPixelBufferExtendedPixelsLeftKey@^{__CFString=}$kCVPixelBufferExtendedPixelsRightKey@^{__CFString=}$kCVPixelBufferExtendedPixelsTopKey@^{__CFString=}$kCVPixelBufferHeightKey@^{__CFString=}$kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfacePropertiesKey@^{__CFString=}$kCVPixelBufferMemoryAllocatorKey@^{__CFString=}$kCVPixelBufferOpenGLCompatibilityKey@^{__CFString=}$kCVPixelBufferPixelFormatTypeKey@^{__CFString=}$kCVPixelBufferPlaneAlignmentKey@^{__CFString=}$kCVPixelBufferPoolAllocationThresholdKey@^{__CFString=}$kCVPixelBufferPoolFreeBufferNotification@^{__CFString=}$kCVPixelBufferPoolMaximumBufferAgeKey@^{__CFString=}$kCVPixelBufferPoolMinimumBufferCountKey@^{__CFString=}$kCVPixelBufferWidthKey@^{__CFString=}$kCVPixelFormatBitsPerBlock@^{__CFString=}$kCVPixelFormatBlackBlock@^{__CFString=}$kCVPixelFormatBlockHeight@^{__CFString=}$kCVPixelFormatBlockHorizontalAlignment@^{__CFString=}$kCVPixelFormatBlockVerticalAlignment@^{__CFString=}$kCVPixelFormatBlockWidth@^{__CFString=}$kCVPixelFormatCGBitmapContextCompatibility@^{__CFString=}$kCVPixelFormatCGBitmapInfo@^{__CFString=}$kCVPixelFormatCGImageCompatibility@^{__CFString=}$kCVPixelFormatCodecType@^{__CFString=}$kCVPixelFormatConstant@^{__CFString=}$kCVPixelFormatContainsAlpha@^{__CFString=}$kCVPixelFormatFillExtendedPixelsCallback@^{__CFString=}$kCVPixelFormatFourCC@^{__CFString=}$kCVPixelFormatHorizontalSubsampling@^{__CFString=}$kCVPixelFormatName@^{__CFString=}$kCVPixelFormatOpenGLCompatibility@^{__CFString=}$kCVPixelFormatOpenGLFormat@^{__CFString=}$kCVPixelFormatOpenGLInternalFormat@^{__CFString=}$kCVPixelFormatOpenGLType@^{__CFString=}$kCVPixelFormatPlanes@^{__CFString=}$kCVPixelFormatQDCompatibility@^{__CFString=}$kCVPixelFormatVerticalSubsampling@^{__CFString=}$kCVZeroTime@{_CVTime=qii}$'''
enums = '''$kCVAttachmentMode_ShouldNotPropagate@0$kCVAttachmentMode_ShouldPropagate@1$kCVPixelBufferLock_ReadOnly@1$kCVPixelFormatType_16BE555@16$kCVPixelFormatType_16BE565@1110783541$kCVPixelFormatType_16Gray@1647392359$kCVPixelFormatType_16LE555@1278555445$kCVPixelFormatType_16LE5551@892679473$kCVPixelFormatType_16LE565@1278555701$kCVPixelFormatType_1IndexedGray_WhiteIsZero@33$kCVPixelFormatType_1Monochrome@1$kCVPixelFormatType_24BGR@842285639$kCVPixelFormatType_24RGB@24$kCVPixelFormatType_2Indexed@2$kCVPixelFormatType_2IndexedGray_WhiteIsZero@34$kCVPixelFormatType_30RGB@1378955371$kCVPixelFormatType_32ABGR@1094862674$kCVPixelFormatType_32ARGB@32$kCVPixelFormatType_32AlphaGray@1647522401$kCVPixelFormatType_32BGRA@1111970369$kCVPixelFormatType_32RGBA@1380401729$kCVPixelFormatType_420YpCbCr8BiPlanarFullRange@875704422$kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange@875704438$kCVPixelFormatType_420YpCbCr8Planar@2033463856$kCVPixelFormatType_420YpCbCr8PlanarFullRange@1714696752$kCVPixelFormatType_422YpCbCr10@1983000880$kCVPixelFormatType_422YpCbCr16@1983000886$kCVPixelFormatType_422YpCbCr8@846624121$kCVPixelFormatType_422YpCbCr8FullRange@2037741158$kCVPixelFormatType_422YpCbCr8_yuvs@2037741171$kCVPixelFormatType_422YpCbCr_4A_8BiPlanar@1630697081$kCVPixelFormatType_4444AYpCbCr16@2033463606$kCVPixelFormatType_4444AYpCbCr8@2033463352$kCVPixelFormatType_4444YpCbCrA8@1983131704$kCVPixelFormatType_4444YpCbCrA8R@1916022840$kCVPixelFormatType_444YpCbCr10@1983131952$kCVPixelFormatType_444YpCbCr8@1983066168$kCVPixelFormatType_48RGB@1647589490$kCVPixelFormatType_4Indexed@4$kCVPixelFormatType_4IndexedGray_WhiteIsZero@36$kCVPixelFormatType_64ARGB@1647719521$kCVPixelFormatType_8Indexed@8$kCVPixelFormatType_8IndexedGray_WhiteIsZero@40$kCVReturnAllocationFailed@-6662$kCVReturnDisplayLinkAlreadyRunning@-6671$kCVReturnDisplayLinkCallbacksNotSet@-6673$kCVReturnDisplayLinkNotRunning@-6672$kCVReturnError@-6660$kCVReturnFirst@-6660$kCVReturnInvalidArgument@-6661$kCVReturnInvalidDisplay@-6670$kCVReturnInvalidPixelBufferAttributes@-6682$kCVReturnInvalidPixelFormat@-6680$kCVReturnInvalidPoolAttributes@-6691$kCVReturnInvalidSize@-6681$kCVReturnLast@-6699$kCVReturnPixelBufferNotOpenGLCompatible@-6683$kCVReturnPoolAllocationFailed@-6690$kCVReturnSuccess@0$kCVReturnWouldExceedAllocationThreshold@-6689$kCVSMPTETimeRunning@2$kCVSMPTETimeType24@0$kCVSMPTETimeType25@1$kCVSMPTETimeType2997@4$kCVSMPTETimeType2997Drop@5$kCVSMPTETimeType30@3$kCVSMPTETimeType30Drop@2$kCVSMPTETimeType5994@7$kCVSMPTETimeType60@6$kCVSMPTETimeValid@1$kCVTimeIsIndefinite@1$kCVTimeStampBottomField@131072$kCVTimeStampHostTimeValid@2$kCVTimeStampIsInterlaced@196608$kCVTimeStampRateScalarValid@16$kCVTimeStampSMPTETimeValid@4$kCVTimeStampTopField@65536$kCVTimeStampVideoHostTimeValid@3$kCVTimeStampVideoRefreshPeriodValid@8$kCVTimeStampVideoTimeValid@1$'''
misc.update({})
functions={'CVImageBufferGetEncodedSize': (sel32or64(b'{CGSize=ff}^{__CVBuffer=}', b'{CGSize=dd}^{__CVBuffer=}'),), 'CVOpenGLTextureRelease': (b'v^{__CVBuffer=}',), 'CVPixelBufferPoolRelease': (b'v^{__CVPixelBufferPool=}',), 'CVPixelBufferPoolGetTypeID': (b'L',), 'CVPixelBufferCreate': (sel32or64(b'i^{__CFAllocator=}LLL^{__CFDictionary=}^^{__CVBuffer=}', b'i^{__CFAllocator=}LLI^{__CFDictionary=}^^{__CVBuffer=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {5: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVOpenGLBufferPoolGetTypeID': (b'L',), 'CVPixelBufferFillExtendedPixels': (b'i^{__CVBuffer=}',), 'CVOpenGLTextureCacheRetain': (b'^{__CVOpenGLTextureCache=}^{__CVOpenGLTextureCache=}',), 'CVOpenGLBufferPoolCreateOpenGLBuffer': (b'i^{__CFAllocator=}^{__CVOpenGLBufferPool=}^^{__CVBuffer=}', '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVDisplayLinkSetCurrentCGDisplay': (b'i^{__CVDisplayLink=}I',), 'CVBufferSetAttachment': (b'v^{__CVBuffer=}^{__CFString=}@I',), 'CVGetCurrentHostTime': (b'Q',), 'CVPixelBufferPoolCreate': (b'i^{__CFAllocator=}^{__CFDictionary=}^{__CFDictionary=}^^{__CVPixelBufferPool=}', '', {'retval': {'already_cfretained': True}, 'arguments': {3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVPixelBufferGetHeightOfPlane': (b'L^{__CVBuffer=}L',), 'CVBufferRetain': (b'^{__CVBuffer=}^{__CVBuffer=}',), 'CVDisplayLinkTranslateTime': (sel32or64(b'i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), '', {'arguments': {1: {'type_modifier': 'n'}, 2: {'type_modifier': 'o'}}}), 'CVPixelBufferRetain': (b'^{__CVBuffer=}^{__CVBuffer=}',), 'CVPixelBufferGetPlaneCount': (b'L^{__CVBuffer=}',), 'CVOpenGLTextureCacheRelease': (b'v^{__CVOpenGLTextureCache=}',), 'CVPixelBufferGetBaseAddress': (b'^v^{__CVBuffer=}', '', {'comment': 'fixme', 'retval': {'c_array_of_variable_length': True}}), 'CVOpenGLBufferPoolRelease': (b'v^{__CVOpenGLBufferPool=}',), 'CVOpenGLTextureCacheGetTypeID': (b'L',), 'CVPixelBufferLockBaseAddress': (b'i^{__CVBuffer=}Q',), 'CVPixelBufferUnlockBaseAddress': (b'i^{__CVBuffer=}Q',), 'CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType': (sel32or64(b'v^{__CFDictionary=}L', b'v^{__CFDictionary=}I'),), 'CVOpenGLTextureIsFlipped': (b'Z^{__CVBuffer=}',), 'CVPixelBufferGetTypeID': (b'L',), 'CVDisplayLinkGetActualOutputVideoRefreshPeriod': (b'd^{__CVDisplayLink=}',), 'CVPixelBufferGetWidth': (b'L^{__CVBuffer=}',), 'CVDisplayLinkCreateWithCGDisplay': (b'iI^^{__CVDisplayLink=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVBufferRelease': (b'v^{__CVBuffer=}',), 'CVDisplayLinkStart': (b'i^{__CVDisplayLink=}',), 'CVDisplayLinkGetCurrentTime': (sel32or64(b'i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), '', {'arguments': {1: {'type_modifier': 'o'}}}), 'CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes': (b'^{__CFArray=}^{__CFAllocator=}', '', {'retval': {'already_cfretained': True}}), 'CVPixelBufferPoolGetAttributes': (b'^{__CFDictionary=}^{__CVPixelBufferPool=}',), 'CVBufferGetAttachments': (b'^{__CFDictionary=}^{__CVBuffer=}I',), 'CVOpenGLBufferPoolCreate': (b'i^{__CFAllocator=}^{__CFDictionary=}^{__CFDictionary=}^^{__CVOpenGLBufferPool=}', '', {'retval': {'already_cfretained': True}, 'arguments': {3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVDisplayLinkRetain': (b'^{__CVDisplayLink=}^{__CVDisplayLink=}',), 'CVPixelBufferCreateWithIOSurface': (b'i^{__CFAllocator=}^{__IOSurface=}^{__CFDictionary=}^^{__CVBuffer=}', '', {'retval': {'already_cfretained': True}, 'arguments': {3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVDisplayLinkCreateWithOpenGLDisplayMask': (b'iI^^{__CVDisplayLink=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVOpenGLBufferCreate': (b'i^{__CFAllocator=}LL^{__CFDictionary=}^^{__CVBuffer=}', '', {'retval': {'already_cfretained': True}, 'arguments': {4: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVPixelBufferPoolCreatePixelBufferWithAuxAttributes': (b'i^{__CFAllocator=}^{__CVPixelBufferPool=}^{__CFDictionary=}^^{__CVBuffer=}', '', {'retval': {'already_cfretained': True}}), 'CVOpenGLTextureCacheFlush': (b'v^{__CVOpenGLTextureCache=}Q',), 'CVDisplayLinkCreateWithActiveCGDisplays': (b'i^^{__CVDisplayLink=}', '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVDisplayLinkGetNominalOutputVideoRefreshPeriod': (b'{_CVTime=qii}^{__CVDisplayLink=}',), 'CVPixelBufferCreateResolvedAttributesDictionary': (b'i^{__CFAllocator=}^{__CFArray=}^^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVDisplayLinkSetOutputCallback': (b'i^{__CVDisplayLink=}^?^v', '', {'arguments': {1: {'callable': {'retval': {'type': b'i'}, 'arguments': {0: {'type': b'@'}, 1: {'type': b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}', 'type_modifier': 'n'}, 2: {'type': b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}', 'type_modifier': 'N'}, 3: {'type': b'Q'}, 4: {'type': b'^Q', 'type_modifier': 'o'}, 5: {'type': b'^v'}}}}}}), 'CVOpenGLTextureGetName': (b'I^{__CVBuffer=}',), 'CVOpenGLBufferRelease': (b'v^{__CVBuffer=}',), 'CVOpenGLTextureRetain': (b'^{__CVBuffer=}^{__CVBuffer=}',), 'CVPixelBufferIsPlanar': (b'Z^{__CVBuffer=}',), 'CVPixelBufferGetWidthOfPlane': (b'L^{__CVBuffer=}L',), 'CVBufferPropagateAttachments': (b'v^{__CVBuffer=}^{__CVBuffer=}',), 'CVPixelBufferPoolRetain': (b'^{__CVPixelBufferPool=}^{__CVPixelBufferPool=}',), 'CVPixelBufferGetHeight': (b'L^{__CVBuffer=}',), 'CVPixelBufferGetExtendedPixels': (b'v^{__CVBuffer=}^L^L^L^L', '', {'arguments': {1: {'type_modifier': 'o'}, 2: {'type_modifier': 'o'}, 3: {'type_modifier': 'o'}, 4: {'type_modifier': 'o'}}}), 'CVOpenGLBufferGetTypeID': (b'L',), 'CVDisplayLinkRelease': (b'v^{__CVDisplayLink=}',), 'CVBufferGetAttachment': (b'@^{__CVBuffer=}^{__CFString=}^I', '', {'arguments': {2: {'type_modifier': 'o'}}}), 'CVDisplayLinkStop': (b'i^{__CVDisplayLink=}',), 'CVPixelFormatDescriptionCreateWithPixelFormatType': (sel32or64(b'^{__CFDictionary=}^{__CFAllocator=}L', b'^{__CFDictionary=}^{__CFAllocator=}I'), '', {'retval': {'already_cfretained': True}}), 'CVPixelBufferGetIOSurface': (b'^{__IOSurface=}^{__CVBuffer=}',), 'CVOpenGLTextureCacheCreateTextureFromImage': (b'i^{__CFAllocator=}^{__CVOpenGLTextureCache=}@^{__CFDictionary=}^@', '', {'retval': {'already_cfretained': True}, 'arguments': {4: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVDisplayLinkCreateWithCGDisplays': (b'i^Il^^{__CVDisplayLink=}', '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVPixelBufferPoolGetPixelBufferAttributes': (b'^{__CFDictionary=}^{__CVPixelBufferPool=}',), 'CVOpenGLTextureGetTypeID': (b'L',), 'CVOpenGLBufferPoolGetAttributes': (b'^{__CFDictionary=}^{__CVOpenGLBufferPool=}',), 'CVBufferRemoveAllAttachments': (b'v^{__CVBuffer=}',), 'CVPixelBufferCreateWithBytes': (sel32or64(b'i^{__CFAllocator=}LLL^vL^?^v^{__CFDictionary=}^^{__CVBuffer=}', b'i^{__CFAllocator=}LLI^vL^?^v^{__CFDictionary=}^^{__CVBuffer=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {9: {'already_cfretained': True, 'type_modifier': 'o'}, 6: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^v'}}}}}}), 'CVOpenGLBufferPoolRetain': (b'^{__CVOpenGLBufferPool=}^{__CVOpenGLBufferPool=}',), 'CVPixelBufferCreateWithPlanarBytes': (sel32or64(b'i^{__CFAllocator=}LLL^vLL^^v^L^L^L^?^v^{__CFDictionary=}^^{__CVBuffer=}', b'i^{__CFAllocator=}LLI^vLL^^v^L^L^L^?^v^{__CFDictionary=}^^{__CVBuffer=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {11: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^v'}, 2: {'type': b'L'}, 3: {'type': b'L'}, 4: {'type': b'^^v'}}}}}}), 'CVImageBufferGetCleanRect': (sel32or64(b'{CGRect={CGPoint=ff}{CGSize=ff}}^{__CVBuffer=}', b'{CGRect={CGPoint=dd}{CGSize=dd}}^{__CVBuffer=}'),), 'CVPixelBufferGetBytesPerRowOfPlane': (b'L^{__CVBuffer=}L',), 'CVDisplayLinkGetTypeID': (b'L',), 'CVImageBufferGetDisplaySize': (sel32or64(b'{CGSize=ff}^{__CVBuffer=}', b'{CGSize=dd}^{__CVBuffer=}'),), 'CVPixelBufferGetDataSize': (b'L^{__CVBuffer=}',), 'CVOpenGLBufferPoolGetOpenGLBufferAttributes': (b'^{__CFDictionary=}^{__CVOpenGLBufferPool=}',), 'CVOpenGLBufferAttach': (b'i^{__CVBuffer=}^{_CGLContextObject=}Iii',), 'CVPixelBufferGetBaseAddressOfPlane': (b'^v^{__CVBuffer=}L', '', {'comment': 'fixme', 'retval': {'c_array_of_variable_length': True}}), 'CVDisplayLinkIsRunning': (b'Z^{__CVDisplayLink=}',), 'CVPixelBufferGetPixelFormatType': (sel32or64(b'L^{__CVBuffer=}', b'I^{__CVBuffer=}'),), 'CVBufferRemoveAttachment': (b'v^{__CVBuffer=}^{__CFString=}',), 'CVOpenGLBufferGetAttributes': (b'^{__CFDictionary=}@',), 'CVDisplayLinkGetOutputVideoLatency': (b'{_CVTime=qii}^{__CVDisplayLink=}',), 'CVPixelBufferGetBytesPerRow': (b'L^{__CVBuffer=}',), 'CVPixelBufferPoolCreatePixelBuffer': (b'i^{__CFAllocator=}^{__CVPixelBufferPool=}^^{__CVBuffer=}', '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVImageBufferGetColorSpace': (b'^{CGColorSpace=}^{__CVBuffer=}',), 'CVDisplayLinkGetCurrentCGDisplay': (b'I^{__CVDisplayLink=}',), 'CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext': (b'i^{__CVDisplayLink=}^{_CGLContextObject=}^{_CGLPixelFormatObject=}',), 'CVPixelBufferRelease': (b'v^{__CVBuffer=}',), 'CVBufferSetAttachments': (b'v^{__CVBuffer=}^{__CFDictionary=}I',), 'CVOpenGLTextureGetTarget': (b'I^{__CVBuffer=}',), 'CVGetHostClockFrequency': (b'd',), 'CVGetHostClockMinimumTimeDelta': (b'I',), 'CVOpenGLBufferRetain': (b'^{__CVBuffer=}^{__CVBuffer=}',), 'CVOpenGLTextureCacheCreate': (b'i^{__CFAllocator=}^{__CFDictionary=}^{_CGLContextObject=}^{_CGLPixelFormatObject=}^{__CFDictionary=}^^{__CVOpenGLTextureCache=}', '', {'retval': {'already_cfretained': True}, 'arguments': {5: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CVOpenGLTextureGetCleanTexCoords': (b'v^{__CVBuffer=}[2f][2f][2f][2f]',)}
aliases = {'CV_INLINE': 'CF_INLINE'}
cftypes=[('CVBufferRef', b'^{__CVBuffer=}', 'CVBufferGetTypeID', None), ('CVDisplayLinkRef', b'^{__CVDisplayLink=}', 'CVDisplayLinkGetTypeID', None), ('CVOpenGLBufferPoolRef', b'^{__CVOpenGLBufferPool=}', 'CVOpenGLBufferPoolGetTypeID', None), ('CVOpenGLTextureCacheRef', b'^{__CVOpenGLTextureCache=}', 'CVOpenGLTextureCacheGetTypeID', None), ('CVPixelBufferPoolRef', b'^{__CVPixelBufferPool=}', 'CVPixelBufferPoolGetTypeID', None), ('CVOpenGLBufferRef', b'^{__CVOpenGLBuffer=}', 'CVOpenGLBufferGetTypeID', None), ('CVPixelBufferRef', b'^{__CVPixelBuffer=}', 'CVPixelBufferGetTypeID', None), ('CVOpenGLTextureRef', b'^{__CVOpenGLTexture=}', 'CVOpenGLTextureGetTypeID', None)]
expressions = {}

# END OF FILE
