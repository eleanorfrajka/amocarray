.. Documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:parser: myst_parser.sphinx_ # this is the markdown parser

Welcome to AMOCarray's documentation!
======================================

AMOCarray is a repository to read in data from various AMOC observing arrays, and transform the data into a more unified format.

For recommendations or bug reports, please visit https://github.com/eleanorfrajka/amocarray/issues/new

AC0.1 format manual
====================

**Objectives**: This document defines the common AMOC array data format, hereafter AC0.1.


AC0.1 General conventions
-------------------------
.. toctree::
   :maxdepth: 3

   format/AC_general_conventions
   format/AC_attributes
..   format/File_naming_convention
   format/Dimension_definition
   format/Location_variables
   format/Array_name
   format/Geophysical_variables
   format/Evolution_process

AMOCarray's API
------------------
.. toctree::
   :maxdepth: 3

   demo-output.ipynb
   amocarray

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
