# This file is generated by objective.metadata
#
# Last update: Wed May  9 13:36:07 2012

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
constants = '''$PDFDocumentAuthorAttribute$PDFDocumentCreationDateAttribute$PDFDocumentCreatorAttribute$PDFDocumentDidBeginFindNotification$PDFDocumentDidBeginPageFindNotification$PDFDocumentDidBeginPageWriteNotification$PDFDocumentDidBeginWriteNotification$PDFDocumentDidEndFindNotification$PDFDocumentDidEndPageFindNotification$PDFDocumentDidEndPageWriteNotification$PDFDocumentDidEndWriteNotification$PDFDocumentDidFindMatchNotification$PDFDocumentDidUnlockNotification$PDFDocumentKeywordsAttribute$PDFDocumentModificationDateAttribute$PDFDocumentProducerAttribute$PDFDocumentSubjectAttribute$PDFDocumentTitleAttribute$PDFThumbnailViewDocumentEditedNotification$PDFViewAnnotationHitNotification$PDFViewAnnotationWillHitNotification$PDFViewChangedHistoryNotification$PDFViewCopyPermissionNotification$PDFViewDisplayBoxChangedNotification$PDFViewDisplayModeChangedNotification$PDFViewDocumentChangedNotification$PDFViewPageChangedNotification$PDFViewPrintPermissionNotification$PDFViewScaleChangedNotification$PDFViewSelectionChangedNotification$'''
enums = '''$kPDFActionNamedFind@8$kPDFActionNamedFirstPage@3$kPDFActionNamedGoBack@5$kPDFActionNamedGoForward@6$kPDFActionNamedGoToPage@7$kPDFActionNamedLastPage@4$kPDFActionNamedNextPage@1$kPDFActionNamedNone@0$kPDFActionNamedPreviousPage@2$kPDFActionNamedPrint@9$kPDFActionNamedZoomIn@10$kPDFActionNamedZoomOut@11$kPDFAnnotationArea@4$kPDFBorderStyleBeveled@2$kPDFBorderStyleDashed@1$kPDFBorderStyleInset@3$kPDFBorderStyleSolid@0$kPDFBorderStyleUnderline@4$kPDFControlArea@16$kPDFDisplayBoxArtBox@4$kPDFDisplayBoxBleedBox@2$kPDFDisplayBoxCropBox@1$kPDFDisplayBoxMediaBox@0$kPDFDisplayBoxTrimBox@3$kPDFDisplaySinglePage@0$kPDFDisplaySinglePageContinuous@1$kPDFDisplayTwoUp@2$kPDFDisplayTwoUpContinuous@3$kPDFDocumentPermissionsNone@0$kPDFDocumentPermissionsOwner@2$kPDFDocumentPermissionsUser@1$kPDFIconArea@64$kPDFInterpolationQualityHigh@2$kPDFInterpolationQualityLow@1$kPDFInterpolationQualityNone@0$kPDFLineStyleCircle@2$kPDFLineStyleClosedArrow@5$kPDFLineStyleDiamond@3$kPDFLineStyleNone@0$kPDFLineStyleOpenArrow@4$kPDFLineStyleSquare@1$kPDFLinkArea@8$kPDFMarkupTypeHighlight@0$kPDFMarkupTypeStrikeOut@1$kPDFMarkupTypeUnderline@2$kPDFNoArea@0$kPDFPageArea@1$kPDFPopupArea@128$kPDFPrintPageScaleDownToFit@2$kPDFPrintPageScaleNone@0$kPDFPrintPageScaleToFit@1$kPDFTextAnnotationIconComment@0$kPDFTextAnnotationIconHelp@3$kPDFTextAnnotationIconInsert@6$kPDFTextAnnotationIconKey@1$kPDFTextAnnotationIconNewParagraph@4$kPDFTextAnnotationIconNote@2$kPDFTextAnnotationIconParagraph@5$kPDFTextArea@2$kPDFTextFieldArea@32$kPDFWidgetCheckBoxControl@2$kPDFWidgetPushButtonControl@0$kPDFWidgetRadioButtonControl@1$kPDFWidgetUnknownControl@-1$'''
misc.update({})
aliases = {'kPDFDestinationUnspecifiedValue': 'FLT_MAX'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('PDFActionResetForm', b'fieldsIncludedAreCleared', {'retval': {'type': b'Z'}})
    r('PDFActionResetForm', b'setFieldsIncludedAreCleared:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotation', b'hasAppearanceStream', {'retval': {'type': b'Z'}})
    r('PDFAnnotation', b'setShouldDisplay:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotation', b'setShouldPrint:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotation', b'shouldDisplay', {'retval': {'type': b'Z'}})
    r('PDFAnnotation', b'shouldPrint', {'retval': {'type': b'Z'}})
    r('PDFAnnotationButtonWidget', b'allowsToggleToOff', {'retval': {'type': b'Z'}})
    r('PDFAnnotationButtonWidget', b'isHighlighted', {'retval': {'type': b'Z'}})
    r('PDFAnnotationButtonWidget', b'setAllowsToggleToOff:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotationButtonWidget', b'setHighlighted:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotationChoiceWidget', b'isListChoice', {'retval': {'type': b'Z'}})
    r('PDFAnnotationChoiceWidget', b'setIsListChoice:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotationLink', b'setHighlighted:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFAnnotationPopup', b'isOpen', {'retval': {'type': b'Z'}})
    r('PDFAnnotationPopup', b'setIsOpen:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFDocument', b'allowsCopying', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'allowsPrinting', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'isEncrypted', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'isFinding', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'isLocked', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'printOperationForPrintInfo:scalingMode:autoRotate:', {'arguments': {4: {'type': b'Z'}}})
    r('PDFDocument', b'unlockWithPassword:', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'writeToFile:', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'writeToFile:withOptions:', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'writeToURL:', {'retval': {'type': b'Z'}})
    r('PDFDocument', b'writeToURL:withOptions:', {'retval': {'type': b'Z'}})
    r('PDFOutline', b'isOpen', {'retval': {'type': b'Z'}})
    r('PDFOutline', b'setIsOpen:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFPage', b'displaysAnnotations', {'retval': {'type': b'Z'}})
    r('PDFPage', b'setDisplaysAnnotations:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFSelection', b'drawForPage:active:', {'arguments': {3: {'type': b'Z'}}})
    r('PDFSelection', b'drawForPage:withBox:active:', {'arguments': {4: {'type': b'Z'}}})
    r('PDFThumbnailView', b'allowsDragging', {'retval': {'type': b'Z'}})
    r('PDFThumbnailView', b'allowsMultipleSelection', {'retval': {'type': b'Z'}})
    r('PDFThumbnailView', b'setAllowsDragging:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFThumbnailView', b'setAllowsMultipleSelection:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'allowsDragging', {'retval': {'type': b'Z'}})
    r('PDFView', b'autoScales', {'retval': {'type': b'Z'}})
    r('PDFView', b'canGoBack', {'retval': {'type': b'Z'}})
    r('PDFView', b'canGoForward', {'retval': {'type': b'Z'}})
    r('PDFView', b'canGoToFirstPage', {'retval': {'type': b'Z'}})
    r('PDFView', b'canGoToLastPage', {'retval': {'type': b'Z'}})
    r('PDFView', b'canGoToNextPage', {'retval': {'type': b'Z'}})
    r('PDFView', b'canGoToPreviousPage', {'retval': {'type': b'Z'}})
    r('PDFView', b'canZoomIn', {'retval': {'type': b'Z'}})
    r('PDFView', b'canZoomOut', {'retval': {'type': b'Z'}})
    r('PDFView', b'displaysAsBook', {'retval': {'type': b'Z'}})
    r('PDFView', b'displaysPageBreaks', {'retval': {'type': b'Z'}})
    r('PDFView', b'enableDataDetectors', {'retval': {'type': b'Z'}})
    r('PDFView', b'pageForPoint:nearest:', {'arguments': {3: {'type': b'Z'}}})
    r('PDFView', b'printWithInfo:autoRotate:', {'arguments': {3: {'type': b'Z'}}})
    r('PDFView', b'printWithInfo:autoRotate:pageScaling:', {'arguments': {3: {'type': b'Z'}}})
    r('PDFView', b'setAllowsDragging:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'setAutoScales:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'setCurrentSelection:animate:', {'arguments': {3: {'type': b'Z'}}})
    r('PDFView', b'setDisplaysAsBook:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'setDisplaysPageBreaks:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'setEnableDataDetectors:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'setShouldAntiAlias:', {'arguments': {2: {'type': b'Z'}}})
    r('PDFView', b'shouldAntiAlias', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'PDFViewOpenPDF:forRemoteGoToAction:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'PDFViewPerformFind:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'PDFViewPerformGoToPage:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'PDFViewPerformPrint:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'PDFViewPrintJobTitle:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'PDFViewWillChangeScaleFactor:toScale:', {'retval': {'type': sel32or64(b'f', b'd')}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'f', b'd')}}})
    r('NSObject', b'PDFViewWillClickOnLink:withURL:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'classForAnnotationClass:', {'retval': {'type': b'^{objc_class=}'}, 'arguments': {2: {'type': b'^{objc_class=}'}}})
    r('NSObject', b'classForPage', {'retval': {'type': b'^{objc_class=}'}})
    r('NSObject', b'didMatchString:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'documentDidBeginDocumentFind:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'documentDidBeginPageFind:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'documentDidEndDocumentFind:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'documentDidEndPageFind:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'documentDidFindMatch:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'documentDidUnlock:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
protocols={'PDFViewDelegate': objc.informal_protocol('PDFViewDelegate', [objc.selector(None, 'PDFViewWillClickOnLink:withURL:', b'v@:@@', isRequired=False), objc.selector(None, 'PDFViewOpenPDF:forRemoteGoToAction:', b'v@:@@', isRequired=False), objc.selector(None, 'PDFViewPerformFind:', b'v@:@', isRequired=False), objc.selector(None, 'PDFViewWillChangeScaleFactor:toScale:', sel32or64(b'f@:@f', b'd@:@d'), isRequired=False), objc.selector(None, 'PDFViewPerformPrint:', b'v@:@', isRequired=False), objc.selector(None, 'PDFViewPrintJobTitle:', b'@@:@', isRequired=False), objc.selector(None, 'PDFViewPerformGoToPage:', b'v@:@', isRequired=False)]), 'PDFDocumentDelegate': objc.informal_protocol('PDFDocumentDelegate', [objc.selector(None, 'classForPage', b'^{objc_class=}@:', isRequired=False), objc.selector(None, 'classForAnnotationClass:', b'^{objc_class=}@:^{objc_class=}', isRequired=False), objc.selector(None, 'didMatchString:', b'v@:@', isRequired=False)]), 'PDFDocumentNotifications': objc.informal_protocol('PDFDocumentNotifications', [objc.selector(None, 'documentDidFindMatch:', b'v@:@', isRequired=False), objc.selector(None, 'documentDidBeginPageFind:', b'v@:@', isRequired=False), objc.selector(None, 'documentDidBeginDocumentFind:', b'v@:@', isRequired=False), objc.selector(None, 'documentDidUnlock:', b'v@:@', isRequired=False), objc.selector(None, 'documentDidEndPageFind:', b'v@:@', isRequired=False), objc.selector(None, 'documentDidEndDocumentFind:', b'v@:@', isRequired=False)])}
expressions = {}

# END OF FILE
