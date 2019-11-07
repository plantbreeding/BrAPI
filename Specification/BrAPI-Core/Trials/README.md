
# Group Trials

Services related to trials. Trials comprise of multiple studies. The trial concept in BrAPI corresponds to the "investigation" concept in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).




## Trials [/brapi/v1/trials] 




### Get Trials  [GET /brapi/v1/trials{?commonCropName}{?programDbId}{?locationDbId}{?active}{?sortBy}{?sortOrder}{?page}{?pageSize}]

Retrieve a filtered list of breeding Trials. A Trial is a collection of Studies



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string||
|publicReleaseDate|string (date)||
|submissionDate|string (date)||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]||
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialDescription|string|The human readable description of a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + commonCropName (Optional, ) ... Common name for the crop associated with this trial
    + programDbId (Optional, ) ... Program filter to only return trials associated with given program id.
    + locationDbId (Optional, ) ... Filter by location
    + active (Optional, ) ... Filter active status true/false.
    + sortBy (Optional, ) ... Sort order. Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction: asc/desc
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Wheat",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Post Trials  [POST /brapi/v1/trials]

Create new breeding Trials. A Trial represents a collection of related Studies. `trialDbId` is generated by the server.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string||
|publicReleaseDate|string (date)||
|submissionDate|string (date)||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]||
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDescription|string|The human readable description of a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string||
|publicReleaseDate|string (date)||
|submissionDate|string (date)||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]||
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialDescription|string|The human readable description of a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Wheat",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "datasetAuthorships": [
            {
                "datasetPUI": "doi:10.15454/312953986E3",
                "license": "https://CreativeCommons.org/licenses/by/4.0",
                "publicReleaseDate": "2018-01-01",
                "submissionDate": "2018-01-01"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "programDbId": "673f378a",
        "programName": "Tomatillo_Breeding_Program",
        "publications": [
            {
                "publicationPUI": "doi:10.15454/312953986E3",
                "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
            }
        ],
        "startDate": "2018-01-01",
        "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
        "trialName": "Peru Yield Trial 1"
    }
]
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Wheat",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Trials by trialDbId  [GET /brapi/v1/trials/{trialDbId}]

Get the details of a specific Trial



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|culturalPractices|string|General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|location|object||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|altitude|number|The altitude/elevation of this location (in meters)|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|instituteName|string|each institute/laboratory can have several experimental field|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyDescription|string|The description of this study|
|studyName|string|The human readable name for a study|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + trialDbId (Required, ) ... The internal trialDbId
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataLinkName": "image-archive.zip",
                "type": "Image Archive",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.0"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "location": {
            "abbreviation": "L1",
            "additionalInfo": {},
            "altitude": 35.6,
            "coordinateDescription": "North East corner of greenhouse",
            "coordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "countryCode": "PER",
            "countryName": "Peru",
            "documentationURL": "https://brapi.org",
            "environmentType": "Nursery",
            "exposure": "Structure, no exposure",
            "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
            "instituteName": "Plant Science Institute",
            "locationDbId": "3cfdd67d",
            "locationName": "Location 1",
            "locationType": "Storage Location",
            "siteStatus": "Private",
            "slope": "0",
            "topography": "Valley"
        },
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01",
        "studyDbId": "175ac75a",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "Grape_Yield_Spring_2018",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Put Trials by trialDbId  [PUT /brapi/v1/trials/{trialDbId}]

Update the details of an existing Trial

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string||
|publicReleaseDate|string (date)||
|submissionDate|string (date)||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]||
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDescription|string|The human readable description of a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|culturalPractices|string|General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|location|object||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|altitude|number|The altitude/elevation of this location (in meters)|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|instituteName|string|each institute/laboratory can have several experimental field|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyDescription|string|The description of this study|
|studyName|string|The human readable name for a study|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + trialDbId (Required, ) ... The internal trialDbId
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
    "additionalInfo": {},
    "commonCropName": "Wheat",
    "contacts": [
        {
            "contactDbId": "5f4e5509",
            "email": "bob@bob.com",
            "instituteName": "The BrAPI Institute",
            "name": "Bob Robertson",
            "orcid": "http://orcid.org/0000-0001-8640-1750",
            "type": "PI"
        }
    ],
    "datasetAuthorships": [
        {
            "datasetPUI": "doi:10.15454/312953986E3",
            "license": "https://CreativeCommons.org/licenses/by/4.0",
            "publicReleaseDate": "2018-01-01",
            "submissionDate": "2018-01-01"
        }
    ],
    "documentationURL": "https://wiki.brapi.org",
    "endDate": "2018-01-01",
    "programDbId": "673f378a",
    "programName": "Tomatillo_Breeding_Program",
    "publications": [
        {
            "publicationPUI": "doi:10.15454/312953986E3",
            "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
        }
    ],
    "startDate": "2018-01-01",
    "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
    "trialName": "Peru Yield Trial 1"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataLinkName": "image-archive.zip",
                "type": "Image Archive",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.0"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "location": {
            "abbreviation": "L1",
            "additionalInfo": {},
            "altitude": 35.6,
            "coordinateDescription": "North East corner of greenhouse",
            "coordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "countryCode": "PER",
            "countryName": "Peru",
            "documentationURL": "https://brapi.org",
            "environmentType": "Nursery",
            "exposure": "Structure, no exposure",
            "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
            "instituteName": "Plant Science Institute",
            "locationDbId": "3cfdd67d",
            "locationName": "Location 1",
            "locationType": "Storage Location",
            "siteStatus": "Private",
            "slope": "0",
            "topography": "Valley"
        },
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01",
        "studyDbId": "175ac75a",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "Grape_Yield_Spring_2018",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Trials  [POST /brapi/v1/search/trials]

Advanced searching for the programs resource.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|commonCropNames|array[string]|Common name for the crop associated with this trial|
|contactDbIds|array[string]|List of contact entities associated with this trial|
|programDbIds|array[string]|A program identifier to search for|
|searchDateRangeEnd|string (date)|The end of the overlapping search date range|
|searchDateRangeStart|string (date)|The start of the overlapping search date range|
|studyDbIds|array[string]|The ID which uniquely identifies a study|
|trialDbIds|array[string]|The ID which uniquely identifies a trial|
|trialNames|array[string]|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "contactDbIds": [
        "e0f70c2a",
        "b82f0967"
    ],
    "programDbIds": [
        "7e54bd46",
        "e54a7703"
    ],
    "searchDateRangeEnd": "2018-01-01",
    "searchDateRangeStart": "2018-01-01",
    "studyDbIds": [
        "e4fbcc24",
        "6ca07754"
    ],
    "trialDbIds": [
        "d2593dc2",
        "9431a731"
    ],
    "trialNames": [
        "All Yield Trials 2016",
        "Disease Resistance Study Comparison Group"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Search Trials by searchResultsDbId  [GET /brapi/v1/search/trials/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the trials resource.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string||
|publicReleaseDate|string (date)||
|submissionDate|string (date)||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]||
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialDescription|string|The human readable description of a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Wheat",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

