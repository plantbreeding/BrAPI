# Group Images

Calls for manipulating images

Implementation Notes:

The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 




### Get - /images [GET /brapi/v2/images{?imageDbId}{?imageName}{?observationUnitDbId}{?observationDbId}{?descriptiveOntologyTerm}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
    + externalReferenceID (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceID` parameter)
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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




### Post - /images [POST /brapi/v2/images]

Create new image meta data objects

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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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




### Get - /images/{imageDbId} [GET /brapi/v2/images/{imageDbId}]

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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "imageDbId": "a55efb9c",
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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




### Put - /images/{imageDbId} [PUT /brapi/v2/images/{imageDbId}/]

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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
    "externalReferences": [
        {
            "referenceID": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
            "referenceSource": "OBO Library"
        },
        {
            "referenceID": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
    "imageFileName": "image_0000231.jpg",
    "imageFileSize": 50000,
    "imageHeight": 550,
    "imageLocation": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373,
                123
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "imageDbId": "a55efb9c",
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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




### Put - /images/{imageDbId}/imagecontent [PUT /brapi/v2/images/{imageDbId}/imagecontent]

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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "imageDbId": "a55efb9c",
        "imageFileName": "image_0000231.jpg",
        "imageFileSize": 50000,
        "imageHeight": 550,
        "imageLocation": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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




### Post - /search/images [POST /brapi/v2/search/images]

Submit a search request for `XXEntitiesXX`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/XXEntitiesXX/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>
<br/>
Image Implementation Notes<br/>
- `imageURL` should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.<br/>
- `descriptiveOntologyTerm` can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.<br/>

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image to search for. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|externalReferenceIDs|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|imageDbIds|array[string]|A list of image Ids to search for|
|imageFileNames|array[string]|Image file names to search for.|
|imageFileSizeMax|integer|A maximum image file size to search for.|
|imageFileSizeMin|integer|A minimum image file size to search for.|
|imageHeightMax|integer|A maximum image height to search for.|
|imageHeightMin|integer|A minimum image height to search for.|
|imageLocation|object|A GeoJSON Polygon which describes an area to search for other GeoJSON objects. All contained Points and intersecting Polygons should be returned as search results.   All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
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
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
    "externalReferenceIDs": [
        "http://purl.obolibrary.org/obo/ro.owl",
        "14a19841"
    ],
    "externalReferenceSources": [
        "OBO Library",
        "Field App Name"
    ],
    "imageDbIds": [
        "564b64a6",
        "0d122d1d"
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
                [
                    [
                        -77.456654,
                        42.241133
                    ],
                    [
                        -75.414133,
                        41.508282
                    ],
                    [
                        -76.506042,
                        42.417373
                    ],
                    [
                        -77.456654,
                        42.241133
                    ]
                ]
            ],
            "type": "Polygon"
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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




### Get - /search/images/{searchResultsDbId} [GET /brapi/v2/search/images/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Images` search request <br/>
Clients should submit a search request using the corresponding `POST /search/images` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>
<br/>
Image Implementation Notes<br/>
- `imageURL` should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.<br/>
- `descriptiveOntologyTerm` can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.<br/>



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|additionalInfo|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|description|string|The human readable description of an image.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|imageDbId|string|The unique identifier of an image|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
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
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "imageDbId": "a55efb9c",
                "imageFileName": "image_0000231.jpg",
                "imageFileSize": 50000,
                "imageHeight": 550,
                "imageLocation": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

