
# Group Genome Maps

Notes on the `GenomeMaps` objects:
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome





### Get - /maps [GET /brapi/v2/maps{?mapDbId}{?mapPUI}{?scientificName}{?type}{?commonCropName}{?programDbId}{?trialDbId}{?studyDbId}{?page}{?pageSize}]

Get list of maps



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The common name of the `Crop`</td></tr>
<tr><td><span style="font-weight:bold;">mapDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">type</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The type of map this represents, usually "Genetic" or "Physical"</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">comments</span></td><td>string</td><td>Additional comments about a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">linkageGroupCount</span></td><td>integer</td><td>The number of linkage groups present in a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapName</span></td><td>string</td><td>A human readable name for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapPUI</span></td><td>string</td><td>The DOI or other permanent identifier for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">markerCount</span></td><td>integer</td><td>The number of markers present in a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">publishedDate</span></td><td>string<br>(date-time)</td><td>The date this `GenomeMap` was published</td></tr>
<tr><td><span style="font-weight:bold;">scientificName</span></td><td>string</td><td>Full scientific binomial format name. This includes Genus, Species, and Sub-species</td></tr>
<tr><td><span style="font-weight:bold;">unit</span></td><td>string</td><td>The units used to describe the data in a `GenomeMap`</td></tr>
</table>


 

+ Parameters
    + mapDbId (Optional, string) ... The ID which uniquely identifies a `GenomeMap`
    + mapPUI (Optional, string) ... The DOI or other permanent identifier for a `GenomeMap`
    + scientificName (Optional, string) ... Full scientific binomial format name. This includes Genus, Species, and Sub-species
    + type (Optional, string) ... The type of map, usually "Genetic" or "Physical"
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, string) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + studyDbId (Optional, string) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "comments": "Comments about this map",
                "commonCropName": "Paw Paw",
                "documentationURL": "https://brapi.org",
                "linkageGroupCount": 5,
                "mapDbId": "142cffd5",
                "mapName": "Genome Map 1",
                "mapPUI": "doi:10.3207/2959859860",
                "markerCount": 1100,
                "publishedDate": "2018-01-01T14:47:23-0600",
                "scientificName": "Zea mays",
                "type": "Genetic",
                "unit": "cM"
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




### Get - /maps/{mapDbId} [GET /brapi/v2/maps/{mapDbId}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The common name of the `Crop`</td></tr>
<tr><td><span style="font-weight:bold;">mapDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">type</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The type of map this represents, usually "Genetic" or "Physical"</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">comments</span></td><td>string</td><td>Additional comments about a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">linkageGroupCount</span></td><td>integer</td><td>The number of linkage groups present in a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapName</span></td><td>string</td><td>A human readable name for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapPUI</span></td><td>string</td><td>The DOI or other permanent identifier for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">markerCount</span></td><td>integer</td><td>The number of markers present in a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">publishedDate</span></td><td>string<br>(date-time)</td><td>The date this `GenomeMap` was published</td></tr>
<tr><td><span style="font-weight:bold;">scientificName</span></td><td>string</td><td>Full scientific binomial format name. This includes Genus, Species, and Sub-species</td></tr>
<tr><td><span style="font-weight:bold;">unit</span></td><td>string</td><td>The units used to describe the data in a `GenomeMap`</td></tr>
</table>


 

+ Parameters
    + mapDbId (Required, string) ... The ID which uniquely identifies a `GenomeMap`
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
        "comments": "Comments about this map",
        "commonCropName": "Paw Paw",
        "documentationURL": "https://brapi.org",
        "linkageGroupCount": 5,
        "mapDbId": "142cffd5",
        "mapName": "Genome Map 1",
        "mapPUI": "doi:10.3207/2959859860",
        "markerCount": 1100,
        "publishedDate": "2018-01-01T14:47:23-0600",
        "scientificName": "Zea mays",
        "type": "Genetic",
        "unit": "cM"
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




### Get - /maps/{mapDbId}/linkagegroups [GET /brapi/v2/maps/{mapDbId}/linkagegroups{?page}{?pageSize}]

Get the Linkage Groups of a specific Genomic Map. A Linkage Group is the BrAPI generic term for a named section of a map. A Linkage Group can represent a Chromosome, Scaffold, or Linkage Group.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">linkageGroupName</span></td><td>string</td><td>The Uniquely Identifiable name of a `LinkageGroup` <br> This might be a chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.</td></tr>
<tr><td><span style="font-weight:bold;">markerCount</span></td><td>integer</td><td>The number of markers associated with a `LinkageGroup`</td></tr>
<tr><td><span style="font-weight:bold;">maxPosition</span></td><td>integer</td><td>The maximum position of a marker within a `LinkageGroup`</td></tr>
</table>


 

+ Parameters
    + mapDbId (Required, string) ... The ID which uniquely identifies a `GenomeMap`
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "linkageGroupName": "Chromosome 3",
                "markerCount": 150,
                "maxPosition": 2500
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




