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

- 'imageURL' should be a complete URL decribing the location of the image. There is no BrAPI call for retireiving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.  

 

+ Parameters
    + imageDbId (Optional, ) ... The unique identifier for a image
    + imageName (Optional, ) ... The human readable name of an image
    + observationUnitDbId (Optional, ) ... The unique identifier of the observation unit an image is portraying
    + observationDbId (Optional, ) ... The unique identifier of the observation an image is accosiated with
    + descriptiveOntologyTerm (Optional, ) ... A descriptive term associated with an image
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "additionalInfo": null,
                "copyright": null,
                "description": null,
                "descriptiveOntologyTerms": [
                    ""
                ],
                "imageDbId": "940028bc-7ad6-4119-b6af-936ade8f0cb3",
                "imageFileName": null,
                "imageFileSize": null,
                "imageHeight": null,
                "imageLocation": null,
                "imageName": null,
                "imageTimeStamp": null,
                "imageURL": null,
                "imageWidth": null,
                "mimeType": null,
                "observationDbIds": [
                    ""
                ],
                "observationUnitDbId": null
            },
            {
                "additionalInfo": null,
                "copyright": null,
                "description": null,
                "descriptiveOntologyTerms": [
                    ""
                ],
                "imageDbId": "8a4c82c1-f1f2-4334-adec-4d693b2da1e6",
                "imageFileName": null,
                "imageFileSize": null,
                "imageHeight": null,
                "imageLocation": null,
                "imageName": null,
                "imageTimeStamp": null,
                "imageURL": null,
                "imageWidth": null,
                "mimeType": null,
                "observationDbIds": [
                    ""
                ],
                "observationUnitDbId": null
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Post Images  [POST /brapi/v1/images]

Create a new image meta data object

Implementation Notes

- 'imageURL' should be a complete URL decribing the location of the image. There is no BrAPI call for retireiving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.

- The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons.

- With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera.

- For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 

 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "copyright": "copyright0",
    "description": "description0",
    "descriptiveOntologyTerms": [
        "descriptiveOntologyTerms0",
        "descriptiveOntologyTerms1"
    ],
    "imageFileName": "imageFileName0",
    "imageFileSize": 0,
    "imageHeight": 0,
    "imageLocation": {
        "geometry": {},
        "type": "Feature"
    },
    "imageName": "imageName0",
    "imageTimeStamp": "2018-01-01",
    "imageWidth": 0,
    "mimeType": "mimeType0",
    "observationDbIds": [
        "observationDbIds0",
        "observationDbIds1"
    ],
    "observationUnitDbId": "observationUnitDbId0"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "additionalInfo": null,
        "copyright": null,
        "description": null,
        "descriptiveOntologyTerms": [
            ""
        ],
        "imageDbId": "b2d6d3de-afa4-4bda-be92-d430f01af2ba",
        "imageFileName": null,
        "imageFileSize": null,
        "imageHeight": null,
        "imageLocation": null,
        "imageName": null,
        "imageTimeStamp": null,
        "imageURL": null,
        "imageWidth": null,
        "mimeType": null,
        "observationDbIds": [
            ""
        ],
        "observationUnitDbId": null
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Images by imageDbId  [GET /brapi/v1/images/{imageDbId}]

Get one image meta data object

Implementation Notes

- 'imageURL' should be a complete URL decribing the location of the image. There is no BrAPI call for retireiving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's. 

 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": null
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Images by imageDbId  [PUT /brapi/v1/images/{imageDbId}]

Update an image meta data object

Implementation Notes

- This call should be paired with 'PUT /images/{imageDbId}/imagecontent' for full capability

- A server may choose to modify the image meta data object based on the actually image which has been uploaded. 

- Image data may be stored in a database or file system. Servers should generate and provide the \"imageURL\" as an absolute path for retrieving the image, wherever it happens to live. 

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's. 

- The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
        
- With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
        
- For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. '

 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "copyright": "copyright0",
    "description": "description0",
    "descriptiveOntologyTerms": [
        "descriptiveOntologyTerms0",
        "descriptiveOntologyTerms1"
    ],
    "imageFileName": "imageFileName0",
    "imageFileSize": 0,
    "imageHeight": 0,
    "imageLocation": {
        "geometry": {},
        "type": "Feature"
    },
    "imageName": "imageName0",
    "imageTimeStamp": "2018-01-01",
    "imageWidth": 0,
    "mimeType": "mimeType0",
    "observationDbIds": [
        "observationDbIds0",
        "observationDbIds1"
    ],
    "observationUnitDbId": "observationUnitDbId0"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": null
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Images Imagecontent by imageDbId  [PUT /brapi/v1/images/{imageDbId}/imagecontent]

Update an image with the image file content

Implementation Notes

- This call should be paired with 'PUT /images/{imageDbId}' for full capability

- A server may choose to modify the image meta data object based on the actually image which has been uploaded. 

- Image data may be stored in a database or file system. Servers should generate and provide the "imageURL" for retrieving the image, wherever it happens to live.  

 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for a image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "additionalInfo": {},
        "copyright": "copyright0",
        "description": "description0",
        "descriptiveOntologyTerms": [
            "descriptiveOntologyTerms0",
            "descriptiveOntologyTerms1"
        ],
        "imageDbId": "imageDbId0",
        "imageFileName": "imageFileName0",
        "imageFileSize": 0,
        "imageHeight": 0,
        "imageLocation": {
            "geometry": {},
            "type": "Feature"
        },
        "imageName": "imageName0",
        "imageTimeStamp": "2018-01-01",
        "imageURL": "imageURL0",
        "imageWidth": 0,
        "mimeType": "mimeType0",
        "observationDbIds": [
            "observationDbIds0",
            "observationDbIds1"
        ],
        "observationUnitDbId": "observationUnitDbId0"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Images  [POST /brapi/v1/search/images]

Get filtered set of image meta data

Implementation Notes

- 'imageURL' should be a complete URL decribing the location of the image. There is no BrAPI call for retireiving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.  

See Search Services for additional implementation details.

 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "descriptiveOntologyTerms": [
        "descriptiveOntologyTerms0",
        "descriptiveOntologyTerms1"
    ],
    "imageFileNames": [
        "imageFileNames0",
        "imageFileNames1"
    ],
    "imageFileSizeMax": 0,
    "imageFileSizeMin": 0,
    "imageHeightMax": 0,
    "imageHeightMin": 0,
    "imageLocation": {
        "geometry": {},
        "type": "Feature"
    },
    "imageNames": [
        "imageNames0",
        "imageNames1"
    ],
    "imageTimeStampRangeEnd": "2018-01-01",
    "imageTimeStampRangeStart": "2018-01-01",
    "imageWidthMax": 0,
    "imageWidthMin": 0,
    "mimeTypes": [
        "mimeTypes0",
        "mimeTypes1"
    ],
    "observationDbIds": [
        "observationDbIds0",
        "observationDbIds1"
    ],
    "observationUnitDbIds": [
        "observationUnitDbIds0",
        "observationUnitDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Search Images by searchResultsDbId  [GET /brapi/v1/search/images/{searchResultsDbId}{?page}{?pageSize}]

Get filtered set of image meta data

Implementation Notes

- 'imageURL' should be a complete URL decribing the location of the image. There is no BrAPI call for retireiving the image content, so it could be on a different path, or a different host.

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or ontology references, or full ontology URI's.  

 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "copyright": "copyright0",
                "description": "description0",
                "descriptiveOntologyTerms": [
                    "descriptiveOntologyTerms0",
                    "descriptiveOntologyTerms1"
                ],
                "imageDbId": "imageDbId0",
                "imageFileName": "imageFileName0",
                "imageFileSize": 0,
                "imageHeight": 0,
                "imageLocation": {
                    "geometry": {},
                    "type": "Feature"
                },
                "imageName": "imageName0",
                "imageTimeStamp": "2018-01-01",
                "imageURL": "imageURL0",
                "imageWidth": 0,
                "mimeType": "mimeType0",
                "observationDbIds": [
                    "observationDbIds0",
                    "observationDbIds1"
                ],
                "observationUnitDbId": "observationUnitDbId0"
            },
            {
                "additionalInfo": {},
                "copyright": "copyright1",
                "description": "description1",
                "descriptiveOntologyTerms": [
                    "descriptiveOntologyTerms0",
                    "descriptiveOntologyTerms1"
                ],
                "imageDbId": "imageDbId1",
                "imageFileName": "imageFileName1",
                "imageFileSize": 0,
                "imageHeight": 0,
                "imageLocation": {
                    "geometry": {},
                    "type": "Feature"
                },
                "imageName": "imageName1",
                "imageTimeStamp": "2018-01-01",
                "imageURL": "imageURL1",
                "imageWidth": 0,
                "mimeType": "mimeType1",
                "observationDbIds": [
                    "observationDbIds0",
                    "observationDbIds1"
                ],
                "observationUnitDbId": "observationUnitDbId1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

