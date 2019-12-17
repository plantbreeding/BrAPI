FORMAT: 1A

# BrAPI Phenotyping

The Breeding API (BrAPI) is a Standardized REST ful Web Service API Specification for communicating Plant Breeding Data. BrAPI allows for easy data sharing between databases and tools involved in plant breeding.

### General Reference Documentation
- [URL Structure](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/URL_Structure.md)
- [Response Structure](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Response_Structure.md)
- [Date/Time Encoding](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Date_Time_Encoding.md)
- [Location Encoding](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Location_Encoding.md)
- [Error Handling](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Error_Handling.md)
- [Search Services](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Search_Services.md)



### BrAPI Core
The BrAPI Core module contains high level entities used for organization and management. This includes Programs, Trials, Studies, Locations, People, and Lists

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Core) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Core) - [Apiary](https://brapicore.docs.apiary.io)


### **BrAPI Phenotyping**
The **BrAPI Phenotyping** module contains entities related to phenotypic observations. This includes Observation Units, Observations, Observation Variables, Traits, Scales, Methods, and Images

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Phenotyping) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Phenotyping) - [Apiary](https://brapiphenotyping.docs.apiary.io)


### BrAPI Genotyping
The BrAPI Genotyping module contains entities related to genotyping analysis. This includes Samples, Markers, Variant Sets, Variants, Call Sets, Calls, References, Reads, and Vendor Orders

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Genotyping) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Genotyping) - [Apiary](https://brapigenotyping.docs.apiary.io)


### BrAPI Germplasm
The BrAPI Germplasm module contains entities related to germplasm management. This includes Germplasm, Germplasm Attributes, Seed Lots, Crosses, Pedigree, and Progeny

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Germplasm) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Germplasm) - [Apiary](https://brapigermplasm.docs.apiary.io)


# Group Events

An event is discrete occurrence at a particular time in the experiment (which can be natural, such as rain, or unnatural, such as planting, watering, etc). Events may be the realization of Treatments or parts of Treatments, or may be confounding to Treatments. Can be applied at the whole study level or to only a subset of observation units.  
[also see the [MIAPPE](https://www.miappe.org/) definition]




### Get - /events [GET /brapi/v1/events{?studyDbId}{?observationUnitDbId}{?eventType}{?dateRangeStart}{?dateRangeEnd}{?page}{?pageSize}]

Get list of events



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|date|array[string]|A list of dates when the event occured  MIAPPE V1.1 (DM-68) Event date - Date and time of the event.|
|eventDbId|string|Internal database identifier|
|eventDescription|string|A detailed, human-readable description of this event  MIAPPE V1.1 (DM-67) Event description - Description of the event, including details such as amount applied and possibly duration of the event. |
|eventParameters|array[object]|A list of objects describing additional event parameters. Each of the following accepts a human-readable value or URI|
|key|string|Specifies the relationship between the event and the given property. E.g. fertilizer, operator|
|rdfValue|string|The type of the value given above, e.g. http://xmlns.com/foaf/0.1/Agent|
|value|string|The value of the property for this event. E.g. nitrogen, John Doe|
|eventType|string|General category for this event (e.g. Sowing, Watering, Rain). Each eventType should correspond to exactly one eventTypeDbId, if provided.  MIAPPE V1.1 (DM-65) Event type - Short name of the event.|
|eventTypeDbId|string|An identifier for this event type, in the form of an ontology class reference  MIAPPE V1.1 (DM-66) Event accession number - Accession number of the event type in a suitable controlled vocabulary (Crop Ontology).|
|observationUnitDbIds|array[string]|A list of the affected observation units. If this parameter is not given, it is understood that the event affected all units in the study|
|studyDbId|string|The study in which the event occurred|


 

+ Parameters
    + studyDbId (Optional, ) ... Filter based on study unique identifier in which the events occured
    + observationUnitDbId (Optional, ) ... Filter based on an ObservationUnit unique identifier in which the events occured
    + eventType (Optional, ) ... Filter based on an Event Type
    + dateRangeStart (Optional, ) ... Filter based on an Date Range
    + dateRangeEnd (Optional, ) ... Filter based on an Date Range
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "date": [
                    "2018-10-08T18:15:11Z",
                    "2018-11-09T18:16:12Z"
                ],
                "eventDbId": "8566d4cb",
                "eventDescription": "A set of plots was watered",
                "eventParameters": [
                    {
                        "key": "http://www.example.fr/vocabulary/2018#hasContact,",
                        "value": "http://www.example.fr/id/agent/marie,",
                        "valueRdfType": "http://xmlns.com/foaf/0.1/Agent,"
                    },
                    {
                        "key": "fertilizer",
                        "value": "nitrogen",
                        "valueRdfType": null
                    }
                ],
                "eventType": "Watering",
                "eventTypeDbId": "4e7d691e",
                "observationUnitDbIds": [
                    "8439eaff",
                    "d7682e7a",
                    "305ae51c"
                ],
                "studyDbId": "2cc2001f"
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

# Group Images

Calls for manipulating images

Implementation Notes:

The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 




### Get - /images [GET /brapi/v1/images{?imageDbId}{?imageName}{?observationUnitDbId}{?observationDbId}{?descriptiveOntologyTerm}{?page}{?pageSize}]

Get filtered set of image meta data

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + imageDbId (Optional, ) ... The unique identifier for a image
    + imageName (Optional, ) ... The human readable name of an image
    + observationUnitDbId (Optional, ) ... The unique identifier of the observation unit an image is portraying
    + observationDbId (Optional, ) ... The unique identifier of the observation an image is associated with
    + descriptiveOntologyTerm (Optional, ) ... A descriptive term associated with an image
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "copyright": "Copyright 2018 Bob Robertson",
                "description": "This is a picture of a tomato",
                "descriptiveOntologyTerms": [
                    "doi:10.1002/0470841559",
                    "Red",
                    "ncbi:0300294"
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "imageName": "Tomato Image 1",
                "imageTimeStamp": "2018-01-01T14:47:23-0600",
                "imageURL": "https://wiki.brapi.org/images/tomato",
                "imageWidth": 700,
                "mimeType": "image/jpeg",
                "observationDbIds": [
                    "d05dd235",
                    "8875177d",
                    "c08e81b6"
                ],
                "observationUnitDbId": "b7e690b6"
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




### Post - /images [POST /brapi/v1/images]

Create a new image meta data object

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.

- The '/images' calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons.

- With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera.

- For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. '

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "copyright": "Copyright 2018 Bob Robertson",
        "description": "This is a picture of a tomato",
        "descriptiveOntologyTerms": [
            "doi:10.1002/0470841559",
            "Red",
            "ncbi:0300294"
        ],
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "imageName": "Tomato Image 1",
        "imageTimeStamp": "2018-01-01T14:47:23-0600",
        "imageURL": "https://wiki.brapi.org/images/tomato",
        "imageWidth": 700,
        "mimeType": "image/jpeg",
        "observationDbIds": [
            "d05dd235",
            "8875177d",
            "c08e81b6"
        ],
        "observationUnitDbId": "b7e690b6"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "copyright": "Copyright 2018 Bob Robertson",
                "description": "This is a picture of a tomato",
                "descriptiveOntologyTerms": [
                    "doi:10.1002/0470841559",
                    "Red",
                    "ncbi:0300294"
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "imageName": "Tomato Image 1",
                "imageTimeStamp": "2018-01-01T14:47:23-0600",
                "imageURL": "https://wiki.brapi.org/images/tomato",
                "imageWidth": 700,
                "mimeType": "image/jpeg",
                "observationDbIds": [
                    "d05dd235",
                    "8875177d",
                    "c08e81b6"
                ],
                "observationUnitDbId": "b7e690b6"
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




### Get - /images/{imageDbId} [GET /brapi/v1/images/{imageDbId}]

Get one image meta data object

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "copyright": "Copyright 2018 Bob Robertson",
        "description": "This is a picture of a tomato",
        "descriptiveOntologyTerms": [
            "doi:10.1002/0470841559",
            "Red",
            "ncbi:0300294"
        ],
        "imageDbId": "a55efb9c",
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "imageName": "Tomato Image 1",
        "imageTimeStamp": "2018-01-01T14:47:23-0600",
        "imageURL": "https://wiki.brapi.org/images/tomato",
        "imageWidth": 700,
        "mimeType": "image/jpeg",
        "observationDbIds": [
            "d05dd235",
            "8875177d",
            "c08e81b6"
        ],
        "observationUnitDbId": "b7e690b6"
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




### Put - /images/{imageDbId} [PUT /brapi/v1/images/{imageDbId}]

Update an image meta data object

Implementation Notes

- This call should be paired with 'PUT /images/{imageDbId}/imagecontent' for full capability

- A server may choose to modify the image meta data object based on the actually image which has been uploaded. 

- Image data may be stored in a database or file system. Servers should generate and provide the "imageURL" as an absolute path for retrieving the image, wherever it happens to live. 

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's. 

- The '/images' calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 

- With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 

- For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "copyright": "Copyright 2018 Bob Robertson",
    "description": "This is a picture of a tomato",
    "descriptiveOntologyTerms": [
        "doi:10.1002/0470841559",
        "Red",
        "ncbi:0300294"
    ],
    "imageFileName": "image_0000231.jpg",
    "imageFileSize": 50000,
    "imageHeight": 550,
    "imageLocation": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373
            ],
            "type": "Point"
        },
        "type": "Feature"
    },
    "imageName": "Tomato Image 1",
    "imageTimeStamp": "2018-01-01T14:47:23-0600",
    "imageURL": "https://wiki.brapi.org/images/tomato",
    "imageWidth": 700,
    "mimeType": "image/jpeg",
    "observationDbIds": [
        "d05dd235",
        "8875177d",
        "c08e81b6"
    ],
    "observationUnitDbId": "b7e690b6"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "copyright": "Copyright 2018 Bob Robertson",
        "description": "This is a picture of a tomato",
        "descriptiveOntologyTerms": [
            "doi:10.1002/0470841559",
            "Red",
            "ncbi:0300294"
        ],
        "imageDbId": "a55efb9c",
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "imageName": "Tomato Image 1",
        "imageTimeStamp": "2018-01-01T14:47:23-0600",
        "imageURL": "https://wiki.brapi.org/images/tomato",
        "imageWidth": 700,
        "mimeType": "image/jpeg",
        "observationDbIds": [
            "d05dd235",
            "8875177d",
            "c08e81b6"
        ],
        "observationUnitDbId": "b7e690b6"
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




### Put - /images/{imageDbId}/imagecontent [PUT /brapi/v1/images/{imageDbId}/imagecontent]

Update an image with the image file content

Implementation Notes

- This call should be paired with 'PUT /images/{imageDbId}' for full capability

- A server may choose to modify the image meta data object based on the actually image which has been uploaded. 

- Image data may be stored in a database or file system. Servers should generate and provide the "imageURL" for retrieving the image, wherever it happens to live.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "copyright": "Copyright 2018 Bob Robertson",
        "description": "This is a picture of a tomato",
        "descriptiveOntologyTerms": [
            "doi:10.1002/0470841559",
            "Red",
            "ncbi:0300294"
        ],
        "imageDbId": "a55efb9c",
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "imageName": "Tomato Image 1",
        "imageTimeStamp": "2018-01-01T14:47:23-0600",
        "imageURL": "https://wiki.brapi.org/images/tomato",
        "imageWidth": 700,
        "mimeType": "image/jpeg",
        "observationDbIds": [
            "d05dd235",
            "8875177d",
            "c08e81b6"
        ],
        "observationUnitDbId": "b7e690b6"
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




### Post - /search/images [POST /brapi/v1/search/images]

Get filtered set of image meta data

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image to search for. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileNames|array[string]|Image file names to search for.|
|imageFileSizeMax|integer|A maximum image file size to search for.|
|imageFileSizeMin|integer|A minimum image file size to search for.|
|imageHeightMax|integer|A maximum image height to search for.|
|imageHeightMin|integer|A minimum image height to search for.|
|imageLocation|object||
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageNames|array[string]|Human readable names to search for.|
|imageTimeStampRangeEnd|string (date-time)|The latest timestamp to search for.|
|imageTimeStampRangeStart|string (date-time)|The earliest timestamp to search for.|
|imageWidthMax|integer|A maximum image width to search for.|
|imageWidthMin|integer|A minimum image width to search for.|
|mimeTypes|array[string]|A set of image file types to search for.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with to search for|
|observationUnitDbIds|array[string]|A set of observation unit identifiers to search for.|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "descriptiveOntologyTerms": [
        "doi:10.1002/0470841559",
        "Red",
        "ncbi:0300294"
    ],
    "imageFileNames": [
        "image_01032019.jpg",
        "picture_field_1234.jpg"
    ],
    "imageFileSizeMax": 20000000,
    "imageFileSizeMin": 1000,
    "imageHeightMax": 1080,
    "imageHeightMin": 720,
    "imageLocation": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373
            ],
            "type": "Point"
        },
        "type": "Feature"
    },
    "imageNames": [
        "Image 43",
        "Tractor in field"
    ],
    "imageTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "imageTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "imageWidthMax": 1920,
    "imageWidthMin": 1280,
    "mimeTypes": [
        "image/jpg",
        "image/jpeg",
        "image/gif"
    ],
    "observationDbIds": [
        "47326456",
        "fc9823ac"
    ],
    "observationUnitDbIds": [
        "f5e4b273",
        "328c9424"
    ],
    "page": 0,
    "pageSize": 1000
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "copyright": "Copyright 2018 Bob Robertson",
                "description": "This is a picture of a tomato",
                "descriptiveOntologyTerms": [
                    "doi:10.1002/0470841559",
                    "Red",
                    "ncbi:0300294"
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "imageName": "Tomato Image 1",
                "imageTimeStamp": "2018-01-01T14:47:23-0600",
                "imageURL": "https://wiki.brapi.org/images/tomato",
                "imageWidth": 700,
                "mimeType": "image/jpeg",
                "observationDbIds": [
                    "d05dd235",
                    "8875177d",
                    "c08e81b6"
                ],
                "observationUnitDbId": "b7e690b6"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/images/{searchResultsDbId} [GET /brapi/v1/search/images/{searchResultsDbId}{?page}{?pageSize}]

Get filtered set of image meta data

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|imageTimeStamp|string (date-time)|The date and time the image was taken|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|imageWidth|integer|The width of the image in Pixels.|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 102 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "copyright": "Copyright 2018 Bob Robertson",
                "description": "This is a picture of a tomato",
                "descriptiveOntologyTerms": [
                    "doi:10.1002/0470841559",
                    "Red",
                    "ncbi:0300294"
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "imageName": "Tomato Image 1",
                "imageTimeStamp": "2018-01-01T14:47:23-0600",
                "imageURL": "https://wiki.brapi.org/images/tomato",
                "imageWidth": 700,
                "mimeType": "image/jpeg",
                "observationDbIds": [
                    "d05dd235",
                    "8875177d",
                    "c08e81b6"
                ],
                "observationUnitDbId": "b7e690b6"
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


# Group Methods

API to manage the details of observation variable Methods. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Method describes the way an observation should be collected. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Method "estimation" or "drone image processing". 






### Get - /methods [GET /brapi/v1/methods{?page}{?pageSize}]

Returns a list of Methods available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "description": "A measuring tape was used",
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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




### Post - /methods [POST /brapi/v1/methods]

Create a new method object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "description": "A measuring tape was used",
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "description": "A measuring tape was used",
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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




### Get - /methods/{methodDbId} [GET /brapi/v1/methods/{methodDbId}]

Retrieve details about a specific method

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "description": "A measuring tape was used",
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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




### Put - /methods/{methodDbId} [PUT /brapi/v1/methods/{methodDbId}]

Update the details of an existing method

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "description": "A measuring tape was used",
    "formula": "a^2 + b^2 = c^2",
    "methodClass": "Measurement",
    "methodName": "Measuring Tape",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": [
                    "OBO",
                    "RDF",
                    "WEBPAGE"
                ]
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
    },
    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "description": "A measuring tape was used",
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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