### Get - /markerpositions [GET /brapi/v2/markerpositions{?mapDbId}{?linkageGroupName}{?variantDbId}{?minPosition}{?maxPosition}{?page}{?pageSize}]

Get marker position information, based on Map, Linkage Group, and Marker ID



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">linkageGroupName</span></td><td>string</td><td>The Uniquely Identifiable name of a `LinkageGroup` <br> This might be a chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.</td></tr>
<tr><td><span style="font-weight:bold;">mapDbId</span></td><td>string</td><td>The ID which uniquely identifies a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapName</span></td><td>string</td><td>A human readable name for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">position</span></td><td>integer</td><td>The position of a marker or variant within a `LinkageGroup`</td></tr>
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Variant` within the given database server <br> A `Variant` can also represent a Marker </td></tr>
<tr><td><span style="font-weight:bold;">variantName</span></td><td>string</td><td>The human readable name for a `Variant` <br> A `Variant` can also represent a Marker </td></tr>
</table>


 

+ Parameters
    + mapDbId (Optional, string) ... The ID which uniquely identifies a `GenomeMap`
    + linkageGroupName (Optional, string) ... The Uniquely Identifiable name of a `LinkageGroup`<br> This might be a chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + variantDbId (Optional, string) ... The unique id for a marker
    + minPosition (Optional, integer) ... The minimum position
    + maxPosition (Optional, integer) ... The maximum position
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "linkageGroupName": "Chromosome 3",
                "mapDbId": "3d52bdf3",
                "mapName": "Genome Map 1",
                "position": 2390,
                "variantDbId": "a1eb250a",
                "variantName": "Marker_2390"
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




### Post - /search/markerpositions [POST /brapi/v2/search/markerpositions]

Submit a search request for `MarkerPositions`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/markerpositions/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">linkageGroupNames</span></td><td>array[string]</td><td>A list of Uniquely Identifiable linkage group names</td></tr>
<tr><td><span style="font-weight:bold;">mapDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `GenomeMaps` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">maxPosition</span></td><td>integer</td><td>The maximum position of markers in a given map</td></tr>
<tr><td><span style="font-weight:bold;">minPosition</span></td><td>integer</td><td>The minimum position of markers in a given map</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Variants` within the given database server</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">linkageGroupName</span></td><td>string</td><td>The Uniquely Identifiable name of a `LinkageGroup` <br> This might be a chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.</td></tr>
<tr><td><span style="font-weight:bold;">mapDbId</span></td><td>string</td><td>The ID which uniquely identifies a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapName</span></td><td>string</td><td>A human readable name for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">position</span></td><td>integer</td><td>The position of a marker or variant within a `LinkageGroup`</td></tr>
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Variant` within the given database server <br> A `Variant` can also represent a Marker </td></tr>
<tr><td><span style="font-weight:bold;">variantName</span></td><td>string</td><td>The human readable name for a `Variant` <br> A `Variant` can also represent a Marker </td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "linkageGroupNames": [
        "Chromosome 2",
        "Chromosome 3"
    ],
    "mapDbIds": [
        "7e6fa8aa",
        "bedc418c"
    ],
    "maxPosition": 4000,
    "minPosition": 250,
    "page": 0,
    "pageSize": 1000,
    "variantDbIds": [
        "a0caa928",
        "f8894a26"
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
                "linkageGroupName": "Chromosome 3",
                "mapDbId": "3d52bdf3",
                "mapName": "Genome Map 1",
                "position": 2390,
                "variantDbId": "a1eb250a",
                "variantName": "Marker_2390"
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




### Get - /search/markerpositions/{searchResultsDbId} [GET /brapi/v2/search/markerpositions/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `MarkerPositions` search request <br/>
Clients should submit a search request using the corresponding `POST /search/markerpositions` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">linkageGroupName</span></td><td>string</td><td>The Uniquely Identifiable name of a `LinkageGroup` <br> This might be a chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.</td></tr>
<tr><td><span style="font-weight:bold;">mapDbId</span></td><td>string</td><td>The ID which uniquely identifies a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">mapName</span></td><td>string</td><td>A human readable name for a `GenomeMap`</td></tr>
<tr><td><span style="font-weight:bold;">position</span></td><td>integer</td><td>The position of a marker or variant within a `LinkageGroup`</td></tr>
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Variant` within the given database server <br> A `Variant` can also represent a Marker </td></tr>
<tr><td><span style="font-weight:bold;">variantName</span></td><td>string</td><td>The human readable name for a `Variant` <br> A `Variant` can also represent a Marker </td></tr>
</table>


 

+ Parameters
    + searchResultsDbId (Required, string) ... Unique identifier which references the search results
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "linkageGroupName": "Chromosome 3",
                "mapDbId": "3d52bdf3",
                "mapName": "Genome Map 1",
                "position": 2390,
                "variantDbId": "a1eb250a",
                "variantName": "Marker_2390"
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

