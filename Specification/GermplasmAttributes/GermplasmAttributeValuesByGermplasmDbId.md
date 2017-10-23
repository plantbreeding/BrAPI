## Germplasm attribute values by germplasmDbId [/brapi/v1/germplasm/{germplasmDbId}/attributes?attributeList={attributeDbId},{attributeDbId}&pageSize={pageSize}&page={page}]

Status: ACCEPTED.]

### Germplasm attribute values [GET]
Values for all attributes by default.
+ Parameters
    + germplasmDbId (required, string, `993`) ... The germplasm characterized
    + attributeDbId (optional, string, `1`) ... Restrict the response to only the listed attributes.
    + pageSize (optional, number, `10000`) ... the number of attributes to return in one request, defaults to 1000.
    + page (optional, number, `1`) ... Required if `pageSize` is given; and requires that `pageSize` be given. The first page is 1, not 0.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 1,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : [
                {
                    "germplasmDbId": "993",
                    "data": [
                        {
                            "attributeDbId": "1",
                            "attributeName": "Rht-B1b",
                            "attributeCode": "RHT",
                            "value": "Present", 
                            "determinedDate": "2007-05-28"
                        }
                    ]
                }
            ]
        }