# Group Observation Units

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.





### Get - /observationlevels [GET /brapi/v1/observationlevels{?page}{?pageSize}]

Call to retrieve the list of supported observation levels. 

Observation levels indicate the granularity level at which the measurements are taken. 

The values are used to supply the `observationLevel` parameter in the observation unit details call.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]||


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
            "field",
            "plot",
            "plant"
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




### Get - /observationunits [GET /brapi/v1/observationunits{?germplasmDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?page}{?pageSize}]

Get a filtered set of Observation Units



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA_179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:4d45d11c",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Post - /observationunits [POST /brapi/v1/observationunits]

Add new Observation Units

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationLevel": "plot",
        "observationUnitName": "Plot 1",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "blockNumber": "6",
            "entryNumber": "3",
            "entryType": [
                "CHECK",
                "TEST",
                "FILLER"
            ],
            "geoCoordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW",
            "replicate": "1"
        },
        "observationUnitXref": [
            {
                "id": "SAMEA_179865230",
                "source": "ebi.biosample"
            },
            {
                "id": "INRA:4d45d11c",
                "source": "gnpis.lot"
            }
        ],
        "plantNumber": "1",
        "plotNumber": "01",
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA_179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:4d45d11c",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Put - /observationunits [PUT /brapi/v1/observationunits]

