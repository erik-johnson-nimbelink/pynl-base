"""
Setup for the NimbeLink package

(C) NimbeLink Corp. 2020

All rights reserved except as explicitly granted in the license agreement
between NimbeLink Corp. and the designated licensee. No other use or disclosure
of this software is permitted. Portions of this software may be subject to third
party license terms as specified in this software, and such portions are
excluded from the preceding copyright notice of NimbeLink Corp.
"""

from distutils.core import setup
from setuptools import find_packages

setup(
    name = "pynl-base",
    description = "NimbeLink library base",
    version = "1.0.1",
    packages = find_packages(),
    entry_points = {
        "console_scripts":
            ["nimbelink=nimbelink.__main__:main"]
    },
    install_requires = [
        "diskcache",
        "pynrfjprog",
        "pyserial>=3.4",
        "PyYAML>=5.3",
        "requests",
    ]
)
