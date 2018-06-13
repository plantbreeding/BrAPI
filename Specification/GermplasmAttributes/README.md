# Group Germplasm Attributes
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.





## Attributes [Get /brapi/v1/attributes{?attributeCategoryDbId}{?pageSize}{?page}]

 List available attributes.
<a href="https://test-server.brapi.org/brapi/v1/attributes"> test-server.brapi.org/brapi/v1/attributes</a>  

+ Parameters
    + attributeCategoryDbId (Optional, string) ... filter for kind of attributes
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "values": [
                    "Present",
                    "Absent",
                    "Heterozygous"
                ],
                "name": "Rht-B1b",
                "code": "RHT",
                "uri": "http://www.cropontology.org/rdf/CO_321:0000020",
                "datatype": "Categorical",
                "attributeCategoryDbId": "1",
                "description": "Allele of marker 11_4769, diagnostic for allele b of reduced-height gene Rht-B1"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 1,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

## Germplasm/{germplasmdbid}/attributes [Get /brapi/v1/germplasm/{germplasmDbId}/attributes{?attributeDbIds}{?attributeList}{?pageSize}{?page}]

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
    "result": {
        "data": [
            {
                "attributeDbId": "1",
                "attributeCode": "RHT",
                "determinedDate": "2007-05-28",
                "attributeName": "Rht-B1b",
                "value": "Present"
            }
        ],
        "germplasmDbId": "01BEL084609"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 1,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

## Attributes/categories [Get /brapi/v1/attributes/categories{?pageSize}{?page}]

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
    "result": {
        "data": [
            {
                "name": "Morphological",
                "attributeCategoryDbId": "1"
            },
            {
                "name": "Agronomic",
                "attributeCategoryDbId": "2"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 1,
            "totalCount": 2,
            "pageSize": 10,
            "totalPages": 1
        }
    }
}
```