Update a set of Observation Units

Note - In strictly typed languages, this structure can be represented as a Map or Dictionary of objects and parsed directly to JSON.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA_179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:4d45d11c",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Get - /observationunits/table [GET /brapi/v1/observationunits/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}]

<p>This service is designed to retrieve a table for observation values as a matrix of Observation Units and Observation Variables.</p>
<p>The table may be represented by JSON, CSV, or TSV. The "Accept" HTTP header is used for the client to request different return formats. 
By default, if the "Accept" header is not included in the request, the server should return JSON as described below.</p>
<p>The table is REQUIRED to have the following columns</p>
<ul>
  <li>observationUnitDbId - Each row is related to one Observation Unit</li>
  <li>At least one column with an observationVariableDbId</li>
</ul>
<p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p>
<ul>
  <li>observationUnitName</li>
  <li>studyDbId</li>
  <li>studyName</li>
  <li>germplasmDbId</li>
  <li>germplasmName</li>
  <li>plotNumber</li>
  <li>plantNumber</li>
  <li>blockNumber</li>
  <li>entryNumber</li>
  <li>replicate</li>
  <li>positionCoordinateX</li>
  <li>positionCoordinateY</li>
  <li>year</li>
</ul>
<p>The JSON representation provides a pair of extra arrays for defining the headers of the table. 
The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names. 
The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table. 
By appending the two arrays, you can construct the complete header row of the table. </p>
<p>For CSV and TSV representations of the table, an extra header row is needed to describe both the Observation Variable DbId and the Observation Variable Name for each data column. 
See the example responses below</p> 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|headerRow|array[string]|The header row describing observation unit fields. Append "observationVariableDbIds" for complete header row of the table.  This array should contain any or all of the following strings; year, studyDbId, studyName, locationDbId, locationName, germplasmDbId, germplasmName, observationUnitDbId, plotNumber, replicate, blockNumber, entryType, X, Y|
|observationVariableDbIds|array[string]|The list of observation variables which have values recorded for them in the data matrix. Append to the "headerRow" for complete header row.|
|observationVariableNames|array[string]|The list of observation variable names which have values recorded for them in the data matrix. Order should match "observationVariableDbIds".|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/csv)
```
"\"observationTimeStamp\",\"studyDbId\",\"studyName\",\"germplasmDbId\",\"germplasmName\",\"observationUnitDbId\",\"observationUnitName\",\"plotNumber\",\"plantNumber\",\"blockNumber\",\"entryNumber\",\"replicate\",\"positionCoordinateX\",\"positionCoordinateY\",\"2d599b04\",\"a0e84c5c\",\"35c5670a\",\"0144dea8\"\n\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"Plant height\",\"Carotenoid\",\"Root color\",\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"1.1\", \"\",    \"\", \"\"\n\"2019-09-10T18:14:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"1.9\", \"\",    \"\", \"\"\n\"2019-09-10T18:15:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"1.4\", \"\",    \"\", \"\"\n\"2019-09-10T18:16:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"1.5\", \"\",    \"\", \"\"\n\"2019-09-10T18:17:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"\",    \"2.6\", \"\", \"\"\n\"2019-09-10T18:18:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"\",    \"2.3\", \"\", \"\"\n\"2019-09-10T18:19:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"\",    \"3.1\", \"\", \"\"\n\"2019-09-10T18:20:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"\",    \"3.2\", \"\", \"\""
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
            [
                "2019-09-10T18:13:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1.1",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:14:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "1.9",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:15:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "1.4",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:16:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "1.5",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:17:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "",
                "2.6",
                "",
                ""
            ],
            [
                "2019-09-10T18:18:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "",
                "2.3",
                "",
                ""
            ],
            [
                "2019-09-10T18:19:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "",
                "3.1",
                "",
                ""
            ],
            [
                "2019-09-10T18:20:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "",
                "3.2",
                "",
                ""
            ]
        ],
        "headerRow": [
            "observationTimeStamp",
            "studyDbId",
            "studyName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "observationUnitName",
            "plotNumber",
            "plantNumber",
            "blockNumber",
            "entryNumber",
            "replicate",
            "positionCoordinateX",
            "positionCoordinateY"
        ],
        "observationVariableDbIds": [
            "367aa1a9",
            "2acb934c",
            "85a21ce1",
            "46f590e5"
        ],
        "observationVariableNames": [
            "Plant height",
            "Carotenoid",
            "Root color",
            "Virus severity"
        ]
    }
}
```

