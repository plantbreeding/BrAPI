FORMAT: 1A

# BrAPI Genotyping

The Breeding API (BrAPI) is a Standardized RESTful Web Service API Specification for communicating Plant Breeding Data. BrAPI allows for easy data sharing between databases and tools involved in plant breeding.

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


### BrAPI Phenotyping
The BrAPI Phenotyping module contains entities related to phenotypic observations. This includes Observation Units, Observations, Observation Variables, Traits, Scales, Methods, and Images

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Phenotyping) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Phenotyping) - [Apiary](https://brapiphenotyping.docs.apiary.io)


### **BrAPI Genotyping**
The **BrAPI Genotyping** module contains entities related to genotyping analysis. This includes Samples, Markers, Variant Sets, Variants, Call Sets, Calls, References, Reads, and Vendor Orders

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Genotyping) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Genotyping) - [Apiary](https://brapigenotyping.docs.apiary.io)


### BrAPI Germplasm
The BrAPI Germplasm module contains entities related to germplasm management. This includes Germplasm, Germplasm Attributes, Seed Lots, Crosses, Pedigree, and Progeny

V2.0 - [GitHub](https://github.com/plantbreeding/API/tree/brapi-v2-dev/Specification/BrAPI-Germplasm) - [SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Germplasm) - [Apiary](https://brapigermplasm.docs.apiary.io)


# Group CallSets





### Get - /callsets [GET /brapi/v1/callsets{?callSetDbId}{?callSetName}{?variantSetDbId}{?sampleDbId}{?germplasmDbId}{?page}{?pageSize}]

 Gets a filtered list of `CallSet` JSON objects.
Also See:
`GET /variantsets/{variantsetsDbId}/callsets` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|callSetName|string|The call set name.|
|created|string (int64)|The date this call set was created in milliseconds from the epoch.|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|updated|string (int64)|The time at which this call set was last updated in milliseconds from the epoch.|
|variantSetIds|array[string]|The IDs of the variant sets this call set has calls in.|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + callSetName (Optional, ) ... The human readbale name of the `CallSet` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
    + sampleDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
    + germplasmDbId (Optional, ) ... Return only call sets generated from the Sample of this Germplasm
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "created": "",
                "sampleDbId": "sampleDbId",
                "studyDbId": "studyDbId",
                "updated": "",
                "variantSetIds": [
                    "variantSetIds1",
                    "variantSetIds2"
                ]
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




### Get - /callsets/{callSetDbId} [GET /brapi/v1/callsets/{callSetDbId}]

`GET /callsets/{id}` will return a JSON version of `CallSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|callSetName|string|The call set name.|
|created|string (int64)|The date this call set was created in milliseconds from the epoch.|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|updated|string (int64)|The time at which this call set was last updated in milliseconds from the epoch.|
|variantSetIds|array[string]|The IDs of the variant sets this call set has calls in.|


 

+ Parameters
    + callSetDbId (Required, ) ... The ID of the `CallSet` to be retrieved.
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
        "callSetDbId": "callSetDbId",
        "callSetName": "callSetName",
        "created": "",
        "sampleDbId": "sampleDbId",
        "studyDbId": "studyDbId",
        "updated": "",
        "variantSetIds": [
            "variantSetIds1",
            "variantSetIds2"
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




### Get - /callsets/{callSetDbId}/calls [GET /brapi/v1/callsets/{callSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

 Gets a list of `Calls` associated with a `CallSet`.
Also See:
`GET /calls?callSetDbId={callSetDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + callSetDbId (Required, ) ... The ID of the `CallSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseset": "phaseset",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "sepPhased": "sepPhased",
        "sepUnphased": "sepUnphased",
        "unknownString": "unknownString"
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




### Post - /search/callsets [POST /brapi/v1/search/callsets]

`POST /callsets/search` must accept a JSON version of
`SearchCallSetsRequest` as the post body and will return a JSON version of
`SearchCallSetsResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|Only return call sets with these DbIds (case-sensitive, exact match).|
|callSetNames|array[string]|Only return call sets with these names (case-sensitive, exact match).|
|germplasmDbIds|array[string]|Return only call sets generated from the Sample of this germplasm|
|germplasmNames|array[string]|Return only call sets generated from the Sample of this germplasm|
|sampleDbIds|array[string]|Return only call sets generated from the provided Biosample ID.|
|sampleNames|array[string]|Return only call sets generated from the provided Biosample ID.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "callSetDbIds1",
        "callSetDbIds2"
    ],
    "callSetNames": [
        "callSetNames1",
        "callSetNames2"
    ],
    "germplasmDbIds": [
        "germplasmDbIds1",
        "germplasmDbIds2"
    ],
    "germplasmNames": [
        "germplasmNames1",
        "germplasmNames2"
    ],
    "sampleDbIds": [
        "sampleDbIds1",
        "sampleDbIds2"
    ],
    "sampleNames": [
        "sampleNames1",
        "sampleNames2"
    ],
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
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




### Get - /search/callsets/{searchResultsDbId} [GET /brapi/v1/search/callsets/{searchResultsDbId}{?page}{?pageSize}]

`POST /callsets/search` must accept a JSON version of
`SearchCallSetsRequest` as the post body and will return a JSON version of
`SearchCallSetsResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|callSetName|string|The call set name.|
|created|string (int64)|The date this call set was created in milliseconds from the epoch.|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|updated|string (int64)|The time at which this call set was last updated in milliseconds from the epoch.|
|variantSetIds|array[string]|The IDs of the variant sets this call set has calls in.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "created": "",
                "sampleDbId": "sampleDbId",
                "studyDbId": "studyDbId",
                "updated": "",
                "variantSetIds": [
                    "variantSetIds1",
                    "variantSetIds2"
                ]
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

# Group Calls





### Get - /calls [GET /brapi/v1/calls{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

 `GET /call` will return a filtered list of `Call` JSON objects.
Also See:
`GET /callsets/{callsetsDbId}/calls`
`GET /variants/{variantsDbId}/calls`
`GET /variantsets/{variantsetsDbId}/calls` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseset": "phaseset",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "sepPhased": "sepPhased",
        "sepUnphased": "sepUnphased",
        "unknownString": "unknownString"
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




### Post - /search/calls [POST /brapi/v1/search/calls]

`GET /callsets/{id}` will return a JSON version of `CallSet`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "callSetDbIds1",
        "callSetDbIds2"
    ],
    "sepPhased": "sepPhased",
    "sepUnphased": "sepUnphased",
    "unknownString": "unknownString",
    "variantDbIds": [
        "variantDbIds1",
        "variantDbIds2"
    ],
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
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




### Get - /search/calls/{searchResultsDbId} [GET /brapi/v1/search/calls/{searchResultsDbId}{?page}{?pageSize}]

Returns a filtered list of `Call` JSON objects.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseset": "phaseset",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "sepPhased": "sepPhased",
        "sepUnphased": "sepUnphased",
        "unknownString": "unknownString"
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


# Group Genome Maps

Retrieving genetic or physical maps
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome





### Get - /maps [GET /brapi/v1/maps{?commonCropName}{?scientificName}{?type}{?programDbId}{?trialDbId}{?studyDbId}{?page}{?pageSize}]

Get list of maps



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop, found from "GET /commoncropnames"|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer (int32)|The number of linkage groups present in this genome map|
|mapDbId|string|The ID which uniquely identifies this genome map|
|mapName|string|A human readable name for this genome map|
|markerCount|integer (int32)|The number of markers present in this genome map|
|publishedDate|string (date)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|type|string|The type of map this represents, ussually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

+ Parameters
    + commonCropName (Optional, ) ... The common name of the crop, found from "GET /commoncropnames"
    + scientificName (Optional, ) ... Full scientific binomial format name. This includes Genus, Species, and Sub-species
    + type (Optional, ) ... Type of map
    + programDbId (Optional, ) ... Unique Id to filter by Program
    + trialDbId (Optional, ) ... Unique Id to filter by Trial
    + studyDbId (Optional, ) ... Unique Id to filter by Study
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": {
        "description": "The JSON-LD Context is used to provide JSON-LD definitions to each field in a JSON object. By providing an array of context file urls, a BrAPI response object becomes JSON-LD compatible.  \n\nFor more information, see https://w3c.github.io/json-ld-syntax/#the-context",
        "example": [
            "https://brapi.org/jsonld/context/metadata.jsonld"
        ],
        "items": {
            "format": "uri",
            "type": "string"
        },
        "title": "context",
        "type": "array"
    },
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
                "comments": "comments",
                "commonCropName": "Paw Paw",
                "documentationURL": "https://brapi.org",
                "linkageGroupCount": 1,
                "mapDbId": "gm1",
                "mapName": "Genome Map 1",
                "markerCount": 11,
                "name": "Genome Map 1",
                "publishedDate": "2018-01-01",
                "scientificName": "Asimina triloba",
                "species": "triloba",
                "type": "Genetic",
                "unit": "cM"
            },
            {
                "comments": "comments",
                "commonCropName": "Paw Paw",
                "documentationURL": "https://brapi.org",
                "linkageGroupCount": 2,
                "mapDbId": "gm2",
                "mapName": "Genome Map 2",
                "markerCount": 11,
                "name": "Genome Map 2",
                "publishedDate": "2018-01-01",
                "scientificName": "Asimina triloba",
                "species": "triloba",
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




### Get - /maps/{mapDbId} [GET /brapi/v1/maps/{mapDbId}{?page}{?pageSize}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop, found from "GET /commoncropnames"|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer (int32)|The number of linkage groups present in this genome map|
|mapDbId|string|The ID which uniquely identifies this genome map|
|mapName|string|A human readable name for this genome map|
|markerCount|integer (int32)|The number of markers present in this genome map|
|publishedDate|string (date)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|type|string|The type of map this represents, ussually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": {
        "description": "The JSON-LD Context is used to provide JSON-LD definitions to each field in a JSON object. By providing an array of context file urls, a BrAPI response object becomes JSON-LD compatible.  \n\nFor more information, see https://w3c.github.io/json-ld-syntax/#the-context",
        "example": [
            "https://brapi.org/jsonld/context/metadata.jsonld"
        ],
        "items": {
            "format": "uri",
            "type": "string"
        },
        "title": "context",
        "type": "array"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "documentationURL": "https://brapi.org",
        "mapDbId": "gm1",
        "mapName": "Genome Map 1",
        "name": "Genome Map 1",
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




### Get - /maps/{mapDbId}/linkagegroups [GET /brapi/v1/maps/{mapDbId}/linkagegroups{?page}{?pageSize}]

Get the Linkage Groups of a specific Genomic Map. A Linkage Group is the BrAPI generic term for a named section of a map. A Linkage Group can represent a Chromosome, Scaffold, or Linkage Group.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|markerCount|integer|The number of markers associated with this linkage group|
|maxPosition|integer|The maximum position of a marker within this linkage group|


 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": {
        "description": "The JSON-LD Context is used to provide JSON-LD definitions to each field in a JSON object. By providing an array of context file urls, a BrAPI response object becomes JSON-LD compatible.  \n\nFor more information, see https://w3c.github.io/json-ld-syntax/#the-context",
        "example": [
            "https://brapi.org/jsonld/context/metadata.jsonld"
        ],
        "items": {
            "format": "uri",
            "type": "string"
        },
        "title": "context",
        "type": "array"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "data": []
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




### Get - /markerpositions [GET /brapi/v1/markerpositions{?mapDbId}{?linkageGroupName}{?markerDbId}{?minPosition}{?maxPosition}{?page}{?pageSize}]

Get marker position information, based on Map, Linkage Group, and Marker ID



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readbale name of the map|
|markerDbId|string|Internal db identifier|
|markerName|string|The human readable name for a marker|
|position|integer|The position of a marker within a linkage group|


 

+ Parameters
    + mapDbId (Optional, ) ... unique id of a map
    + linkageGroupName (Optional, ) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + markerDbId (Optional, ) ... The unique id for a marker
    + minPosition (Optional, ) ... The minimum position
    + maxPosition (Optional, ) ... The maximum position
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": {
        "description": "The JSON-LD Context is used to provide JSON-LD definitions to each field in a JSON object. By providing an array of context file urls, a BrAPI response object becomes JSON-LD compatible.  \n\nFor more information, see https://w3c.github.io/json-ld-syntax/#the-context",
        "example": [
            "https://brapi.org/jsonld/context/metadata.jsonld"
        ],
        "items": {
            "format": "uri",
            "type": "string"
        },
        "title": "context",
        "type": "array"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "data": []
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




### Post - /search/markerpositions [POST /brapi/v1/search/markerpositions]

Get marker position information, based on Map, Linkage Group, and Marker ID

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|linkageGroupNames|array[string]|The Uniquely Identifiable name of this linkage group|
|mapDbIds|array[string]|The unique ID of the map|
|markerDbIds|array[string]|Internal db identifier|
|maxPosition|integer|The maximum position|
|minPosition|integer|The minimum position|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "linkageGroupNames": [
        "linkageGroupNames1",
        "linkageGroupNames2"
    ],
    "mapDbIds": [
        "mapDbIds1",
        "mapDbIds2"
    ],
    "markerDbIds": [
        "markerDbIds1",
        "markerDbIds2"
    ],
    "maxPosition": 0,
    "minPosition": 0
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




### Post - /search/markerpositions/{searchResultsDbId} [POST /brapi/v1/search/markerpositions/{searchResultsDbId}{?page}{?pageSize}]

Get marker position information, based on Map, Linkage Group, and Marker ID



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readbale name of the map|
|markerDbId|string|Internal db identifier|
|markerName|string|The human readable name for a marker|
|position|integer|The position of a marker within a linkage group|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": {
        "description": "The JSON-LD Context is used to provide JSON-LD definitions to each field in a JSON object. By providing an array of context file urls, a BrAPI response object becomes JSON-LD compatible.  \n\nFor more information, see https://w3c.github.io/json-ld-syntax/#the-context",
        "example": [
            "https://brapi.org/jsonld/context/metadata.jsonld"
        ],
        "items": {
            "format": "uri",
            "type": "string"
        },
        "title": "context",
        "type": "array"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "data": []
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

# Group References





### Get - /references [GET /brapi/v1/references{?referenceDbId}{?referenceSetDbId}{?accession}{?md5checksum}{?isDerived}{?minLength}{?maxLength}{?page}{?pageSize}]

`GET /references` will return a filtered list of `Reference` JSON objects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|string (int64)|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The reference ID. Unique within the repository.|
|referenceName|string|The unique name of this reference within the Reference Set (e.g. '22').|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object||
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + referenceDbId (Optional, ) ... The ID of the `Refernce` to be retrieved.
    + referenceSetDbId (Optional, ) ... The ID of the `RefernceSet` to be retrieved.
    + accession (Optional, ) ... If unset, return the reference sets for which the `accession`matches this string (case-sensitive, exact match).
    + md5checksum (Optional, ) ... If specified, return the references for which the`md5checksum` matches this string (case-sensitive, exact match).See `Reference::md5checksum` for details.
    + isDerived (Optional, ) ... If the reference is derived from a source sequence
    + minLength (Optional, ) ... The minimum length of the reference sequences to be retrieved.
    + maxLength (Optional, ) ... The maximum length of the reference sequences to be retrieved.
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
                "length": "",
                "md5checksum": "md5checksum",
                "referenceDbId": "referenceDbId",
                "referenceName": "referenceName",
                "sourceAccessions": [
                    "sourceAccessions1",
                    "sourceAccessions2"
                ],
                "sourceURI": "sourceURI",
                "species": {
                    "term": "term",
                    "termURI": "termURI"
                }
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




### Get - /references/{referenceDbId} [GET /brapi/v1/references/{referenceDbId}]

`GET /references/{reference_id}` will return a JSON version of
`Reference`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|string (int64)|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The reference ID. Unique within the repository.|
|referenceName|string|The unique name of this reference within the Reference Set (e.g. '22').|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object||
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + referenceDbId (Required, ) ... The ID of the `Reference` to be retrieved.




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
        "length": "",
        "md5checksum": "md5checksum",
        "referenceDbId": "referenceDbId",
        "referenceName": "referenceName",
        "sourceAccessions": [
            "sourceAccessions1",
            "sourceAccessions2"
        ],
        "sourceURI": "sourceURI",
        "species": {
            "term": "term",
            "termURI": "termURI"
        }
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




### Get - /references/{referenceDbId}/bases [GET /brapi/v1/references/{referenceDbId}/bases{?start}{?end}{?pageToken}]

`POST /listreferencebases` will return a JSON version of
`ListReferenceBasesResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|nextPageToken|string|The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. This field will be empty if there aren't any additional results.|
|offset|string (int64)|The offset position (0-based) of the given sequence from the start of this `Reference`. This value will differ for each page in a paginated request.|
|sequence|string|A substring of the bases that make up this reference. Bases are represented as IUPAC-IUB codes; this string matches the regexp `[ACGTMRWSYKVHDBN]*`.|


 

+ Parameters
    + referenceDbId (Required, ) ... The ID of the `Reference` to be retrieved.
    + start (Optional, ) ... The start position (0-based) of this query. Defaults to 0.Genomic positions are non-negative integers less than reference length.Requests spanning the join of circular genomes are represented astwo requests one on each side of the join (position 0).
    + end (Optional, ) ... The end position (0-based, exclusive) of this query. Defaults to the length of this `Reference`.
    + pageToken (Optional, ) ... The continuation token, which is used to page through large result sets.To get the next page of results, set this parameter to the value of`next_page_token` from the previous response.
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
        "nextPageToken": "nextPageToken",
        "offset": "",
        "sequence": "sequence"
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




### Get - /referencesets [GET /brapi/v1/referencesets{?referenceSetDbId}{?accession}{?assemblyPUI}{?md5checksum}{?page}{?pageSize}]

`GET /referencesets/{reference_set_id}` will return a JSON version of
`ReferenceSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|assemblyPUI|string|The remaining information is about the source of the sequences Public id of this reference set, such as `GRCh37`.|
|description|string|Optional free text description of this reference set.|
|isDerived|boolean (boolean)|A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).|
|md5checksum|string|Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.|
|referenceSetDbId|string|The reference set ID. Unique in the repository.|
|referenceSetName|string|The reference set name.|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.|
|sourceURI|string|Specifies a FASTA format file/string.|
|species|object||
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + referenceSetDbId (Optional, ) ... The ID of the `ReferenceSet` to be retrieved.
    + accession (Optional, ) ... If unset, return the reference sets for which the `accession`matches this string (case-sensitive, exact match).
    + assemblyPUI (Optional, ) ... If unset, return the reference sets for which the `assemblyId`matches this string (case-sensitive, exact match).
    + md5checksum (Optional, ) ... If unset, return the reference sets for which the`md5checksum` matches this string (case-sensitive, exact match).See `ReferenceSet::md5checksum` for details.
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
                "assemblyPUI": "assemblyPUI",
                "description": "description",
                "md5checksum": "md5checksum",
                "referenceSetDbId": "referenceSetDbId",
                "referenceSetName": "referenceSetName",
                "sourceAccessions": [
                    "sourceAccessions1",
                    "sourceAccessions2"
                ],
                "sourceURI": "sourceURI",
                "species": {
                    "term": "term",
                    "termURI": "termURI"
                }
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




### Get - /referencesets/{referenceSetDbId} [GET /brapi/v1/referencesets/{referenceSetDbId}]

`GET /referencesets/{reference_set_id}` will return a JSON version of
`ReferenceSet`.





 

+ Parameters
    + referenceSetDbId (Required, ) ... The ID of the `ReferenceSet` to be retrieved.




+ Response 200 (application/json)
```
{
    "additionalInfo": {},
    "assemblyPUI": "assemblyPUI",
    "description": "description",
    "md5checksum": "md5checksum",
    "referenceSetDbId": "referenceSetDbId",
    "referenceSetName": "referenceSetName",
    "sourceAccessions": [
        "sourceAccessions1",
        "sourceAccessions2"
    ],
    "sourceURI": "sourceURI",
    "species": {
        "term": "term",
        "termURI": "termURI"
    }
}
```




### Post - /search/references [POST /brapi/v1/search/references]

`POST /references/search` must accept a JSON version of
`SearchReferencesRequest` as the post body and will return a JSON
version of `SearchReferencesResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accession|string|If specified, return the references for which the `accession` matches this string (case-sensitive, exact match).|
|md5checksum|string|If specified, return the references for which the `md5checksum` matches this string (case-sensitive, exact match). See `ReferenceSet::md5checksum` for details.|
|page_size|integer (int32)|Specifies the maximum number of results to return in a single page. If unspecified, a system default will be used.|
|page_token|string|The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of `next_page_token` from the previous response.|
|referenceSetDbId|string|The `ReferenceSet` to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accession": "accession",
    "md5checksum": "md5checksum",
    "page_size": 0,
    "page_token": "page_token",
    "referenceSetDbId": "referenceSetDbId"
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




### Get - /search/references/{searchResultsDbId} [GET /brapi/v1/search/references/{searchResultsDbId}{?page}{?pageSize}]

`POST /references/search` must accept a JSON version of
`SearchReferencesRequest` as the post body and will return a JSON
version of `SearchReferencesResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|string (int64)|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The reference ID. Unique within the repository.|
|referenceName|string|The unique name of this reference within the Reference Set (e.g. '22').|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object||
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "length": "",
                "md5checksum": "md5checksum",
                "referenceDbId": "referenceDbId",
                "referenceName": "referenceName",
                "sourceAccessions": [
                    "sourceAccessions1",
                    "sourceAccessions2"
                ],
                "sourceURI": "sourceURI",
                "species": {
                    "term": "term",
                    "termURI": "termURI"
                }
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




### Post - /search/referencesets [POST /brapi/v1/search/referencesets]

`POST /referencesets/search` must accept a JSON version of
`SearchReferenceSetsRequest` as the post body and will return a JSON
version of `SearchReferenceSetsResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accession|string|If unset, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).|
|assemblyPUI|string|If unset, return the reference sets for which the `assemblyId` matches this string (case-sensitive, exact match).|
|md5checksum|string|If unset, return the reference sets for which the `md5checksum` matches this string (case-sensitive, exact match). See `ReferenceSet::md5checksum` for details.|
|page_size|integer (int32)|Specifies the maximum number of results to return in a single page. If unspecified, a system default will be used.|
|page_token|string|The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of `next_page_token` from the previous response.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accession": "accession",
    "assemblyPUI": "assemblyPUI",
    "md5checksum": "md5checksum",
    "page_size": 0,
    "page_token": "page_token"
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




### Get - /search/referencesets/{searchResultsDbId} [GET /brapi/v1/search/referencesets/{searchResultsDbId}{?page}{?pageSize}]

`POST /referencesets/search` must accept a JSON version of
`SearchReferenceSetsRequest` as the post body and will return a JSON
version of `SearchReferenceSetsResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|assemblyPUI|string|The remaining information is about the source of the sequences Public id of this reference set, such as `GRCh37`.|
|description|string|Optional free text description of this reference set.|
|isDerived|boolean (boolean)|A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).|
|md5checksum|string|Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.|
|referenceSetDbId|string|The reference set ID. Unique in the repository.|
|referenceSetName|string|The reference set name.|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.|
|sourceURI|string|Specifies a FASTA format file/string.|
|species|object||
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "assemblyPUI": "assemblyPUI",
                "description": "description",
                "md5checksum": "md5checksum",
                "referenceSetDbId": "referenceSetDbId",
                "referenceSetName": "referenceSetName",
                "sourceAccessions": [
                    "sourceAccessions1",
                    "sourceAccessions2"
                ],
                "sourceURI": "sourceURI",
                "species": {
                    "term": "term",
                    "termURI": "termURI"
                }
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


# Group Samples

API methods for tracking/managing plant samples and related meta-data. A 'Sample' in the context of BrAPI, is defined as the actual biological plant material collected from the field.





### Get - /samples [GET /brapi/v1/samples{?sampleDbId}{?observationUnitDbId}{?plateDbId}{?germplasmDbId}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + sampleDbId (Optional, ) ... the internal DB id for a sample
    + observationUnitDbId (Optional, ) ... the internal DB id for an observation unit where a sample was taken from
    + plateDbId (Optional, ) ... the internal DB id for a plate of samples
    + germplasmDbId (Optional, ) ... the internal DB id for a germplasm
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
                "column": 6,
                "germplasmDbId": "7e08d538",
                "notes": "This sample was taken from the root of a tree",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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




### Post - /samples [POST /brapi/v1/samples]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "column": 6,
        "germplasmDbId": "7e08d538",
        "notes": "This sample was taken from the root of a tree",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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
                "column": 6,
                "germplasmDbId": "7e08d538",
                "notes": "This sample was taken from the root of a tree",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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




### Get - /samples/{sampleDbId} [GET /brapi/v1/samples/{sampleDbId}]

Used to retrieve the details of a single Sample from a Sample Tracking system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
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
        "column": 6,
        "germplasmDbId": "7e08d538",
        "notes": "This sample was taken from the root of a tree",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDbId": "cd06a61d",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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




### Put - /samples/{sampleDbId} [PUT /brapi/v1/samples/{sampleDbId}]

Update the details of an existing Sample

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "column": 6,
    "germplasmDbId": "7e08d538",
    "notes": "This sample was taken from the root of a tree",
    "observationUnitDbId": "073a3ce5",
    "plateDbId": "2dce16d1",
    "plateName": "Plate_alpha_20191022",
    "programDbId": "bd748e00",
    "row": "B",
    "sampleBarcode": "3a027b59",
    "sampleGroupDbId": "8524b436",
    "sampleName": "Sample_alpha_20191022",
    "samplePUI": "doi:10.15454/312953986E3",
    "sampleTimestamp": "2018-01-01T14:47:23-0600",
    "sampleType": "Tissue",
    "studyDbId": "64bd6bf9",
    "takenBy": "Bob",
    "tissueType": "Root",
    "trialDbId": "d34c5349",
    "well": "B6"
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
        "column": 6,
        "germplasmDbId": "7e08d538",
        "notes": "This sample was taken from the root of a tree",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDbId": "cd06a61d",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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




### Post - /search/samples [POST /brapi/v1/search/samples]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]| The ID which uniquely identifies a germplasm|
|observationUnitDbIds|array[string]|The ID which uniquely identifies an observation unit|
|plateDbIds|array[string]|The ID which uniquely identifies a plate of samples|
|sampleDbIds|array[string]|The ID which uniquely identifies a sample|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds1",
        "germplasmDbIds2"
    ],
    "observationUnitDbIds": [
        "observationUnitDbIds1",
        "observationUnitDbIds2"
    ],
    "plateDbIds": [
        "plateDbIds1",
        "plateDbIds2"
    ],
    "sampleDbIds": [
        "sampleDbIds1",
        "sampleDbIds2"
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




### Get - /search/samples/{searchResultsDbId} [GET /brapi/v1/search/samples/{searchResultsDbId}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|column|integer|The Column identifier for this samples location in the plate|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a sample|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateName|string|The human readable name of a plate|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|row|string|The Row identifier for this samples location in the plate|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|sampleName|string|The name of the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "column": 6,
                "germplasmDbId": "7e08d538",
                "notes": "This sample was taken from the root of a tree",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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

# Group VariantSets





### Post - /search/variantsets [POST /brapi/v1/search/variantsets]

`POST /variantsets/search` must accept a JSON version of
`SearchVariantSetsRequest` as the post body and will return a JSON version
of `SearchVariantSetsResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|studyDbIds|array[string]|The `Dataset` to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "studyDbIds": [
        "studyDbIds1",
        "studyDbIds2"
    ],
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
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




### Get - /search/variantsets/{searchResultsDbId} [GET /brapi/v1/search/variantsets/{searchResultsDbId}{?page}{?pageSize}]

`POST /variantsets/search` must accept a JSON version of
`SearchVariantSetsRequest` as the post body and will return a JSON version
of `SearchVariantSetsResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "analysis": [
                    {
                        "analysisDbId": "analysisDbId",
                        "analysisName": "analysisName",
                        "created": "created",
                        "description": "description",
                        "software": [
                            "software1",
                            "software2"
                        ],
                        "type": "type",
                        "updated": "updated"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": ""
                    }
                ],
                "callSetCount": 0,
                "referenceSetDbId": "referenceSetDbId",
                "studyDbId": "studyDbId",
                "variantCount": 0,
                "variantSetDbId": "variantSetDbId",
                "variantSetName": "variantSetName"
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




### Get - /variantsets [GET /brapi/v1/variantsets{?variantSetDbId}{?page}{?pageSize}]

`GET /variantsets` will return a filtered list of `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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
                "analysis": [
                    {
                        "analysisDbId": "analysisDbId",
                        "analysisName": "analysisName",
                        "created": "created",
                        "description": "description",
                        "software": [
                            "software1",
                            "software2"
                        ],
                        "type": "type",
                        "updated": "updated"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": ""
                    }
                ],
                "callSetCount": 0,
                "referenceSetDbId": "referenceSetDbId",
                "studyDbId": "studyDbId",
                "variantCount": 0,
                "variantSetDbId": "variantSetDbId",
                "variantSetName": "variantSetName"
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




### Post - /variantsets/extract [POST /brapi/v1/variantsets/extract]

`POST /variantsets/extract` will perform a search for `Calls` which match the search criteria in `variantSetsExtractRequest`
The results of the search will be used to create a new `VariantSet` on the server. The new `VariantSet` will be returned.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "callSetDbIds1",
        "callSetDbIds2"
    ],
    "sepPhased": "sepPhased",
    "sepUnphased": "sepUnphased",
    "unknownString": "unknownString",
    "variantDbIds": [
        "variantDbIds1",
        "variantDbIds2"
    ],
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
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
        "analysis": [
            {
                "analysisDbId": "analysisDbId",
                "analysisName": "analysisName",
                "created": "created",
                "description": "description",
                "software": [
                    "software1",
                    "software2"
                ],
                "type": "type",
                "updated": "updated"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": [
                    "DartSeq",
                    "VCF",
                    "Hapmap",
                    "tabular",
                    "JSON"
                ],
                "fileFormat": [
                    "text/csv",
                    "text/tsv",
                    "application/excel",
                    "application/zip",
                    "application/json"
                ],
                "fileURL": ""
            }
        ],
        "callSetCount": 0,
        "referenceSetDbId": "referenceSetDbId",
        "studyDbId": "studyDbId",
        "variantCount": 0,
        "variantSetDbId": "variantSetDbId",
        "variantSetName": "variantSetName"
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




