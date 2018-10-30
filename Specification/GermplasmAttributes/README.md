# Group Germplasm Attributes
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.





## Attributes [/brapi/v1/attributes] 




### Get Attributes Categories  [GET /brapi/v1/attributes/categories{?page}{?pageSize}]

List all available attribute categories.

 

+ Parameters
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
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCategoryDbId": "1",
                "attributeCategoryName": null,
                "name": "Morphological"
            },
            {
                "attributeCategoryDbId": "2",
                "attributeCategoryName": null,
                "name": "Agronomic"
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





### Get Attributes  [GET /brapi/v1/attributes{?attributeCategoryDbId}{?page}{?pageSize}]

List available attributes.

 

+ Parameters
    + attributeCategoryDbId (Optional, ) ... Unique identifier for the general category for the attribute. very similar to Trait class.
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
            "totalCount": 10,
            "totalPages": 5
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCategoryDbId": "2",
                "attributeDbId": "1",
                "attributeName": null,
                "code": "RHT",
                "contextOfUse": null,
                "crop": null,
                "datatype": "Categorical",
                "defaultValue": null,
                "description": "Allele of marker 11_4769",
                "documentationURL": null,
                "growthStage": null,
                "institution": null,
                "language": null,
                "method": null,
                "name": "Rht-B1b",
                "ontologyDbId": null,
                "ontologyName": null,
                "ontologyRefernce": null,
                "scale": null,
                "scientist": null,
                "status": null,
                "submissionTimestamp": null,
                "synonyms": null,
                "trait": null,
                "uri": "http://www.brapi.org/ontology/MO_123:1000001",
                "values": "Present",
                "xref": null
            },
            {
                "attributeCategoryDbId": "3",
                "attributeDbId": "2",
                "attributeName": null,
                "code": "WEV",
                "contextOfUse": null,
                "crop": null,
                "datatype": "Categorical",
                "defaultValue": null,
                "description": "Resistance allele",
                "documentationURL": null,
                "growthStage": null,
                "institution": null,
                "language": null,
                "method": null,
                "name": "Weevil Resistance",
                "ontologyDbId": null,
                "ontologyName": null,
                "ontologyRefernce": null,
                "scale": null,
                "scientist": null,
                "status": null,
                "submissionTimestamp": null,
                "synonyms": null,
                "trait": null,
                "uri": "http://www.brapi.org/ontology/MO_123:1000002",
                "values": "Absent",
                "xref": null
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

