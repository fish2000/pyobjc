"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    name="PyABPresence",
    app=["main.py"],
    data_files=["English.lproj"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-InstantMessage",
    ]

)