### Get - /variantsets/{variantSetDbId} [GET /brapi/v1/variantsets/{variantSetDbId}]

`GET /variantsets/{variantSetDbId}` will return a JSON version of
`VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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
        "analysis": [
            {
                "analysisDbId": "analysisDbId",
                "analysisName": "analysisName",
                "created": "created",
                "description": "description",
                "software": [
                    "software1",
                    "software2"
                ],
                "type": "type",
                "updated": "updated"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": [
                    "DartSeq",
                    "VCF",
                    "Hapmap",
                    "tabular",
                    "JSON"
                ],
                "fileFormat": [
                    "text/csv",
                    "text/tsv",
                    "application/excel",
                    "application/zip",
                    "application/json"
                ],
                "fileURL": ""
            }
        ],
        "callSetCount": 0,
        "referenceSetDbId": "referenceSetDbId",
        "studyDbId": "studyDbId",
        "variantCount": 0,
        "variantSetDbId": "variantSetDbId",
        "variantSetName": "variantSetName"
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




### Get - /variantsets/{variantSetDbId}/calls [GET /brapi/v1/variantsets/{variantSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

 Gets a list of `Calls` associated with a `VariantSet`.
Also See:
`GET /calls?variantSetDbId={variantSetDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseset": "phaseset",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "sepPhased": "sepPhased",
        "sepUnphased": "sepUnphased",
        "unknownString": "unknownString"
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




### Get - /variantsets/{variantSetDbId}/callsets [GET /brapi/v1/variantsets/{variantSetDbId}/callsets{?callSetDbId}{?callSetName}{?page}{?pageSize}]

 Gets a list of `CallSets` associated with a `VariantSet`.
Also See:
`GET /callsets?variantSetDbId={variantSetDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|callSetName|string|The call set name.|
|created|string (int64)|The date this call set was created in milliseconds from the epoch.|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|updated|string (int64)|The time at which this call set was last updated in milliseconds from the epoch.|
|variantSetIds|array[string]|The IDs of the variant sets this call set has calls in.|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + callSetName (Optional, ) ... The human readbale name of the `CallSet` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "created": "",
                "sampleDbId": "sampleDbId",
                "studyDbId": "studyDbId",
                "updated": "",
                "variantSetIds": [
                    "variantSetIds1",
                    "variantSetIds2"
                ]
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




### Get - /variantsets/{variantSetDbId}/variants [GET /brapi/v1/variantsets/{variantSetDbId}/variants{?variantDbId}{?page}{?pageSize}]

`GET /variantsets/{variant_set_id}` will return a JSON version of
`VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]|Similar to "cipos", but for the variant's end position (which is derived from start + svlen).|
|cipos|array[integer]|In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCFv4.2|
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string|The reference on which this variant occurs. (e.g. `chr20` or `X`)|
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)|Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCFv4.2|
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|array[string]|An array of `VariantSet` IDs this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string|The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"; not necessarily in situ   DEL  : deletion of sequence following "start"|


 

