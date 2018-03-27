## Variable ontology list [/brapi/v1/ontologies]
Scope: CORE.
Status: ACCEPTED.

Call to retrieve a list of observation variable ontologies available in the system.

### Variable ontology list [GET /brapi/v1/ontologies{?page}{?pageSize}]

+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [
                    {
                        "ontologyDbId": "CO_334",
                        "ontologyName": "Wheat ontology",
                        "authors": "J. Snow, H. Peterson",
                        "version": "v1.2",
                        "description": "developped for European genetic studies projects",
                        "copyright": "Copyright 2016, INRA",
                        "licence": "CC BY-SA 4.0"
                    }, {
                        "ontologyDbId": "CO_335",
                        "ontologyName": "Rice ontology",
                        "authors": "J. Doe",
                        "description": "developped for IRRI and amended with partners needs",
                        "version": "v2",
                        "copyright": null,
                        "licence": null
                    }
                ]
            }
        }
