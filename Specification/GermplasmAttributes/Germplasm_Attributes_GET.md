## Germplasm attribute values by germplasmDbId [/brapi/v1/germplasm/{germplasmDbId}/attributes]

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|attributeDbId|string|internal database identifier for this attribute |Y|
|attributeName|string|for display, and stable identifier unique in the database|Y|
|attributeCode|string|abbreviation||
|value|string|value of this attribute of this germplasm|Y|
|determinedDate|date string|date the value was recorded for this germplasm|Y|

### Germplasm attribute values [GET /brapi/v1/germplasm/{germplasmDbId}/attributes{?attributeDbIds}{?pageSize}{?page}]

+ Parameters
    + germplasmDbId (required, string, `993`) ... The germplasm characterized 
    + attributeList (optional, array, `123,234,345`) ... **Deprecated** Use 'attributeDbIds' instead
    + attributeDbIds (optional, array, `123,234,345`) ... Restrict the response to only the listed attributeDbIds.
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "germplasmDbId": "993",
                "data": [
                    {
                        "attributeDbId": "123",
                        "attributeName": "Rht-B1b",
                        "attributeCode": "RHT",
                        "value": "Present", 
                        "determinedDate": "2007-05-28"
                    },
                    {
                        "attributeDbId": "234",
                        "attributeName": "Example Name",
                        "attributeCode": "EXN",
                        "value": "Heterozygous", 
                        "determinedDate": "2010-05-28"
                    }
                ]
            }
        }