+ Parameters
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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
                "alternate_bases": [
                    "alternate_bases1",
                    "alternate_bases2"
                ],
                "ciend": [
                    -1000,
                    0
                ],
                "cipos": [
                    -12000,
                    1000
                ],
                "created": "",
                "end": "",
                "filtersFailed": [
                    "filtersFailed1",
                    "filtersFailed2"
                ],
                "referenceBases": "referenceBases",
                "referenceName": "chr20",
                "start": "",
                "svlen": "",
                "updated": "",
                "variantDbId": "variantDbId",
                "variantNames": [
                    "variantNames1",
                    "variantNames2"
                ],
                "variantSetDbId": [
                    "variantSetDbId1",
                    "variantSetDbId2"
                ],
                "variantType": "DUP"
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

# Group Variants





### Post - /search/variants [POST /brapi/v1/search/variants]

`POST /variants/search` must accept a JSON version of
`SearchVariantsRequest` as the post body and will return a JSON version of
`SearchVariantsResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|Only return variant calls which belong to call sets with these IDs. If unspecified, return all variants and no variant call objects.|
|end|string (int64)|Required. The end of the window (0-based, exclusive) for which overlapping variants should be returned.|
|reference_name|string|Required. Only return variants on this reference.|
|start|string (int64)|Required. The beginning of the window (0-based, inclusive) for which overlapping variants should be returned. Genomic positions are non-negative integers less than reference length. Requests spanning the join of circular genomes are represented as two requests one on each side of the join (position 0).|
|variantSetDbIds|array[string]|The `VariantSet` to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultsDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "callSetDbIds1",
        "callSetDbIds2"
    ],
    "end": "",
    "reference_name": "reference_name",
    "start": "",
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
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




### Get - /search/variants/{searchResultsDbId} [GET /brapi/v1/search/variants/{searchResultsDbId}{?page}{?pageSize}]

`POST /variants/search` must accept a JSON version of
`SearchVariantsRequest` as the post body and will return a JSON version of
`SearchVariantsResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]|Similar to "cipos", but for the variant's end position (which is derived from start + svlen).|
|cipos|array[integer]|In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCFv4.2|
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string|The reference on which this variant occurs. (e.g. `chr20` or `X`)|
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)|Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCFv4.2|
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|array[string]|An array of `VariantSet` IDs this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string|The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"; not necessarily in situ   DEL  : deletion of sequence following "start"|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "alternate_bases": [
                    "alternate_bases1",
                    "alternate_bases2"
                ],
                "ciend": [
                    -1000,
                    0
                ],
                "cipos": [
                    -12000,
                    1000
                ],
                "created": "",
                "end": "",
                "filtersFailed": [
                    "filtersFailed1",
                    "filtersFailed2"
                ],
                "referenceBases": "referenceBases",
                "referenceName": "chr20",
                "start": "",
                "svlen": "",
                "updated": "",
                "variantDbId": "variantDbId",
                "variantNames": [
                    "variantNames1",
                    "variantNames2"
                ],
                "variantSetDbId": [
                    "variantSetDbId1",
                    "variantSetDbId2"
                ],
                "variantType": "DUP"
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




