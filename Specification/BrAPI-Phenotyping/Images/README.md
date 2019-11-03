# Group Images

Calls for manipulating images

Implementation Notes:

The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 



## Images [/brapi/v1/images] 




### Get Images  [GET /brapi/v1/images{?imageDbId}{?imageName}{?observationUnitDbId}{?observationDbId}{?descriptiveOntologyTerm}{?page}{?pageSize}]

Get filtered set of image meta data

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageDbId|string|The unique identifier of an image|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
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
                "imageTimeStamp": "2018-01-01",
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





### Post Images  [POST /brapi/v1/images]

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
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageDbId|string|The unique identifier of an image|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
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
        "imageTimeStamp": "2018-01-01",
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
                "imageTimeStamp": "2018-01-01",
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





### Get Images by imageDbId  [GET /brapi/v1/images/{imageDbId}]

Get one image meta data object

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageDbId|string|The unique identifier of an image|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
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
        "imageTimeStamp": "2018-01-01",
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





### Put Images by imageDbId  [PUT /brapi/v1/images/{imageDbId}]

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
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageDbId|string|The unique identifier of an image|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
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
    "imageTimeStamp": "2018-01-01",
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
        "imageTimeStamp": "2018-01-01",
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





### Put Images Imagecontent by imageDbId  [PUT /brapi/v1/images/{imageDbId}/imagecontent]

Update an image with the image file content

Implementation Notes

- This call should be paired with 'PUT /images/{imageDbId}' for full capability

- A server may choose to modify the image meta data object based on the actually image which has been uploaded. 

- Image data may be stored in a database or file system. Servers should generate and provide the "imageURL" for retrieving the image, wherever it happens to live.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageDbId|string|The unique identifier of an image|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
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
        "imageTimeStamp": "2018-01-01",
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



## Search [/brapi/v1/search] 




### Post Search Images  [POST /brapi/v1/search/images]

Get filtered set of image meta data

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|imageTimeStampRangeEnd|string (date)|The latest timestamp to search for.|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image to search for. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|observationUnitDbIds|array[string]|A set of observation unit identifiers to search for.|
|imageHeightMax|integer|A maximum image height to search for.|
|imageNames|array[string]|Human readable names to search for.|
|imageWidthMin|integer|A minimum image width to search for.|
|imageHeightMin|integer|A minimum image height to search for.|
|imageWidthMax|integer|A maximum image width to search for.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|imageTimeStampRangeStart|string (date)|The earliest timestamp to search for.|
|imageFileSizeMax|integer|A maximum image file size to search for.|
|mimeTypes|array[string]|A set of image file types to search for.|
|imageFileSizeMin|integer|A minimum image file size to search for.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with to search for|
|imageFileNames|array[string]|Image file names to search for.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

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
    "imageTimeStampRangeEnd": "2018-01-01",
    "imageTimeStampRangeStart": "2018-01-01",
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





### Get Search Images by searchResultsDbId  [GET /brapi/v1/search/images/{searchResultsDbId}{?page}{?pageSize}]

Get filtered set of image meta data

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI''s.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of image meta data|
|mimeType|string|The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc|
|imageTimeStamp|string (date)|The date and time the image was taken|
|descriptiveOntologyTerms|array[string]|A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.|
|imageFileSize|integer|The size of the image in Bytes.|
|imageDbId|string|The unique identifier of an image|
|imageHeight|integer|The height of the image in Pixels.|
|imageURL|string|The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.|
|additionalInfo|object||
|imageWidth|integer|The width of the image in Pixels.|
|observationDbIds|array[string]|A list of observation Ids this image is associated with, if applicable.|
|imageName|string|The human readable name of an image. Might be the same as 'imageFileName', but could be different.|
|description|string|The human readable description of an image.|
|imageFileName|string|The name of the image file. Might be the same as 'imageName', but could be different.|
|imageLocation|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|copyright|string|The copyright information of this image. Example 'Copyright 2018 Bob Robertson'|
|observationUnitDbId|string|The related observation unit identifier, if relevant.|


 

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
                "imageTimeStamp": "2018-01-01",
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

