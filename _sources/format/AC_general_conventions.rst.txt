General conventions
-------------------

* The required granularity of the data set is the project, starting from the first deployment at sea to the most recently recovered and processed dataset.
* Data are recorded as a ??? trajectory Discrete Geometry, using NetCDFfootnote:[NetCDF-3 does not satisfy the requirements of OG1.0 format] system and following CF 1.10footnote:[http://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html] (Climate and Forecast) specifications. Each data file contains a depth (or pressure) coordinate and a time coordinate.  It can be produced in near real-time and revised, or in a delayed-mode (after rigorous QC) with a specified version number.
* Format follows the ACDD 1.3footnote:[https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3] convention where possible.
* Vocabulary collections will be hosted somewhere (see e.g., NERC Vocabulary Server - NVS, OceanOPS, ICES, etc). The AMOC Task Team data management team will manage (additions, updates, etc.) the collections. Treatment of vocabularies is detailed in the https://oceangliderscommunity.github.io/OG-format-user-manual/vocabularyCollection/tableOfControlledVocab.html[vocabularies document].
* AC0.1 defines some variables and definitions, as described in this document. Other types of measurements (e.g. intermediate parameters, technical measurements, other variables) not framed by AC0.1 can be included in AC0.1 data files. No control will be applied to those measurements.
* Geospatial variables are mandatory.
* Methodologies used to interpolate data, compute along-track positioning variables, apply QC etc. ahould be linked and, where possible, follow community best practices. It is encouraged to use unique resource identifiers (uris) to link to these resources.
* 3 recommendations level have been defined for AC0.1:

  - Mandatory: Minimum metadata set to be compliant with AC0.1 requirement.
  - Highly desirable: Worth having for complete use of the data set.
  - Suggested: If the information is available.


DOI management
--------------

A DOI can be minted at any level (PI, Reference Data Center, Data Assembly Center, Global Data Assembly Center) following the internal policy of data curation.

A DOI can be minted for a single deployment or multiple deployments (i.e. project, array).

A DOI if included in AC0.1 files needs to be preserved. The DOI must remain unchanged if there is no valuable modification. If valuable information is aggregated/added or a new product produced, a new DOI should be created and the new DOI should link to the original DOI to acknowledge as the source.

The most effective way of preserving the integrity of the source citation is to preserve the initial DOI added in the AC0.1 file.

AC0.1 file naming convention
----------------------------

Data files should be named as follows:

"<id>.nc" (ex : "rapid_20210616T_v2023.1.nc")

Where <id> = "<project>_<end_date>_<release>" (ex : "rapid_20210616T_v2023.1")

In this case:

<project> = "rapid" (the RAPID 26°N array)

<end_date> = "20210616T" The datetime in days precision 2021-06-16 formatted following ISO 8601

<version> = "v2023.1" for the project originator's version number