### Get - /variants [GET /brapi/v1/variants{?variantDbId}{?variantSetDbId}{?page}{?pageSize}]

`GET /variants` will return a filtered list of `Variants`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]|Similar to "cipos", but for the variant's end position (which is derived from start + svlen).|
|cipos|array[integer]|In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCFv4.2|
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string|The reference on which this variant occurs. (e.g. `chr20` or `X`)|
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)|Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCFv4.2|
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|array[string]|An array of `VariantSet` IDs this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string|The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"; not necessarily in situ   DEL  : deletion of sequence following "start"|


 

+ Parameters
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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
                "alternate_bases": [
                    "alternate_bases1",
                    "alternate_bases2"
                ],
                "ciend": [
                    -1000,
                    0
                ],
                "cipos": [
                    -12000,
                    1000
                ],
                "created": "",
                "end": "",
                "filtersFailed": [
                    "filtersFailed1",
                    "filtersFailed2"
                ],
                "referenceBases": "referenceBases",
                "referenceName": "chr20",
                "start": "",
                "svlen": "",
                "updated": "",
                "variantDbId": "variantDbId",
                "variantNames": [
                    "variantNames1",
                    "variantNames2"
                ],
                "variantSetDbId": [
                    "variantSetDbId1",
                    "variantSetDbId2"
                ],
                "variantType": "DUP"
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




