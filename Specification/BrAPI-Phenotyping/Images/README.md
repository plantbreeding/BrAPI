# Group Images

Calls for retrieving, storing, and updating images and image metadata

Implementation Notes:

The Images endpoints support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 

An example use case is available on the BrAPI Wiki -> https://wiki.brapi.org/index.php/Image_Upload




### Post - /delete/images [POST /brapi/v2/delete/images]

Submit a delete request for `Images`

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image to search for. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">imageDbIds</span></td><td>array[string]</td><td>A list of image Ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">imageFileNames</span></td><td>array[string]</td><td>Image file names to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSizeMax</span></td><td>integer</td><td>A maximum image file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSizeMin</span></td><td>integer</td><td>A minimum image file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeightMax</span></td><td>integer</td><td>A maximum image height to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeightMin</span></td><td>integer</td><td>A minimum image height to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>A GeoJSON Polygon which describes an area to search for other GeoJSON objects. All contained Points and intersecting Polygons should be returned as search results.   All coordinates are decimal values on the WGS84 geographic coordinate reference system.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageNames</span></td><td>array[string]</td><td>Human readable names to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStampRangeEnd</span></td><td>string<br>(date-time)</td><td>The latest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStampRangeStart</span></td><td>string<br>(date-time)</td><td>The earliest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidthMax</span></td><td>integer</td><td>A maximum image width to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidthMin</span></td><td>integer</td><td>A minimum image width to search for.</td></tr>
<tr><td><span style="font-weight:bold;">mimeTypes</span></td><td>array[string]</td><td>A set of image file types to search for.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>A set of observation unit identifiers to search for.</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">imageDbIds</span></td><td>array[string]</td><td>The unique ids of the Image records which have been successfully deleted</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "descriptiveOntologyTerms": [
        "doi:10.1002/0470841559",
        "Red",
        "ncbi:0300294"
    ],
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
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
    "pageSize": 1000,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
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
        "datafiles": [],
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
        "imageDbIds": [
            "6a4a59d8",
            "3ff067e0"
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




### Get - /images [GET /brapi/v2/images{?imageDbId}{?imageName}{?observationUnitDbId}{?observationDbId}{?descriptiveOntologyTerm}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get filtered set of image metadata

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for 
retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive 
words, or ontology references, or full ontology URI''s.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

+ Parameters
    + imageDbId (Optional, ) ... The unique identifier for a image
    + imageName (Optional, ) ... The human readable name of an image
    + observationUnitDbId (Optional, ) ... The unique identifier of the observation unit an image is portraying
    + observationDbId (Optional, ) ... The unique identifier of the observation an image is associated with
    + descriptiveOntologyTerm (Optional, ) ... A descriptive term associated with an image
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

Create new image metadata records

Implementation Notes

- This endpoint should be implemented with 'PUT /images/{imageDbId}/imagecontent' for full image upload capability

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for retrieving 
the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive words, or 
ontology references, or full ontology URI's.

- The '/images' calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON 
only supports two of the possible geometries; Points and Polygons.

- With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera.

- For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and 
latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the 
image content.

An example use case is available on the BrAPI Wiki -> https://wiki.brapi.org/index.php/Image_Upload

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

Get one image metadata object

Implementation Notes

- ''imageURL'' should be a complete URL describing the location of the image. There is no BrAPI call for 
retrieving the image content, so it could be on a different path, or a different host.

- ''descriptiveOntologyTerm'' can be thought of as Tags for the image. These could be simple descriptive 
words, or ontology references, or full ontology URI''s.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

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
        "datafiles": [],
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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

Update an existing image metadata record

Implementation Notes

- This endpoint should be implemented with 'PUT /images/{imageDbId}/imagecontent' for full image update capability

- A server may choose to modify the image metadata object based on the actually image which has been uploaded. 

- Image data may be stored in a database or file system. Servers should generate and provide the "imageURL" as an 
absolute path for retrieving the image, wherever it happens to live. 

- 'descriptiveOntologyTerm' can be thought of as Tags for the image. These could be simple descriptive words, or 
ontology references, or full ontology URI's. 

- The '/images' calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON 
only supports two of the possible geometries; Points and Polygons. 

- With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 

- For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and 
latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the 
image content.

An example use case is available on the BrAPI Wiki -> https://wiki.brapi.org/index.php/Image_Upload

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

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
            "referenceId": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceId": "75a50e76",
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
        "datafiles": [],
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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

This endpoint is used to attach an image binary file to an existing image metadata record. All of the other Images endpoints 
deal with the JSON for image metadata, but 'PUT /images/{imageDbId}/imagecontent' allows you to send any binary file with a Content 
Type (MIME) of image/*. When the real image is uploaded, the server may choose to update some of the metadata to reflect the 
reality of the image that was uploaded, and should respond with the updated JSON.

Implementation Notes

- This endpoint should be implemented with 'POST /images' for full image upload capability

- This endpoint should be implemented with 'PUT /images/{imageDbId}' for full image update capability

- A server may choose to modify the image metadata object based on the actually image which has been uploaded by this endpoint. 

- Image data may be stored in a database or file system. Servers should generate and provide the "imageURL" for retrieving the 
  image binary file. 

An example use case is available on the BrAPI Wiki -> https://wiki.brapi.org/index.php/Image_Upload



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

+ Parameters
    + imageDbId (Required, ) ... The unique identifier for an image
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image to search for. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">imageDbIds</span></td><td>array[string]</td><td>A list of image Ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">imageFileNames</span></td><td>array[string]</td><td>Image file names to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSizeMax</span></td><td>integer</td><td>A maximum image file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSizeMin</span></td><td>integer</td><td>A minimum image file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeightMax</span></td><td>integer</td><td>A maximum image height to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeightMin</span></td><td>integer</td><td>A minimum image height to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>A GeoJSON Polygon which describes an area to search for other GeoJSON objects. All contained Points and intersecting Polygons should be returned as search results.   All coordinates are decimal values on the WGS84 geographic coordinate reference system.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageNames</span></td><td>array[string]</td><td>Human readable names to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStampRangeEnd</span></td><td>string<br>(date-time)</td><td>The latest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStampRangeStart</span></td><td>string<br>(date-time)</td><td>The earliest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidthMax</span></td><td>integer</td><td>A maximum image width to search for.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidthMin</span></td><td>integer</td><td>A minimum image width to search for.</td></tr>
<tr><td><span style="font-weight:bold;">mimeTypes</span></td><td>array[string]</td><td>A set of image file types to search for.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>A set of observation unit identifiers to search for.</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "descriptiveOntologyTerms": [
        "doi:10.1002/0470841559",
        "Red",
        "ncbi:0300294"
    ],
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
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
    "pageSize": 1000,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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
        "datafiles": [],
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td></td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this image. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an image.</td></tr>
<tr><td><span style="font-weight:bold;">descriptiveOntologyTerms</span></td><td>array[string]</td><td>A list of terms to formally describe the image. Each item could be a simple Tag, an Ontology reference Id, or a full ontology URL.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">imageDbId</span></td><td>string</td><td>The unique identifier of an image</td></tr>
<tr><td><span style="font-weight:bold;">imageFileName</span></td><td>string</td><td>The name of the image file. Might be the same as 'imageName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageFileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">imageHeight</span></td><td>integer</td><td>The height of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">imageLocation</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>imageLocation<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">imageName</span></td><td>string</td><td>The human readable name of an image. Might be the same as 'imageFileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">imageTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the image was taken</td></tr>
<tr><td><span style="font-weight:bold;">imageURL</span></td><td>string</td><td>The complete, absolute URI path to the image file. Images might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">imageWidth</span></td><td>integer</td><td>The width of the image in Pixels.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the image. Examples 'image/jpeg', 'image/png', 'image/svg', etc</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>A list of observation Ids this image is associated with, if applicable.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The related observation unit identifier, if relevant.</td></tr>
</table>


 

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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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
        "datafiles": [],
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

