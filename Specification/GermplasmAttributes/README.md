# Group Germplasm Attributes
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.





## Get Attributes Categories  [GET /brapi/v1/attributes/categories{?pageSize}{?page}]

 Scope: OTHER. Status: ACCEPTED.
Implementation target date: PAG2016
List all available attribute categories.
<a href="https://test-server.brapi.org/brapi/v1/attributes"> test-server.brapi.org/brapi/v1/attributes/categories</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 1,
            "pageSize": 10,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCategoryDbId": "1",
                "name": "Morphological"
            },
            {
                "attributeCategoryDbId": "2",
                "name": "Agronomic"
            }
        ]
    }
}
```

## Get Attributes  [GET /brapi/v1/attributes{?attributeCategoryDbId}{?pageSize}{?page}]

 List available attributes.
<a href="https://test-server.brapi.org/brapi/v1/attributes"> test-server.brapi.org/brapi/v1/attributes</a>  

+ Parameters
    + attributeCategoryDbId (Optional, string) ... filter for kind of attributes
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCategoryDbId": "1",
                "code": "RHT",
                "datatype": "Categorical",
                "description": "Allele of marker 11_4769, diagnostic for allele b of reduced-height gene Rht-B1",
                "name": "Rht-B1b",
                "uri": "http://www.cropontology.org/rdf/CO_321:0000020",
                "values": [
                    "Present",
                    "Absent",
                    "Heterozygous"
                ]
            }
        ]
    }
}
```

## Get Germplasm Attributes by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/attributes{?attributeDbIds}{?attributeList}{?pageSize}{?page}]

Values for all attributes by default.

<a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/attributes</a> 

+ Parameters
    + germplasmDbId (Required, string) ... The germplasm characterized
    + attributeDbIds (Optional, array) ... Restrict the response to only the listed attributeDbIds.
    + attributeList (Optional, array) ... **Deprecated** Use "attributeDbIds" instead
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCode": "RHT",
                "attributeDbId": "1",
                "attributeName": "Rht-B1b",
                "determinedDate": "2007-05-28",
                "value": "Present"
            }
        ],
        "germplasmDbId": "01BEL084609"
    }
}
```