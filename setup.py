"""
Setup script for amocarray (DEPRECATED)

This package has been renamed to AMOCatlas.
Please use 'pip install amocatlas' instead.
"""

from setuptools import setup, find_packages
import warnings

# Issue deprecation warning during installation
warnings.warn(
    "amocarray is deprecated and has been renamed to AMOCatlas. "
    "Please install AMOCatlas instead: pip install amocatlas",
    DeprecationWarning
)

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="amocarray",
    version="0.1.0",
    author="Eleanor Frajka-Williams",
    author_email="eleanor.frajka@noc.ac.uk",
    description="DEPRECATED: This package has been renamed to AMOCatlas",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/eleanorfrajka/amocarray",
    project_urls={
        "New Package": "https://github.com/eleanorfrajka/AMOCatlas",
        "Bug Tracker": "https://github.com/eleanorfrajka/amocarray/issues",
    },
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "migrate": ["amocatlas"],
    },
)