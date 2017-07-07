## Variable ontology list [/brapi/v1/ontologies?page={page}&pageSize={pageSize}]
Scope: CORE.
Status: ACCEPTED.

Call to retrieve a list of observation variable ontologies available in the system.

### Variable ontology list [GET]

+ Parameters
    + pageSize (optional, integer, `1000`)
    + page (optional, integer, `100`)

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 0,
                    "totalCount": 12,
                    "totalPages": 6
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
                        "copyright": "© 2016, INRA",
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
