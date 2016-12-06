from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSXMLParser (TestCase):
    def testConstants(self):
        self.assertEqual(NSXMLParserInternalError, 1)
        self.assertEqual(NSXMLParserOutOfMemoryError, 2)
        self.assertEqual(NSXMLParserDocumentStartError, 3)
        self.assertEqual(NSXMLParserEmptyDocumentError, 4)
        self.assertEqual(NSXMLParserPrematureDocumentEndError, 5)
        self.assertEqual(NSXMLParserInvalidHexCharacterRefError, 6)
        self.assertEqual(NSXMLParserInvalidDecimalCharacterRefError, 7)
        self.assertEqual(NSXMLParserInvalidCharacterRefError, 8)
        self.assertEqual(NSXMLParserInvalidCharacterError, 9)
        self.assertEqual(NSXMLParserCharacterRefAtEOFError, 10)
        self.assertEqual(NSXMLParserCharacterRefInPrologError, 11)
        self.assertEqual(NSXMLParserCharacterRefInEpilogError, 12)
        self.assertEqual(NSXMLParserCharacterRefInDTDError, 13)
        self.assertEqual(NSXMLParserEntityRefAtEOFError, 14)
        self.assertEqual(NSXMLParserEntityRefInPrologError, 15)
        self.assertEqual(NSXMLParserEntityRefInEpilogError, 16)
        self.assertEqual(NSXMLParserEntityRefInDTDError, 17)
        self.assertEqual(NSXMLParserParsedEntityRefAtEOFError, 18)
        self.assertEqual(NSXMLParserParsedEntityRefInPrologError, 19)
        self.assertEqual(NSXMLParserParsedEntityRefInEpilogError, 20)
        self.assertEqual(NSXMLParserParsedEntityRefInInternalSubsetError, 21)
        self.assertEqual(NSXMLParserEntityReferenceWithoutNameError, 22)
        self.assertEqual(NSXMLParserEntityReferenceMissingSemiError, 23)
        self.assertEqual(NSXMLParserParsedEntityRefNoNameError, 24)
        self.assertEqual(NSXMLParserParsedEntityRefMissingSemiError, 25)
        self.assertEqual(NSXMLParserUndeclaredEntityError, 26)
        self.assertEqual(NSXMLParserUnparsedEntityError, 28)
        self.assertEqual(NSXMLParserEntityIsExternalError, 29)
        self.assertEqual(NSXMLParserEntityIsParameterError, 30)
        self.assertEqual(NSXMLParserUnknownEncodingError, 31)
        self.assertEqual(NSXMLParserEncodingNotSupportedError, 32)
        self.assertEqual(NSXMLParserStringNotStartedError, 33)
        self.assertEqual(NSXMLParserStringNotClosedError, 34)
        self.assertEqual(NSXMLParserNamespaceDeclarationError, 35)
        self.assertEqual(NSXMLParserEntityNotStartedError, 36)
        self.assertEqual(NSXMLParserEntityNotFinishedError, 37)
        self.assertEqual(NSXMLParserLessThanSymbolInAttributeError, 38)
        self.assertEqual(NSXMLParserAttributeNotStartedError, 39)
        self.assertEqual(NSXMLParserAttributeNotFinishedError, 40)
        self.assertEqual(NSXMLParserAttributeHasNoValueError, 41)
        self.assertEqual(NSXMLParserAttributeRedefinedError, 42)
        self.assertEqual(NSXMLParserLiteralNotStartedError, 43)
        self.assertEqual(NSXMLParserLiteralNotFinishedError, 44)
        self.assertEqual(NSXMLParserCommentNotFinishedError, 45)
        self.assertEqual(NSXMLParserProcessingInstructionNotStartedError, 46)
        self.assertEqual(NSXMLParserProcessingInstructionNotFinishedError, 47)
        self.assertEqual(NSXMLParserNotationNotStartedError, 48)
        self.assertEqual(NSXMLParserNotationNotFinishedError, 49)
        self.assertEqual(NSXMLParserAttributeListNotStartedError, 50)
        self.assertEqual(NSXMLParserAttributeListNotFinishedError, 51)
        self.assertEqual(NSXMLParserMixedContentDeclNotStartedError, 52)
        self.assertEqual(NSXMLParserMixedContentDeclNotFinishedError, 53)
        self.assertEqual(NSXMLParserElementContentDeclNotStartedError, 54)
        self.assertEqual(NSXMLParserElementContentDeclNotFinishedError, 55)
        self.assertEqual(NSXMLParserXMLDeclNotStartedError, 56)
        self.assertEqual(NSXMLParserXMLDeclNotFinishedError, 57)
        self.assertEqual(NSXMLParserConditionalSectionNotStartedError, 58)
        self.assertEqual(NSXMLParserConditionalSectionNotFinishedError, 59)
        self.assertEqual(NSXMLParserExternalSubsetNotFinishedError, 60)
        self.assertEqual(NSXMLParserDOCTYPEDeclNotFinishedError, 61)
        self.assertEqual(NSXMLParserMisplacedCDATAEndStringError, 62)
        self.assertEqual(NSXMLParserCDATANotFinishedError, 63)
        self.assertEqual(NSXMLParserMisplacedXMLDeclarationError, 64)
        self.assertEqual(NSXMLParserSpaceRequiredError, 65)
        self.assertEqual(NSXMLParserSeparatorRequiredError, 66)
        self.assertEqual(NSXMLParserNMTOKENRequiredError, 67)
        self.assertEqual(NSXMLParserNAMERequiredError, 68)
        self.assertEqual(NSXMLParserPCDATARequiredError, 69)
        self.assertEqual(NSXMLParserURIRequiredError, 70)
        self.assertEqual(NSXMLParserPublicIdentifierRequiredError, 71)
        self.assertEqual(NSXMLParserLTRequiredError, 72)
        self.assertEqual(NSXMLParserGTRequiredError, 73)
        self.assertEqual(NSXMLParserLTSlashRequiredError, 74)
        self.assertEqual(NSXMLParserEqualExpectedError, 75)
        self.assertEqual(NSXMLParserTagNameMismatchError, 76)
        self.assertEqual(NSXMLParserUnfinishedTagError, 77)
        self.assertEqual(NSXMLParserStandaloneValueError, 78)
        self.assertEqual(NSXMLParserInvalidEncodingNameError, 79)
        self.assertEqual(NSXMLParserCommentContainsDoubleHyphenError, 80)
        self.assertEqual(NSXMLParserInvalidEncodingError, 81)
        self.assertEqual(NSXMLParserExternalStandaloneEntityError, 82)
        self.assertEqual(NSXMLParserInvalidConditionalSectionError, 83)
        self.assertEqual(NSXMLParserEntityValueRequiredError, 84)
        self.assertEqual(NSXMLParserNotWellBalancedError, 85)
        self.assertEqual(NSXMLParserExtraContentError, 86)
        self.assertEqual(NSXMLParserInvalidCharacterInEntityError, 87)
        self.assertEqual(NSXMLParserParsedEntityRefInInternalError, 88)
        self.assertEqual(NSXMLParserEntityRefLoopError, 89)
        self.assertEqual(NSXMLParserEntityBoundaryError, 90)
        self.assertEqual(NSXMLParserInvalidURIError, 91)
        self.assertEqual(NSXMLParserURIFragmentError, 92)
        self.assertEqual(NSXMLParserNoDTDError, 94)
        self.assertEqual(NSXMLParserDelegateAbortedParseError, 512)

        self.assertIsInstance(NSXMLParserErrorDomain, unicode)

        self.assertEqual(NSXMLParserResolveExternalEntitiesNever, 0)
        self.assertEqual(NSXMLParserResolveExternalEntitiesNoNetwork, 1)
        self.assertEqual(NSXMLParserResolveExternalEntitiesSameOriginOnly, 2)
        self.assertEqual(NSXMLParserResolveExternalEntitiesAlways, 3)

    def testMethods(self):
        self.assertArgIsBOOL(NSXMLParser.setShouldProcessNamespaces_, 0)
        self.assertArgIsBOOL(NSXMLParser.setShouldReportNamespacePrefixes_, 0)
        self.assertArgIsBOOL(NSXMLParser.setShouldResolveExternalEntities_, 0)
        self.assertResultIsBOOL(NSXMLParser.shouldProcessNamespaces)
        self.assertResultIsBOOL(NSXMLParser.shouldReportNamespacePrefixes)
        self.assertResultIsBOOL(NSXMLParser.shouldResolveExternalEntities)
        self.assertResultIsBOOL(NSXMLParser.parse)

    @min_sdk_level('10.6')
    def testProtocols(self):
        objc.protocolNamed('NSXMLParserDelegate')

if __name__ == "__main__":
    main()
