"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(CFBundleName='FieldGraph')
setup(
    app=["Main.py"],
    data_files=["English.lproj", 'CrossCursor.tiff', 'Map.png'],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
