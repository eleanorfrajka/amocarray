"""
amocarray - DEPRECATED

This package has been renamed to AMOCatlas.
Please use 'pip install amocatlas' and update your imports.

For more information, visit: https://github.com/eleanorfrajka/AMOCatlas
"""

import warnings

__version__ = "0.1.0"
__author__ = "Eleanor Frajka-Williams"
__email__ = "eleanor.frajka@noc.ac.uk"

# Issue deprecation warning when the package is imported
warnings.warn(
    "amocarray is deprecated and has been renamed to AMOCatlas. "
    "Please install AMOCatlas instead: pip install amocatlas. "
    "Update your imports from 'import amocarray' to 'import amocatlas'. "
    "See https://github.com/eleanorfrajka/AMOCatlas for more information.",
    DeprecationWarning,
    stacklevel=2
)

# Make sure the warning is always shown
warnings.filterwarnings("always", category=DeprecationWarning, module="amocarray")