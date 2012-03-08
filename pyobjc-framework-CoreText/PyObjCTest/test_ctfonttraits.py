
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontTraits (TestCase):

    def testConstants(self):
        self.assertIsInstance(kCTFontSymbolicTrait, unicode)
        self.assertIsInstance(kCTFontWeightTrait, unicode)
        self.assertIsInstance(kCTFontWidthTrait, unicode)
        self.assertIsInstance(kCTFontSlantTrait, unicode)

        self.assertEqual(kCTFontClassMaskShift, 28)

        self.assertEqual(kCTFontItalicTrait, cast_uint(1 << 0))
        self.assertEqual(kCTFontBoldTrait, cast_uint(1 << 1))
        self.assertEqual(kCTFontExpandedTrait, cast_uint(1 << 5))
        self.assertEqual(kCTFontCondensedTrait, cast_uint(1 << 6))
        self.assertEqual(kCTFontMonoSpaceTrait, cast_uint(1 << 10))
        self.assertEqual(kCTFontVerticalTrait, cast_uint(1 << 11))
        self.assertEqual(kCTFontUIOptimizedTrait, cast_uint(1 << 12))

        self.assertEqual(kCTFontClassMaskTrait, cast_uint(15 << kCTFontClassMaskShift))

        self.assertEqual(kCTFontUnknownClass, cast_uint(0 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontOldStyleSerifsClass, cast_uint(1 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontTransitionalSerifsClass, (2 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontModernSerifsClass, cast_uint(3 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontClarendonSerifsClass, cast_uint(4 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontSlabSerifsClass, cast_uint(5 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontFreeformSerifsClass, cast_uint(7 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontSansSerifClass, cast_uint(8 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontOrnamentalsClass, cast_uint(9 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontScriptsClass, cast_uint(10 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontSymbolicClass, cast_uint(12 << kCTFontClassMaskShift))

if __name__ == "__main__":
    main()