### Get - /variants/{variantDbId} [GET /brapi/v1/variants/{variantDbId}]

`GET /variants/{id}` will return a JSON version of `Variant`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]|Similar to "cipos", but for the variant's end position (which is derived from start + svlen).|
|cipos|array[integer]|In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCFv4.2|
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string|The reference on which this variant occurs. (e.g. `chr20` or `X`)|
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)|Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCFv4.2|
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|array[string]|An array of `VariantSet` IDs this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string|The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"; not necessarily in situ   DEL  : deletion of sequence following "start"|


 

+ Parameters
    + variantDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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
        "alternate_bases": [
            "alternate_bases1",
            "alternate_bases2"
        ],
        "ciend": [
            -1000,
            0
        ],
        "cipos": [
            -12000,
            1000
        ],
        "created": "",
        "end": "",
        "filtersFailed": [
            "filtersFailed1",
            "filtersFailed2"
        ],
        "referenceBases": "referenceBases",
        "referenceName": "chr20",
        "start": "",
        "svlen": "",
        "updated": "",
        "variantDbId": "variantDbId",
        "variantNames": [
            "variantNames1",
            "variantNames2"
        ],
        "variantSetDbId": [
            "variantSetDbId1",
            "variantSetDbId2"
        ],
        "variantType": "DUP"
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




