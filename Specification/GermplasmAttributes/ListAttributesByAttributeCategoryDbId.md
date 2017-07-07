## List attributes available [/brapi/v1/attributes?attributeCategoryDbId=2]
Scope: OTHER. Status: ACCEPTED.
Implementation target date: PAG2016

### Attributes by attributeCategoryDbId [GET] 

List available attributes.

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|attributeCategoryDbId|string|internal database identifier, not stable |Y|
|code|string|abbreviation||
|uri|string|reference to external documentation, ontology etc.||
|name|string|for display, and stable identifier unique in the database|Y|
|description|string|||
|datatype|string|e.g. Categorical, Numeric, Boolean||
|values|string|array of all possible values for this attribute|Y|
+ Parameters
    + attributeCategoryDbId (optional, string, `2`) ... filter for kind of attributes
+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 10000,
                    "totalPages": 1000
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data" : [
                    "attributeCategoryDbId": 1,
                    "code": "RHT",
                    "uri": "http://www.cropontology.org/rdf/CO_321:0000020",
                    "name": "Rht-B1b",
                    "description": "Allele of marker 11_4769, diagnostic for allele b of reduced-height gene Rht-B1",
                    "attributeCategoryId": 2,
                    "attributeCategoryName": "Agronomic",
                    "datatype": "Categorical",
                    "values": ["Present", "Absent", "Heterozygous"]
                ]
            }
        }
