## Variable Details [/brapi/v1/variables/{id}]
Scope: CORE.
Status: ACCEPTED.

Retrieve variable details

+ Parameters
    + id (required, string, `CO_334:0100622`) ... string containing id's of the variables

### Retrieve details of observation variable by id [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {},
                "status": {},
                "datafiles": []
            },
            "result": {
                "traitDbId": "123",
                "observationVariableId": "CO_334:0100622",
                "name": "carot_spectro",
                "fullName": "Carotenoid content by spectro",
                "trait": {
                    "traitId": "CO_334:0100620",
                    "name": "Estimation :Total Carotenoid Content_method",
                    "description": "Total extracted carotenoids in cassava storage root as estimated by spectrophotometer"
                },
                "measurementMethod": {
                    "methodId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "scale": {
                    "scaleId": "CO_334:0100526",
                    "name": "ug/g",
                    "dataType": "Numeric",
                    "validValues": {
                        "min": "0",
                        "max": "100",
                        "categories": null
                    }
                },
                "defaultValue": null
            }
        }