### Get - /variants/{variantDbId}/calls [GET /brapi/v1/variants/{variantDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

 The variant calls for this particular variant. Each one represents the determination of genotype with respect to this variant. `Call`s in this array are implicitly associated with this `Variant`.
Also See:
`GET /calls?variantDbId={variantDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + variantDbId (Required, ) ... The ID of the `Variant` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseset": "phaseset",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "sepPhased": "sepPhased",
        "sepUnphased": "sepUnphased",
        "unknownString": "unknownString"
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


# Group Vendor Samples

This interface is specific to facilities that performs an external analysis, such as genotyping facilities. The interface should be implemented by that facility's server. The breeding database is the client of this interface.

Note that to use these calls, you likely have to use the authentication call prior to connecting (see Authentication best practices).





### Get - /vendor/orders [GET /brapi/v1/vendor/orders{?orderId}{?submissionId}]

List current available orders



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the correct billing and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|orderId|string|The order id returned by the vendor when the order was successfully submitted.|
|requiredServiceInfo|object|A map of additional data required by the requested service. This includes things like Volume and Concentration.|
|serviceIds|array[string]|A list of unique, alpha-numeric ID which identify the requested services to be applied to this order.  A Vendor Service defines what platform, technology, and markers will be used.  A list of available service IDs can be retrieved from the Vendor Specs.|


 

+ Parameters
    + orderId (Optional, ) ... The order id returned by the vendor when the order was successfully submitted. From response of "POST /vendor/orders"
    + submissionId (Optional, ) ... The submission id returned by the vendor when a set of plates was successfully submitted. From response of "POST /vendor/plates"
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
                "clientId": "7b51ad15",
                "numberOfSamples": 180,
                "orderId": "96ba0ca3",
                "requiredServiceInfo": {
                    "extractDNA": true,
                    "genus": "Aedes",
                    "species": "vexans",
                    "volumePerWell": "2.3 ml"
                },
                "serviceIds": [
                    "e8f60f64",
                    "05bd925a",
                    "b698fb5e"
                ]
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




### Post - /vendor/orders [POST /brapi/v1/vendor/orders]

Submit a new order to a vendor

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|integer|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|
|requiredServiceInfo|object|A map of additional data required by the requested service. This includes things like Volume and Concentration.|
|sampleType|string|The type of Samples being submitted|
|serviceIds|array[string]|A list of unique, alpha-numeric ID which identify the requested services to be applied to this order.  A Vendor Service defines what platform, technology, and markers will be used.  A list of available service IDs can be retrieved from the Vendor Specs.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|orderId|string|A unique, alpha-numeric ID which identifies the order|
|shipmentForms|array[object]|Array of paper forms which need to be printed and included with the physical shipment|
|fileDescription|string|The human readable long description for this form|
|fileName|string|The human readable name for this form|
|fileURL|string (uri)|The URL to download this form|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "clientId": "b8aac350",
    "numberOfSamples": 180,
    "plates": [
        {
            "clientPlateBarcode": "6ebf3f25",
            "clientPlateId": "02a8d6f0",
            "sampleSubmissionFormat": "PLATE_96",
            "samples": [
                {
                    "clientSampleBarCode": "7c07e527",
                    "clientSampleId": "bd96bd69",
                    "column": 6,
                    "comments": "This is my favorite sample, please be extra careful with it.",
                    "concentration": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "organismName": "Aspergillus fructus",
                    "row": "B",
                    "speciesName": "Aspergillus fructus",
                    "taxonomyOntologyReference": {
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
                    "tissueType": "Root",
                    "tissueTypeOntologyReference": {
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
                    "volume": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "well": "B6"
                }
            ]
        }
    ],
    "requiredServiceInfo": {
        "extractDNA": true,
        "genus": "Aedes",
        "species": "vexans",
        "volumePerWell": "2.3 ml"
    },
    "sampleType": "Tissue",
    "serviceIds": [
        "e8f60f64",
        "05bd925a",
        "b698fb5e"
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
        "orderId": "b5144468",
        "shipmentForms": [
            {
                "fileDescription": "This is a shipment manifest form",
                "fileName": "Shipment Manifest",
                "fileURL": "https://vendor.org/forms/manifest.pdf"
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




### Get - /vendor/orders/{orderId}/plates [GET /brapi/v1/vendor/orders/{orderId}/plates]

Retrieve the plate and sample details of an order being processed



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|integer|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
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
                "clientPlateBarcode": "31dd5787",
                "clientPlateId": "0ad6c0ef",
                "sampleSubmissionFormat": "PLATE_96",
                "samples": [
                    {
                        "clientSampleBarCode": "7c07e527",
                        "clientSampleId": "bd96bd69",
                        "column": 6,
                        "comments": "This is my favorite sample, please be extra careful with it.",
                        "concentration": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "organismName": "Aspergillus fructus",
                        "row": "B",
                        "speciesName": "Aspergillus fructus",
                        "taxonomyOntologyReference": {
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
                        "tissueType": "Root",
                        "tissueTypeOntologyReference": {
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
                        "volume": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "well": "B6"
                    }
                ]
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




### Get - /vendor/orders/{orderId}/results [GET /brapi/v1/vendor/orders/{orderId}/results]

Retrieve the data files generated by the vendors analysis



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|clientSampleIds|array[string]|The list of sampleDbIds included in the file|
|fileName|string|Name of the file|
|fileType|string|Format of the file|
|fileURL|string (uri)|The URL to a file with the results of a vendor analysis|
|md5sum|string|MD5 Hash Check Sum for the file to confirm download without error|


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
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
                "clientSampleIds": [
                    "3968733e",
                    "e0de6391",
                    "66854172"
                ],
                "fileName": "sequence_data_ce640bd3.csv",
                "fileType": "text/csv",
                "fileURL": "https://vendor.org/data/sequence_data_ce640bd3.csv",
                "md5sum": "c2365e900c81a89cf74d83dab60df146"
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




### Get - /vendor/orders/{orderId}/status [GET /brapi/v1/vendor/orders/{orderId}/status]

Retrieve the current status of an order being processed



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|status|string||


 

+ Parameters
    + orderId (Required, ) ... The order id returned by the vendor when the order was successfully submitted.
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
        "status": [
            "registered",
            "received",
            "inProgress",
            "completed",
            "rejected"
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




### Post - /vendor/plates [POST /brapi/v1/vendor/plates]

Submit a new set of Sample data

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|integer|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|
|sampleType|string|The type of Samples being submitted|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|submissionId|string|A unique, alpha-numeric ID which identifies a set of plates which have been successfully submitted.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "clientId": "b8aac350",
    "numberOfSamples": 180,
    "plates": [
        {
            "clientPlateBarcode": "6ebf3f25",
            "clientPlateId": "02a8d6f0",
            "sampleSubmissionFormat": "PLATE_96",
            "samples": [
                {
                    "clientSampleBarCode": "7c07e527",
                    "clientSampleId": "bd96bd69",
                    "column": 6,
                    "comments": "This is my favorite sample, please be extra careful with it.",
                    "concentration": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "organismName": "Aspergillus fructus",
                    "row": "B",
                    "speciesName": "Aspergillus fructus",
                    "taxonomyOntologyReference": {
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
                    "tissueType": "Root",
                    "tissueTypeOntologyReference": {
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
                    "volume": {
                        "units": "ng/ul",
                        "value": 2.3
                    },
                    "well": "B6"
                }
            ]
        }
    ],
    "sampleType": "Tissue"
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
        "submissionId": "f8f409e0"
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




### Get - /vendor/plates/{submissionId} [GET /brapi/v1/vendor/plates/{submissionId}]

Get data for a submitted set of plates



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|clientId|string|A unique, alpha-numeric ID which identifies the client to the vendor. Used to connect the order to the contract, billing, and contact info.|
|numberOfSamples|integer|The total number of samples contained in this request. Used for billing and basic validation of the request.|
|plates|array[object]|Array of new plates to be submitted to a vendor|
|clientPlateBarcode|string|(Optional) The value of the bar code attached to this plate|
|clientPlateId|string|The ID which uniquely identifies this plate to the client making the request|
|sampleSubmissionFormat|string|Enum for plate formats, usually "PLATE_96" for a 96 well plate or "TUBES" for plateless format|
|samples|array[object]||
|clientSampleBarCode|string|(Optional) The value of the bar code attached to this sample|
|clientSampleId|string|The ID which uniquely identifies this sample to the client making the request|
|column|integer|The Column identifier for this samples location in the plate|
|comments|string|Generic comments about this sample for the vendor|
|concentration|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|organismName|string|Scientific organism name|
|row|string|The Row identifier for this samples location in the plate|
|speciesName|string|Scientific species name|
|taxonomyOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|tissueType|string|The type of tissue in this sample. List of accepted tissue types can be found in the Vendor Specs.|
|tissueTypeOntologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|volume|object|A value with units|
|units|string|Units (example: "ng/ul")|
|value|number|Value (example: "2.3")|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + submissionId (Required, ) ... 




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
        "clientId": "e470ae0d",
        "numberOfSamples": 180,
        "plates": [
            {
                "clientPlateBarcode": "bfb33593",
                "clientPlateId": "dae8f49d",
                "sampleSubmissionFormat": "PLATE_96",
                "samples": [
                    {
                        "clientSampleBarCode": "7c07e527",
                        "clientSampleId": "bd96bd69",
                        "column": 6,
                        "comments": "This is my favorite sample, please be extra careful with it.",
                        "concentration": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "organismName": "Aspergillus fructus",
                        "row": "B",
                        "speciesName": "Aspergillus fructus",
                        "taxonomyOntologyReference": {
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
                        "tissueType": "Root",
                        "tissueTypeOntologyReference": {
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
                        "volume": {
                            "units": "ng/ul",
                            "value": 2.3
                        },
                        "well": "B6"
                    }
                ]
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




### Get - /vendor/specifications [GET /brapi/v1/vendor/specifications]

Defines the plate format specification for the vendor.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary information specific to a particular Vendor. Look for the Vedors specific API documentation for more details|
|services|array[object]|List of platform specifications available at the vendor|
|serviceDescription|string|Description of the vendor platform|
|serviceId|string|Unique identifier for this service|
|serviceName|string|The human readable name of a platform|
|servicePlatformMarkerType|string|The type of markers used in this services platform|
|servicePlatformName|string|The technology platform used by this service|
|specificRequirements|array[object]|Additional arbitrary requirements for a particular platform|
|description|string||
|key|string||
|vendorContact|object||
|vendorAddress|string|The street address of the vendor|
|vendorCity|string|The name of the city where the vendor is located|
|vendorContactName|string|The name or identifier of the primary vendor contact|
|vendorCountry|string|The name of the country where the vendor is located|
|vendorDescription|string|A description of the vendor|
|vendorEmail|string|The primary email address used to contact the vendor|
|vendorName|string|The human readable name of the vendor|
|vendorPhone|string|The primary phone number used to contact the vendor|
|vendorURL|string|The primary URL for the vendor|


 

+ Parameters
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
        "services": [
            {
                "serviceDescription": "A combined DNA extract and Sequencing process using technology and science. Lots of automated pipet machines.",
                "serviceId": "085d298f",
                "serviceName": "The Deluxe Service",
                "servicePlatformMarkerType": "FIXED",
                "servicePlatformName": "RNA-seq",
                "specificRequirements": [
                    {
                        "description": "The genus of the samples (ex Aedes)",
                        "key": "genus"
                    },
                    {
                        "description": "The species of the samples (ex vexans)",
                        "key": "species"
                    },
                    {
                        "description": "Aproximate volume of each sample (ex 2.3 ml)",
                        "key": "volumePerWell"
                    },
                    {
                        "description": "Does DNA extraction need to happen before sequencing (ex true)",
                        "key": "extractDNA"
                    }
                ]
            }
        ],
        "vendorContact": {
            "vendorAddress": "123 Main Street",
            "vendorCity": "Townsville",
            "vendorContactName": "Bob Robertson",
            "vendorCountry": "USA",
            "vendorDescription": "This is a sequencing vendor. Sequencing happens here.",
            "vendorEmail": "bob@bob.org",
            "vendorName": "The Example Vendor Lab",
            "vendorPhone": "+1-800-555-5555",
            "vendorURL": "https://sequencing.org/vendor"
        }
    }
}
```
