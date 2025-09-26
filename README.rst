DEPRECATED: amocarray → AMOCatlas
================================

.. warning::
   **This package has been DEPRECATED.**
   
   The ``amocarray`` package has been renamed to ``AMOCatlas`` and moved to:
   https://github.com/AMOCcommunity/AMOCatlas

Quick Migration
---------------

**Uninstall the old package and install the new one:**

.. code-block:: bash

   pip uninstall amocarray
   pip install AMOCatlas

**Update your import statements:**

.. code-block:: python

   # Old (deprecated)
   import amocarray
   
   # New
   import AMOCatlas

Why the Change?
---------------

The package has been renamed to better reflect its purpose and has moved to 
the AMOCcommunity organization for better community maintenance.

All development now happens at: https://github.com/AMOCcommunity/AMOCatlas

Installation of Deprecated Package
-----------------------------------

If you install this deprecated package, it will automatically install 
``AMOCatlas`` as a dependency and show deprecation warnings to guide you 
through the migration.

Support
-------

For issues or questions, please use the new repository:
https://github.com/AMOCcommunity/AMOCatlas/issues