+ Response 200 (application/tsv)
```
"\"observationTimeStamp\"\t\"studyDbId\"\t\"studyName\"\t\"germplasmDbId\"\t\"germplasmName\"\t\"observationUnitDbId\"\t\"observationUnitName\"\t\"plotNumber\"\t\"plantNumber\"\t\"blockNumber\"\t\"entryNumber\"\t\"replicate\"\t\"positionCoordinateX\"\t\"positionCoordinateY\"\t\"2d599b04\"\t\"a0e84c5c\"\t\"35c5670a\"\t\"0144dea8\"\n\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"Plant height\"\t\"Carotenoid\"\t\"Root color\"\t\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"1.1\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:14:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"1.9\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:15:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"1.4\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:16:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"1.5\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:17:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"\"\t\"2.6\"\t\"\"\t\"\"\n\"2019-09-10T18:18:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"\"\t\"2.3\"\t\"\"\t\"\"\n\"2019-09-10T18:19:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"\"\t\"3.1\"\t\"\"\t\"\"\n\"2019-09-10T18:20:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"\"\t\"3.2\"\t\"\"\t\"\""
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




### Get - /observationunits/{observationUnitDbId} [GET /brapi/v1/observationunits/{observationUnitDbId}]

Get the details of a specific Observation Unit



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationLevel": "plot",
        "observationUnitDbId": "8c67503c",
        "observationUnitName": "Plot 1",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "blockNumber": "6",
            "entryNumber": "3",
            "entryType": [
                "CHECK",
                "TEST",
                "FILLER"
            ],
            "geoCoordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW",
            "replicate": "1"
        },
        "observationUnitXref": [
            {
                "id": "SAMEA_179865230",
                "source": "ebi.biosample"
            },
            {
                "id": "INRA:4d45d11c",
                "source": "gnpis.lot"
            }
        ],
        "plantNumber": "1",
        "plotNumber": "01",
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
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




### Put - /observationunits/{observationUnitDbId} [PUT /brapi/v1/observationunits/{observationUnitDbId}]

Update an existing Observation Units

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "germplasmDbId": "e9d9ed57",
    "germplasmName": "A0000001",
    "locationDbId": "0e208b20",
    "locationName": "Field Station Alpha",
    "observationLevel": "plot",
    "observationUnitName": "Plot 1",
    "observationUnitPUI": "http://pui.per/plot/1a9afc14",
    "observationUnitPosition": {
        "blockNumber": "6",
        "entryNumber": "3",
        "entryType": [
            "CHECK",
            "TEST",
            "FILLER"
        ],
        "geoCoordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "positionCoordinateX": "74",
        "positionCoordinateXType": "GRID_COL",
        "positionCoordinateY": "03",
        "positionCoordinateYType": "GRID_ROW",
        "replicate": "1"
    },
    "observationUnitXref": [
        {
            "id": "SAMEA_179865230",
            "source": "ebi.biosample"
        },
        {
            "id": "INRA:4d45d11c",
            "source": "gnpis.lot"
        }
    ],
    "plantNumber": "1",
    "plotNumber": "01",
    "programDbId": "2d763a7a",
    "programName": "The Perfect Breeding Program",
    "studyDbId": "9865addc",
    "studyName": "Purple_Tomato_1",
    "treatments": [
        {
            "factor": "fertilizer",
            "modality": "low fertilizer"
        }
    ],
    "trialDbId": "776a609c",
    "trialName": "Purple Tomato"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationLevel": "plot",
        "observationUnitDbId": "8c67503c",
        "observationUnitName": "Plot 1",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "blockNumber": "6",
            "entryNumber": "3",
            "entryType": [
                "CHECK",
                "TEST",
                "FILLER"
            ],
            "geoCoordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW",
            "replicate": "1"
        },
        "observationUnitXref": [
            {
                "id": "SAMEA_179865230",
                "source": "ebi.biosample"
            },
            {
                "id": "INRA:4d45d11c",
                "source": "gnpis.lot"
            }
        ],
        "plantNumber": "1",
        "plotNumber": "01",
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
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




### Post - /search/observationunits [POST /brapi/v1/search/observationunits]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.

Use case - this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.

Example Use cases 

- Study a panel of germplasm across multiple studies

- Get all data for a specific study 

- Get simple atomic phenotyping values 

- Study Locations for adaptation to climate change

- Find phenotypes that are from after a certain timestamp

observationTimeStampRangeStart and observationTimeStampRangeEnd use Iso Standard 8601.

observationValue data type inferred from the ontology

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationUnitDbIds|array[string]|The unique id of an observation unit|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|list of programs to search across|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "621b6f1b",
        "cdb7a727"
    ],
    "locationDbIds": [
        "88da535f",
        "1554486a"
    ],
    "observationLevel": "plant",
    "observationUnitDbIds": [
        "66bab7e3",
        "0e5e7f99"
    ],
    "page": 0,
    "pageSize": 1000,
    "programDbIds": [
        "ea41cd20",
        "f03f211a"
    ],
    "studyDbIds": [
        "c74f8370",
        "dd021ad9"
    ],
    "trialDbIds": [
        "4688d49c",
        "3c90127d"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA_179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:4d45d11c",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/observationunits/{searchResultsDbId} [GET /brapi/v1/search/observationunits/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"  MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 102 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA_179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:4d45d11c",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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

# Group Observation Variables

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.





### Post - /search/variables [POST /brapi/v1/search/variables]

Search observation variables.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dataTypes|array[string]|List of scale data types to filter search results|
|methodDbIds|array[string]|List of methods to filter search results|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|observationVariableNames|array[string]|List of human readable observation variable names to search for|
|observationVariableXrefs|array[string]|List of cross references for the observation variable to search for|
|ontologyDbIds|array[string]|List of ontology IDs to search for|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|scaleDbIds|array[string]|List of scales to filter search results|
|scaleXrefs|array[string]|List of cross references for the scale to search for|
|studyDbId|array[string]|The unique ID of a studies to filter on|
|traitClasses|array[string]|List of trait classes to filter search results|
|traitDbIds|array[string]|List of trait unique ID to filter search results|
|traitXrefs|array[string]|List of cross references for the trait to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableDbId|string|Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.|
|observationVariableName|string|Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataTypes": [
        "Numerical",
        "Ordinal",
        "Text"
    ],
    "methodDbIds": [
        "07e34f83",
        "d3d5517a"
    ],
    "observationVariableDbIds": [
        "2ef15c9f",
        "318e7f7d"
    ],
    "observationVariableNames": [
        "Plant Height 1",
        "Root Color"
    ],
    "observationVariableXrefs": [
        " http://purl.obolibrary.org/obo/ro.owl",
        " http://purl.obolibrary.org/obo/ro.owl"
    ],
    "ontologyDbIds": [
        "f44f7b23",
        "a26b576e"
    ],
    "page": 0,
    "pageSize": 1000,
    "scaleDbIds": [
        "a13ecffa",
        "7e1afe4f"
    ],
    "scaleXrefs": [
        " http://purl.obolibrary.org/obo/ro.owl",
        " http://purl.obolibrary.org/obo/ro.owl"
    ],
    "studyDbId": [
        "5bcac0ae",
        "7f48e22d"
    ],
    "traitClasses": [
        "morphological",
        "phenological",
        "agronomical"
    ],
    "traitDbIds": [
        "ef81147b",
        "78d82fad"
    ],
    "traitXrefs": [
        " http://purl.obolibrary.org/obo/ro.owl",
        " http://purl.obolibrary.org/obo/ro.owl"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/variables/{searchResultsDbId} [GET /brapi/v1/search/variables/{searchResultsDbId}{?page}{?pageSize}]

Search observation variables.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableDbId|string|Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.|
|observationVariableName|string|Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 102 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Get - /variables [GET /brapi/v1/variables{?observationVariableDbId}{?traitClass}{?studyDbId}{?page}{?pageSize}]

Call to retrieve a list of observationVariables available in the system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableDbId|string|Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.|
|observationVariableName|string|Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


 

+ Parameters
    + observationVariableDbId (Optional, ) ... Variable's unique ID
    + traitClass (Optional, ) ... Variable's trait class (phenological, physiological, morphological, etc.)
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Post - /variables [POST /brapi/v1/variables]

Add new Observation Variables to the system.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableName|string|Variable name (usually a short name)|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableDbId|string|Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.|
|observationVariableName|string|Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": 2.0,
        "documentationURL": "https://wiki.brapi.org/documentation.html",
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
            "additionalInfo": {},
            "description": "A measuring tape was used",
            "formula": "a^2 + b^2 = c^2",
            "methodClass": "Measurement",
            "methodDbId": "0adb2764",
            "methodName": "Measuring Tape",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
        },
        "observationVariableName": "Variable Name",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scale": {
            "dataType": [
                "Code",
                "Date",
                "Duration",
                "Nominal",
                "Numerical",
                "Ordinal",
                "Text"
            ],
            "decimalPlaces": 2,
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "validValues": {
                "categories": [
                    {
                        "label": "low",
                        "value": "0"
                    },
                    {
                        "label": "medium",
                        "value": "5"
                    },
                    {
                        "label": "high",
                        "value": "10"
                    }
                ],
                "max": 9999,
                "min": 2
            },
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "H",
                "PH",
                "H1"
            ],
            "attribute": "height",
            "entity": "Stalk",
            "mainAbbreviation": "PH",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "status": "recommended",
            "synonyms": [
                "Height",
                "Plant Height",
                "Stalk Height",
                "Canopy Height"
            ],
            "traitClass": "phenological",
            "traitDbId": "9b2e34f5",
            "traitDescription": "The height of the plant",
            "traitName": "Height",
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Get - /variables/{observationVariableDbId} [GET /brapi/v1/variables/{observationVariableDbId}]

Retrieve variable details



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableDbId|string|Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.|
|observationVariableName|string|Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": 2.0,
        "documentationURL": "https://wiki.brapi.org/documentation.html",
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
            "additionalInfo": {},
            "description": "A measuring tape was used",
            "formula": "a^2 + b^2 = c^2",
            "methodClass": "Measurement",
            "methodDbId": "0adb2764",
            "methodName": "Measuring Tape",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
        },
        "observationVariableDbId": "b9b7edd1",
        "observationVariableName": "Variable Name",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scale": {
            "dataType": [
                "Code",
                "Date",
                "Duration",
                "Nominal",
                "Numerical",
                "Ordinal",
                "Text"
            ],
            "decimalPlaces": 2,
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "validValues": {
                "categories": [
                    {
                        "label": "low",
                        "value": "0"
                    },
                    {
                        "label": "medium",
                        "value": "5"
                    },
                    {
                        "label": "high",
                        "value": "10"
                    }
                ],
                "max": 9999,
                "min": 2
            },
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "H",
                "PH",
                "H1"
            ],
            "attribute": "height",
            "entity": "Stalk",
            "mainAbbreviation": "PH",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "status": "recommended",
            "synonyms": [
                "Height",
                "Plant Height",
                "Stalk Height",
                "Canopy Height"
            ],
            "traitClass": "phenological",
            "traitDbId": "9b2e34f5",
            "traitDescription": "The height of the plant",
            "traitName": "Height",
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Put - /variables/{observationVariableDbId} [PUT /brapi/v1/variables/{observationVariableDbId}]

Update an existing Observation Variable



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|method|object||
|additionalInfo|object|Additional arbitrary info|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|observationVariableDbId|string|Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.|
|observationVariableName|string|Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": 2.0,
        "documentationURL": "https://wiki.brapi.org/documentation.html",
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
            "additionalInfo": {},
            "description": "A measuring tape was used",
            "formula": "a^2 + b^2 = c^2",
            "methodClass": "Measurement",
            "methodDbId": "0adb2764",
            "methodName": "Measuring Tape",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
        },
        "observationVariableDbId": "b9b7edd1",
        "observationVariableName": "Variable Name",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scale": {
            "dataType": [
                "Code",
                "Date",
                "Duration",
                "Nominal",
                "Numerical",
                "Ordinal",
                "Text"
            ],
            "decimalPlaces": 2,
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "validValues": {
                "categories": [
                    {
                        "label": "low",
                        "value": "0"
                    },
                    {
                        "label": "medium",
                        "value": "5"
                    },
                    {
                        "label": "high",
                        "value": "10"
                    }
                ],
                "max": 9999,
                "min": 2
            },
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "H",
                "PH",
                "H1"
            ],
            "attribute": "height",
            "entity": "Stalk",
            "mainAbbreviation": "PH",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "status": "recommended",
            "synonyms": [
                "Height",
                "Plant Height",
                "Stalk Height",
                "Canopy Height"
            ],
            "traitClass": "phenological",
            "traitDbId": "9b2e34f5",
            "traitDescription": "The height of the plant",
            "traitName": "Height",
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
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


# Group Observations

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 






### Get - /observations [GET /brapi/v1/observations{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?page}{?pageSize}]

Retrieve all observations where there are measurements for the given observation variables.

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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




### Post - /observations [POST /brapi/v1/observations]

Add new Observation entities

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "collector": "917d3ae0",
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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




### Put - /observations [PUT /brapi/v1/observations]

Update multiple Observation entities simultaneously with a single call

Include as many `observationDbIds` in the request as needed.

Note - In strictly typed languages, this structure can be represented as a Map or Dictionary of objects and parsed directly from JSON.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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




### Get - /observations/table [GET /brapi/v1/observations/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?searchResultsDbId}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}]

<p>This service is designed to retrieve a table of time dependant observation values as a matrix of Observation Units and Observation Variables.
This is also sometimes called a Time Series. This service takes the "Sparse Table" approach for representing this time dependant data.</p>
<p>The table may be represented by JSON, CSV, or TSV. The "Accept" HTTP header is used for the client to request different return formats. 
By default, if the "Accept" header is not included in the request, the server should return JSON as described below.</p>
<p>The table is REQUIRED to have the following columns</p>
<ul>
  <li>observationUnitDbId - Each row is related to one Observation Unit</li>
  <li>observationTimeStamp</li>
  <li>At least one column with an observationVariableDbId</li>
</ul>
<p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p>
<ul>
  <li>observationUnitName</li>
  <li>studyDbId</li>
  <li>studyName</li>
  <li>germplasmDbId</li>
  <li>germplasmName</li>
  <li>plotNumber</li>
  <li>plantNumber</li>
  <li>blockNumber</li>
  <li>entryNumber</li>
  <li>replicate</li>
  <li>positionCoordinateX</li>
  <li>positionCoordinateY</li>
</ul>
<p>The JSON representation provides a pair of extra arrays for defining the headers of the table. 
The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names. 
The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table. 
By appending the two arrays, you can construct the complete header row of the table. </p>
<p>For CSV and TSV representations of the table, an extra header row is needed to describe both the Observation Variable DbId and the Observation Variable Name for each data column. 
See the example responses below</p> 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|headerRow|array[string]|The header row describing observation unit fields. Append "observationVariableDbIds" for complete header row of the table.  This array should contain any or all of the following strings; year, studyDbId, studyName, locationDbId, locationName, germplasmDbId, germplasmName, observationUnitDbId, plotNumber, replicate, blockNumber, entryType, X, Y|
|observationVariableDbIds|array[string]|The list of observation variables which have values recorded for them in the data matrix. Append to the "headerRow" for complete header row.|
|observationVariableNames|array[string]|The list of observation variable names which have values recorded for them in the data matrix. Order should match "observationVariableDbIds".|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + searchResultsDbId (Optional, ) ... Permanent unique identifier which references the search results
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/csv)
```
"\"observationTimeStamp\",\"studyDbId\",\"studyName\",\"germplasmDbId\",\"germplasmName\",\"observationUnitDbId\",\"observationUnitName\",\"plotNumber\",\"plantNumber\",\"blockNumber\",\"entryNumber\",\"replicate\",\"positionCoordinateX\",\"positionCoordinateY\",\"2d599b04\",\"a0e84c5c\",\"35c5670a\",\"0144dea8\"\n\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"Plant height\",\"Carotenoid\",\"Root color\",\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"1.1\", \"\",    \"\", \"\"\n\"2019-09-10T18:14:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"1.9\", \"\",    \"\", \"\"\n\"2019-09-10T18:15:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"1.4\", \"\",    \"\", \"\"\n\"2019-09-10T18:16:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"1.5\", \"\",    \"\", \"\"\n\"2019-09-10T18:17:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"\",    \"2.6\", \"\", \"\"\n\"2019-09-10T18:18:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"\",    \"2.3\", \"\", \"\"\n\"2019-09-10T18:19:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"\",    \"3.1\", \"\", \"\"\n\"2019-09-10T18:20:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"\",    \"3.2\", \"\", \"\""
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
            [
                "2019-09-10T18:13:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1.1",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:14:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "1.9",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:15:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "1.4",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:16:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "1.5",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:17:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "",
                "2.6",
                "",
                ""
            ],
            [
                "2019-09-10T18:18:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "",
                "2.3",
                "",
                ""
            ],
            [
                "2019-09-10T18:19:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "",
                "3.1",
                "",
                ""
            ],
            [
                "2019-09-10T18:20:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "",
                "3.2",
                "",
                ""
            ]
        ],
        "headerRow": [
            "observationTimeStamp",
            "studyDbId",
            "studyName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "observationUnitName",
            "plotNumber",
            "plantNumber",
            "blockNumber",
            "entryNumber",
            "replicate",
            "positionCoordinateX",
            "positionCoordinateY"
        ],
        "observationVariableDbIds": [
            "367aa1a9",
            "2acb934c",
            "85a21ce1",
            "46f590e5"
        ],
        "observationVariableNames": [
            "Plant height",
            "Carotenoid",
            "Root color",
            "Virus severity"
        ]
    }
}
```

+ Response 200 (application/tsv)
```
"\"observationTimeStamp\"\t\"studyDbId\"\t\"studyName\"\t\"germplasmDbId\"\t\"germplasmName\"\t\"observationUnitDbId\"\t\"observationUnitName\"\t\"plotNumber\"\t\"plantNumber\"\t\"blockNumber\"\t\"entryNumber\"\t\"replicate\"\t\"positionCoordinateX\"\t\"positionCoordinateY\"\t\"2d599b04\"\t\"a0e84c5c\"\t\"35c5670a\"\t\"0144dea8\"\n\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"Plant height\"\t\"Carotenoid\"\t\"Root color\"\t\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"1.1\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:14:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"1.9\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:15:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"1.4\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:16:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"1.5\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:17:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"\"\t\"2.6\"\t\"\"\t\"\"\n\"2019-09-10T18:18:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"\"\t\"2.3\"\t\"\"\t\"\"\n\"2019-09-10T18:19:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"\"\t\"3.1\"\t\"\"\t\"\"\n\"2019-09-10T18:20:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"\"\t\"3.2\"\t\"\"\t\"\""
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




