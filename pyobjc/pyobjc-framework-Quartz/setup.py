''' 
Wrappers for the "Quartz" related frameworks on MacOSX. These frameworks
provide a number of graphics related API's.

The frameworks wrapped by this package are:

   * CoreGraphics - 2D Graphics, based on the PDF model

   * ImageIO - Reading and writing images

   * QuartzComposer - Working with "Quartz Composer" compositions

   * QuartzCore  - Image processing and video image manipulation

   * QuarzFilters - Image effects

   * ImageKit - iPhoto-like views

   * PDFKit - Working with PDF files

   * CoreVideo - Managing digital video

All frameworks can be accessed by importing the 'Quartz' module.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: The actual wrappers are subpackages of ``Quartz``, they are not toplevel
packages to avoid name clashes with Apple provided wrappers for CoreGraphics.

WARNING: Running the unittests will change your display settings during the
testrun, which will probably mess up your window layout.
'''

from pyobjc_setup import setup, Extension

import os

setup(
    name='pyobjc-framework-Quartz',
    version='2.2',
    description = "Wrappers for the Quartz frameworks on Mac OS X",
    packages = [ "Quartz", "Quartz.CoreGraphics", "Quartz.ImageIO", "Quartz.QuartzCore", "Quartz.CoreVideo", "Quartz.QuartzComposer", "Quartz.ImageKit", "Quartz.PDFKit", "Quartz.QuartzFilters" ],
    install_requires = [ 
        'pyobjc-core>=2.2',
        'pyobjc-framework-Cocoa>=2.2',
    ],
    ext_modules = [
        # CoreVideo
        Extension('Quartz.CoreVideo._CVPixelBuffer',
            [ 'Modules/_CVPixelBuffer.m' ]),

        # CoreGraphics
        Extension('Quartz.CoreGraphics._inlines',
            [ 'Modules/_CoreGraphics_inlines.m' ]),
        Extension('Quartz.CoreGraphics._callbacks',
            [ 'Modules/_callbacks.m' ]),
        Extension('Quartz.CoreGraphics._doubleindirect',
            [ 'Modules/_doubleindirect.m' ]),
        Extension('Quartz.CoreGraphics._sortandmap',
            [ 'Modules/_sortandmap.m' ]),
        Extension('Quartz.CoreGraphics._coregraphics',
            [ 'Modules/_coregraphics.m' ]),
    ],
)
