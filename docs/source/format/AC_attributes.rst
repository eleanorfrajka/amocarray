Global attributes
-------------------

The global attribute section is used for data discovery. The following global attributes should appear in the global section. The NetCDF Climate and Forecast (CF) Metadata Conventions are available from: http://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html#trajectory-data. It is recommended that extra global attributes follow ACDD convention".

See also https://oceangliderscommunity.github.io/OG-format-user-manual/OG_Format.html

* **title**: A short phrase or sentence describing the dataset.

  * *Requirement status*: mandatory
  * *ex.*: "RAPID 26N array data"

* **program**: The overarching program(s) of which the dataset is a part. A program consists of a set (or portfolio) of related and possibly interdependent projects that meet an overarching objective.

  * *Requirement status*: mandatory
  * *ex.*: "RAPID_MOCHA_WBTS" - note that no special characters should be used here as this will be included in the filenaming convention.

* **program_vocabulary**: A controlled vocabulary for the program attribute.

  * *Requirement status*: highly desirable
  * To be defined

* **id**: Formatted mission name: <program>_<end_date>_<release>

  * *Requirement status*: mandatory
  * *ex.*: "rapid_20210616T_v2023.1"

* **naming_authority**: A unique name that identifies the institution who provided the id.  ACDD-1.3 recommends using reverse-DNS naming.
  
  * *Requirement status*: highly desirable
  * *ex.*: "uk.ac.rapid"

* **institution**: The name of the institution where the original data was produced.

  * *Requirement status*: highly desirable
  * *ex.*: "National Oceanography Centre"

* **internal_dataset_identifier**: The mission identifier used by the institution principally responsible for originating this data

  * *Requirement status*: highly desirable
  * *ex.*: "moc_transport_profiles_200404_2012105_era.mat"

* **geospatial_lat_min**: Describes a simple lower latitude limit
  
  * *Requirement status*: suggested
  * *format*: decimal degree

* **geospatial_lat_max**: Describes a simple upper latitude limit
    
  * *Requirement status*: suggested
  * *format*: decimal degree

* **geospatial_lon_min**: Describes a simple lower longitude limit
      
  * *Requirement status*: suggested
  * *format*: decimal degree  

* **geospatial_lon_max**: Describes a simple upper longitude limit
        
  * *Requirement status*: suggested
  * *format*: decimal degree

* **geospatial_vertical_min**: Describes a simple lower vertical limit

  * *Requirement status*: suggested
  * *format*: meter (negative for sub-surface)

* **geospatial_vertical_max**: Describes a simple upper vertical limit

  * *Requirement status*: suggested
  * *format*: meter (negative for sub-surface)

* **time_coverage_start**: The time of the first data point in the dataset

  * *Requirement status*: highly desirable
  * *format*: Formatted string: YYYYmmddTHHMMss ex.: 20240425T145805

* **time_coverage_end**: The time of the last data point in the dataset

  * *Requirement status*: highly desirable
  * *format*: Formatted string: YYYYmmddTHHMMss ex.: 20240425T145805

* **project**: The name of the project(s) principally responsible for originating this data. Multiple projects are separated by commas.
  
    * *Requirement status*: suggested
    * *ex.*: "RAPID, MOCHA, WBTS"

* **contributor_name**: Name of the contributors to the data set. Multiple contributors are separated by commas.

  * *Requirement status*: suggested, PI name is mandatory
  * *ex.*: "John Smith, Jane Doe"

* **contributor_role**: The role of the contributors to the data set. Multiple roles are separated by commas.

  * *Requirement status*: suggested, PI role is mandatory
  * *ex.*: "Principal Investigator, Data Manager"

* **contributor_role_vocabulary**: Controlled vocabulary for the roles used in the "contributors_role". Multiple contributors’ roles and vocabularies are separated by commas.

  * *Requirement status*: PI vocabulary is mandatory
  * *ex.:* "http://vocab.nerc.ac.uk/search_nvs/W08/, http://vocab.nerc.ac.uk/search_nvs/W08/"

* **contributor_email**: Email address of the contributors to the data set. Multiple email addresses are separated by commas.

  * *Requirement status*: suggested, PI email is mandatory
  * *ex.*: "john.smith@web.com, jane.doe@web.com"

* **contributor_id**: Unique id of the contributors to the data set. Multiple contributors' ids are separated by commas.

  * *Requirement status*: highly desirable.
  * *ex.*: "0000-0001-5109-3700, 0000-0001-5109-3700"

* **contributing_institutions**: Names of the institutions that contributed to the data set. Multiple institutions are separated by commas.

  * *Requirement status*: suggested
  * *ex.*: "National Oceanography Centre, University of Miami"

* **contributing_institutions_vocabulary**: Controlled vocabulary for the institutions used in the "contributing_institutions". Multiple institutions and vocabularies are separated by commas.

  * *Requirement status*: highly desirable
  * *ex.*: "https://ror.org/00874hx02, https://ror.org/02dgjyy92"

* **uri**:  Other universal resource identifiers relevant to be linked to this dataset. Multiple uris are separated by a comma.

  * *Requirement status*: suggested
  * *ex.*: "https://www.rapid.ac.uk"

* **doi**: Digital Object Identifier for the AC1 format dataset. 

  * *Requirement status*: suggested
  * *ex.*: "10.17600/12345678"

* **original_doi**: Digital Object Identifier for the original dataset. Multiple original dois are separated by a comma.

  * *Requirement status*: highly desirable
  * *ex.*: "10.5285/223b34a3-2dc5-c945-e063-7086abc0f274"

* **reference**: A reference to a publication that describes the original data set. Multiple references are separated by a comma.

  * *Requirement status*: highly desirable
  * *ex.*: "Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2024). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2023 (v2023.1), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/223b34a3-2dc5-c945-e063-7086abc0f274"

* **web_link:** A link to a web page that provides more information about the dataset. Multiple web links are separated by a comma.

  * *Requirement status*: suggested
  * *ex.*: "https://www.rapid.ac.uk"

* **comment**: Miscellaneous information about the dataset or methods used to produced it.

  * *Requirement status*: suggested
  * *ex.*: "Data was collected during the RAPID-MOCHA-WBTS project"

* **date_created**: The date the dataset was created. 

  * *Requirement status*: mandatory
  * *format*: Formatted string: YYYYmmddTHHMMss ex.: 20240425T145805

* **Conventions**: A comma-separated list of the conventions that are followed by the dataset.

  * *Requirement status*: mandatory
  * *ex.*: "CF-1.8, ACDD-1.3, AC-0.1"