### Get - /observations/{observationDbId} [GET /brapi/v1/observations/{observationDbId}]

Get the details of a specific Observations

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + observationDbId (Required, ) ... The unique ID of an observation
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "collector": "917d3ae0",
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationDbId": "ef24b615",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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




### Put - /observations/{observationDbId} [PUT /brapi/v1/observations/{observationDbId}]

Update an existing Observation

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + observationDbId (Required, ) ... The unique ID of an observation
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "collector": "917d3ae0",
    "germplasmDbId": "2408ab11",
    "germplasmName": "A0000003",
    "observationTimeStamp": "2018-01-01T14:47:23-0600",
    "observationUnitDbId": "598111d4",
    "observationUnitName": "Plot 1",
    "observationVariableDbId": "c403d107",
    "observationVariableName": "Plant Height in meters",
    "season": {
        "season": "Spring",
        "seasonDbId": "Spring_2018",
        "year": 2018
    },
    "studyDbId": "ef2829db",
    "uploadedBy": "a2f7f60b",
    "value": "2.3"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "collector": "917d3ae0",
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationDbId": "ef24b615",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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




### Post - /search/observations [POST /brapi/v1/search/observations]

Submit a search request for a set of Observations. Returns an Id which reference the results of this search

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationDbIds|array[string]|The unique id of an Observation|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationUnitDbIds|array[string]|The unique id of an Observation Unit|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "fc55fa61",
        "7f5b77be"
    ],
    "locationDbIds": [
        "071d09d3",
        "6e3fc921"
    ],
    "observationDbIds": [
        "6a4a59d8",
        "3ff067e0"
    ],
    "observationLevel": "plot",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationUnitDbIds": [
        "76f559b5",
        "066bc5d3"
    ],
    "observationVariableDbIds": [
        "a646187d",
        "6d23513b"
    ],
    "page": 0,
    "pageSize": 1000,
    "programDbIds": [
        "d8ca7076",
        "d56b0b68"
    ],
    "seasonDbIds": [
        "Spring 2018",
        "Season A"
    ],
    "studyDbIds": [
        "222e0bc3",
        "8b24d5aa"
    ],
    "trialDbIds": [
        "918c52f8",
        "378f58e6"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/observations/{searchResultsDbId} [GET /brapi/v1/search/observations/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of Observations based on search criteria.

observationTimeStamp - Iso Standard 8601.

observationValue data type inferred from the ontology



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 102 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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


# Group Ontologies

API to manage the details of stored Ontologies. This could be a reference a local Ontology or a remote public Ontology.  






### Get - /ontologies [GET /brapi/v1/ontologies{?page}{?pageSize}]

Call to retrieve a list of observation variable ontologies available in the system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|authors|string|Ontology's list of authors (no specific format)|
|copyright|string|Ontology copyright|
|description|string|Human readable description of Ontology|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|licence|string|Ontology licence|
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "additionalInfo": {},
                "authors": "Bob Robertson, Rob Robertson",
                "copyright": "Copyright 1987, Bob Robertson",
                "description": "This is an example ontology that does not exist",
                "documentationURL": "https://wiki.brapi.org/ontology",
                "licence": "MIT Open source licence",
                "ontologyDbId": "18e186cd",
                "ontologyName": "The Official Ontology",
                "version": "V1.3.2"
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


# Group Scales

API to manage the details of observation variable Scales. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Scale describes the units and acceptable values for a Variable. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Scale "inches" or "pixels". 






### Get - /scales [GET /brapi/v1/scales{?page}{?pageSize}]

Returns a list of Scales available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "dataType": [
                    "Code",
                    "Date",
                    "Duration",
                    "Nominal",
                    "Numerical",
                    "Ordinal",
                    "Text"
                ],
                "decimalPlaces": 2,
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scaleDbId": "af730171",
                "scaleName": "Meters",
                "validValues": {
                    "categories": [
                        {
                            "label": "low",
                            "value": "0"
                        },
                        {
                            "label": "medium",
                            "value": "5"
                        },
                        {
                            "label": "high",
                            "value": "10"
                        }
                    ],
                    "max": 9999,
                    "min": 2
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Post - /scales [POST /brapi/v1/scales]

Create a new scale object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "dataType": [
            "Code",
            "Date",
            "Duration",
            "Nominal",
            "Numerical",
            "Ordinal",
            "Text"
        ],
        "decimalPlaces": 2,
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scaleName": "Meters",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "min": 2
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "dataType": [
                    "Code",
                    "Date",
                    "Duration",
                    "Nominal",
                    "Numerical",
                    "Ordinal",
                    "Text"
                ],
                "decimalPlaces": 2,
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scaleDbId": "af730171",
                "scaleName": "Meters",
                "validValues": {
                    "categories": [
                        {
                            "label": "low",
                            "value": "0"
                        },
                        {
                            "label": "medium",
                            "value": "5"
                        },
                        {
                            "label": "high",
                            "value": "10"
                        }
                    ],
                    "max": 9999,
                    "min": 2
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Get - /scales/{scaleDbId} [GET /brapi/v1/scales/{scaleDbId}]

Retrieve details about a specific scale

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "dataType": [
            "Code",
            "Date",
            "Duration",
            "Nominal",
            "Numerical",
            "Ordinal",
            "Text"
        ],
        "decimalPlaces": 2,
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scaleDbId": "af730171",
        "scaleName": "Meters",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "min": 2
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Put - /scales/{scaleDbId} [PUT /brapi/v1/scales/{scaleDbId}]

Update the details of an existing scale

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale  MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable|
|validValues|object||
|categories|array[object]|List of possible values with optional labels|
|label|string|A text label for a category|
|value|string|The actual value for a category|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataType": [
        "Code",
        "Date",
        "Duration",
        "Nominal",
        "Numerical",
        "Ordinal",
        "Text"
    ],
    "decimalPlaces": 2,
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": [
                    "OBO",
                    "RDF",
                    "WEBPAGE"
                ]
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
    },
    "scaleName": "Meters",
    "validValues": {
        "categories": [
            {
                "label": "low",
                "value": "0"
            },
            {
                "label": "medium",
                "value": "5"
            },
            {
                "label": "high",
                "value": "10"
            }
        ],
        "max": 9999,
        "min": 2
    },
    "xref": "http://purl.obolibrary.org/obo/ro.owl"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "dataType": [
            "Code",
            "Date",
            "Duration",
            "Nominal",
            "Numerical",
            "Ordinal",
            "Text"
        ],
        "decimalPlaces": 2,
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scaleDbId": "af730171",
        "scaleName": "Meters",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "min": 2
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
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


# Group Traits

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 






### Get - /traits [GET /brapi/v1/traits{?page}{?pageSize}]

Call to retrieve a list of traits available in the system and their associated variables.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "alternativeAbbreviations": [
                    "H",
                    "PH",
                    "H1"
                ],
                "attribute": "height",
                "entity": "Stalk",
                "mainAbbreviation": "PH",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "status": "recommended",
                "synonyms": [
                    "Height",
                    "Plant Height",
                    "Stalk Height",
                    "Canopy Height"
                ],
                "traitClass": "phenological",
                "traitDbId": "9b2e34f5",
                "traitDescription": "The height of the plant",
                "traitName": "Height",
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Post - /traits [POST /brapi/v1/traits]

Create a new trait object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "alternativeAbbreviations": [
            "H",
            "PH",
            "H1"
        ],
        "attribute": "height",
        "entity": "Stalk",
        "mainAbbreviation": "PH",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "status": "recommended",
        "synonyms": [
            "Height",
            "Plant Height",
            "Stalk Height",
            "Canopy Height"
        ],
        "traitClass": "phenological",
        "traitDescription": "The height of the plant",
        "traitName": "Height",
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "alternativeAbbreviations": [
                    "H",
                    "PH",
                    "H1"
                ],
                "attribute": "height",
                "entity": "Stalk",
                "mainAbbreviation": "PH",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "status": "recommended",
                "synonyms": [
                    "Height",
                    "Plant Height",
                    "Stalk Height",
                    "Canopy Height"
                ],
                "traitClass": "phenological",
                "traitDbId": "9b2e34f5",
                "traitDescription": "The height of the plant",
                "traitName": "Height",
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Get - /traits/{traitDbId} [GET /brapi/v1/traits/{traitDbId}]

Retrieve the details of a single trait

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


 

+ Parameters
    + traitDbId (Required, ) ... Id of the trait to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "alternativeAbbreviations": [
            "H",
            "PH",
            "H1"
        ],
        "attribute": "height",
        "entity": "Stalk",
        "mainAbbreviation": "PH",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "status": "recommended",
        "synonyms": [
            "Height",
            "Plant Height",
            "Stalk Height",
            "Canopy Height"
        ],
        "traitClass": "phenological",
        "traitDbId": "9b2e34f5",
        "traitDescription": "The height of the plant",
        "traitName": "Height",
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
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




### Put - /traits/{traitDbId} [PUT /brapi/v1/traits/{traitDbId}]

Update an existing trait

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitDescription|string|The description of a trait|
|traitName|string|The human readable name of a trait  MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


 

+ Parameters
    + traitDbId (Required, ) ... Id of the trait to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "alternativeAbbreviations": [
        "H",
        "PH",
        "H1"
    ],
    "attribute": "height",
    "entity": "Stalk",
    "mainAbbreviation": "PH",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": [
                    "OBO",
                    "RDF",
                    "WEBPAGE"
                ]
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
    },
    "status": "recommended",
    "synonyms": [
        "Height",
        "Plant Height",
        "Stalk Height",
        "Canopy Height"
    ],
    "traitClass": "phenological",
    "traitDescription": "The height of the plant",
    "traitName": "Height",
    "xref": "http://purl.obolibrary.org/obo/ro.owl"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "alternativeAbbreviations": [
            "H",
            "PH",
            "H1"
        ],
        "attribute": "height",
        "entity": "Stalk",
        "mainAbbreviation": "PH",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "status": "recommended",
        "synonyms": [
            "Height",
            "Plant Height",
            "Stalk Height",
            "Canopy Height"
        ],
        "traitClass": "phenological",
        "traitDbId": "9b2e34f5",
        "traitDescription": "The height of the plant",
        "traitName": "Height",
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
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

