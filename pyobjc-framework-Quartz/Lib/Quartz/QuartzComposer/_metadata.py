# This file is generated by objective.metadata
#
# Last update: Wed May  9 13:36:12 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$QCCompositionAttributeBuiltInKey$QCCompositionAttributeCategoryKey$QCCompositionAttributeCopyrightKey$QCCompositionAttributeDescriptionKey$QCCompositionAttributeHasConsumersKey$QCCompositionAttributeIsTimeDependentKey$QCCompositionAttributeNameKey$QCCompositionCategoryDistortion$QCCompositionCategoryStylize$QCCompositionCategoryUtility$QCCompositionInputAudioPeakKey$QCCompositionInputAudioSpectrumKey$QCCompositionInputDestinationImageKey$QCCompositionInputImageKey$QCCompositionInputPaceKey$QCCompositionInputPreviewModeKey$QCCompositionInputPrimaryColorKey$QCCompositionInputRSSArticleDurationKey$QCCompositionInputRSSFeedURLKey$QCCompositionInputScreenImageKey$QCCompositionInputSecondaryColorKey$QCCompositionInputSourceImageKey$QCCompositionInputTrackInfoKey$QCCompositionInputTrackPositionKey$QCCompositionInputTrackSignalKey$QCCompositionInputXKey$QCCompositionInputYKey$QCCompositionOutputImageKey$QCCompositionOutputWebPageURLKey$QCCompositionPickerPanelDidSelectCompositionNotification$QCCompositionPickerViewDidSelectCompositionNotification$QCCompositionProtocolGraphicAnimation$QCCompositionProtocolGraphicTransition$QCCompositionProtocolImageFilter$QCCompositionProtocolMusicVisualizer$QCCompositionProtocolRSSVisualizer$QCCompositionProtocolScreenSaver$QCCompositionRepositoryDidUpdateNotification$QCPlugInAttributeCategoriesKey$QCPlugInAttributeCopyrightKey$QCPlugInAttributeDescriptionKey$QCPlugInAttributeExamplesKey$QCPlugInAttributeNameKey$QCPlugInExecutionArgumentEventKey$QCPlugInExecutionArgumentMouseLocationKey$QCPlugInPixelFormatARGB8$QCPlugInPixelFormatBGRA8$QCPlugInPixelFormatI8$QCPlugInPixelFormatIf$QCPlugInPixelFormatRGBAf$QCPortAttributeDefaultValueKey$QCPortAttributeMaximumValueKey$QCPortAttributeMenuItemsKey$QCPortAttributeMinimumValueKey$QCPortAttributeNameKey$QCPortAttributeTypeKey$QCPortTypeBoolean$QCPortTypeColor$QCPortTypeImage$QCPortTypeIndex$QCPortTypeNumber$QCPortTypeString$QCPortTypeStructure$QCRendererEventKey$QCRendererMouseLocationKey$QCViewDidStartRenderingNotification$QCViewDidStopRenderingNotification$'''
enums = '''$kQCPlugInExecutionModeConsumer@3$kQCPlugInExecutionModeProcessor@2$kQCPlugInExecutionModeProvider@1$kQCPlugInTimeModeIdle@1$kQCPlugInTimeModeNone@0$kQCPlugInTimeModeTimeBase@2$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'compositionParameterView:shouldDisplayParameterWithKey:attributes:', {'retval': {'type': b'Z'}})
    r('QCCompositionParameterView', b'drawsBackground', {'retval': {'type': b'Z'}})
    r('QCCompositionParameterView', b'hasParameters', {'retval': {'type': b'Z'}})
    r('QCCompositionParameterView', b'setDrawsBackground:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'allowsEmptySelection', {'retval': {'type': b'Z'}})
    r('QCCompositionPickerView', b'drawsBackground', {'retval': {'type': b'Z'}})
    r('QCCompositionPickerView', b'isAnimating', {'retval': {'type': b'Z'}})
    r('QCCompositionPickerView', b'setAllowsEmptySelection:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'setDrawsBackground:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'setShowsCompositionNames:', {'arguments': {2: {'type': b'Z'}}})
    r('QCCompositionPickerView', b'showsCompositionNames', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'didValueForInputKeyChange:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'execute:atTime:withArguments:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'loadPlugInAtPath:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'setValue:forOutputKey:', {'retval': {'type': b'Z'}})
    r('QCPlugIn', b'startExecution:', {'retval': {'type': b'Z'}})
    r('QCRenderer', b'renderAtTime:arguments:', {'retval': {'type': b'Z'}})
    r('QCView', b'autostartsRendering', {'retval': {'type': b'Z'}})
    r('QCView', b'isPausedRendering', {'retval': {'type': b'Z'}})
    r('QCView', b'isRendering', {'retval': {'type': b'Z'}})
    r('QCView', b'loadComposition:', {'retval': {'type': b'Z'}})
    r('QCView', b'loadCompositionFromFile:', {'retval': {'type': b'Z'}})
    r('QCView', b'renderAtTime:arguments:', {'retval': {'type': b'Z'}})
    r('QCView', b'setAutostartsRendering:', {'arguments': {2: {'type': b'Z'}}})
    r('QCView', b'startRendering', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'CGLContextObj', {'required': True, 'retval': {'type': b'^{_CGLContextObject=}'}})
    r('NSObject', b'attributes', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'bindTextureRepresentationToCGLContext:textureUnit:normalizeCoordinates:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 3: {'type': b'I'}, 4: {'type': b'Z'}}})
    r('NSObject', b'bounds', {'required': True, 'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}})
    r('NSObject', b'bufferBaseAddress', {'required': True, 'retval': {'type': b'^v'}})
    r('NSObject', b'bufferBytesPerRow', {'required': True, 'retval': {'type': sel32or64(b'I', b'L')}})
    r('NSObject', b'bufferColorSpace', {'required': True, 'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'bufferPixelFormat', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'bufferPixelsHigh', {'required': True, 'retval': {'type': sel32or64(b'I', b'L')}})
    r('NSObject', b'bufferPixelsWide', {'required': True, 'retval': {'type': sel32or64(b'I', b'L')}})
    r('NSObject', b'canRenderWithCGLContext:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}}})
    r('NSObject', b'colorSpace', {'required': True, 'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'compositionURL', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'copyRenderedTextureForCGLContext:pixelFormat:bounds:isFlipped:', {'required': False, 'retval': {'type': b'I'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 3: {'type': b'@'}, 4: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}, 5: {'type': b'^Z'}}})
    r('NSObject', b'imageBounds', {'required': True, 'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}})
    r('NSObject', b'imageBounds', {'required': True, 'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}})
    r('NSObject', b'imageColorSpace', {'required': True, 'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'imageColorSpace', {'required': True, 'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'inputKeys', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'lockBufferRepresentationWithPixelFormat:colorSpace:forBounds:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'^{CGColorSpace=}'}, 4: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}}})
    r('NSObject', b'lockTextureRepresentationWithColorSpace:forBounds:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{CGColorSpace=}'}, 3: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}}})
    r('NSObject', b'logMessage:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}, 'variadic': True})
    r('NSObject', b'outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'L')}, 4: {'type': sel32or64(b'I', b'L')}, 5: {'type': b'^v'}, 6: {'type': sel32or64(b'I', b'L')}, 7: {'type': b'^?'}, 8: {'type': b'^v'}, 9: {'type': b'^{CGColorSpace=}'}, 10: {'type': b'Z'}}})
    r('NSObject', b'outputImageProviderFromTextureWithPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'L')}, 4: {'type': sel32or64(b'I', b'L')}, 5: {'type': b'I'}, 6: {'type': b'Z'}, 7: {'type': b'^?'}, 8: {'type': b'^v'}, 9: {'type': b'^{CGColorSpace=}'}, 10: {'type': b'Z'}}})
    r('NSObject', b'outputKeys', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'propertyListFromInputValues', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'releaseRenderedTexture:forCGLContext:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'I'}, 3: {'type': b'^{_CGLContextObject=}'}}})
    r('NSObject', b'renderToBuffer:withBytesPerRow:pixelFormat:forBounds:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^v'}, 3: {'type': sel32or64(b'I', b'L')}, 4: {'type': b'@'}, 5: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}}})
    r('NSObject', b'renderWithCGLContext:forBounds:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 3: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}}})
    r('NSObject', b'setInputValuesWithPropertyList:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'setValue:forInputKey:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'shouldColorMatch', {'required': False, 'retval': {'type': b'Z'}})
    r('NSObject', b'shouldColorMatch', {'required': True, 'retval': {'type': b'Z'}})
    r('NSObject', b'supportedBufferPixelFormats', {'required': False, 'retval': {'type': b'@'}})
    r('NSObject', b'supportedRenderedTexturePixelFormats', {'required': False, 'retval': {'type': b'@'}})
    r('NSObject', b'textureColorSpace', {'required': True, 'retval': {'type': b'^{CGColorSpace=}'}})
    r('NSObject', b'textureFlipped', {'required': True, 'retval': {'type': b'Z'}})
    r('NSObject', b'textureMatrix', {'required': True, 'retval': {'type': b'^f'}})
    r('NSObject', b'textureName', {'required': True, 'retval': {'type': b'I'}})
    r('NSObject', b'texturePixelsHigh', {'required': True, 'retval': {'type': sel32or64(b'I', b'L')}})
    r('NSObject', b'texturePixelsWide', {'required': True, 'retval': {'type': sel32or64(b'I', b'L')}})
    r('NSObject', b'textureTarget', {'required': True, 'retval': {'type': b'I'}})
    r('NSObject', b'unbindTextureRepresentationFromCGLContext:textureUnit:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^{_CGLContextObject=}'}, 3: {'type': b'I'}}})
    r('NSObject', b'unlockBufferRepresentation', {'required': True, 'retval': {'type': b'v'}})
    r('NSObject', b'unlockTextureRepresentation', {'required': True, 'retval': {'type': b'v'}})
    r('NSObject', b'userInfo', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'userInfo', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'valueForInputKey:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'valueForOutputKey:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'valueForOutputKey:ofType:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'compositionParameterView:didChangeParameterWithKey:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'compositionParameterView:shouldDisplayParameterWithKey:attributes:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('NSObject', b'compositionPickerView:didSelectComposition:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'compositionPickerViewDidStartAnimating:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'compositionPickerViewWillStopAnimating:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
protocols={'QCCompositionPickerViewDelegate': objc.informal_protocol('QCCompositionPickerViewDelegate', [objc.selector(None, 'compositionPickerView:didSelectComposition:', b'v@:@@', isRequired=False), objc.selector(None, 'compositionPickerViewWillStopAnimating:', b'v@:@', isRequired=False), objc.selector(None, 'compositionPickerViewDidStartAnimating:', b'v@:@', isRequired=False)]), 'QCCompositionParameterViewDelegate': objc.informal_protocol('QCCompositionParameterViewDelegate', [objc.selector(None, 'compositionParameterView:didChangeParameterWithKey:', b'v@:@@', isRequired=False), objc.selector(None, 'compositionParameterView:shouldDisplayParameterWithKey:attributes:', b'Z@:@@@', isRequired=False)])}
expressions = {}

# END OF FILE
