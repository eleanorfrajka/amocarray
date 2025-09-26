"""
DEPRECATED: amocarray has been renamed to AMOCatlas.

This package is deprecated. Please install AMOCatlas instead:
    pip install AMOCatlas

All functionality has been moved to the new package.
"""
import warnings

warnings.warn(
    "The 'amocarray' package has been deprecated and renamed to 'AMOCatlas'. "
    "Please update your code to use 'import AMOCatlas' instead. "
    "Install the new package with: pip install AMOCatlas",
    DeprecationWarning,
    stacklevel=2
)

# Optional: Re-export everything from the new package for backward compatibility
try:
    from AMOCatlas import *
    __version__ = "deprecated"
except ImportError:
    raise ImportError(
        "AMOCatlas is not installed. This deprecated package requires AMOCatlas. "
        "Please install it with: pip install AMOCatlas"
    )