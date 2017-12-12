### Save Observation Unit Phenotypes (zip file) [POST /brapi/v1/studies/{studyDbId}/observationunits/zip]

Use this call for uploading new Observations as a Batched Zip File to a system. 

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds.

+ Parameters
    + studyDbId (required, string, `abc123`) ... The study these observation units are related to.
    
+ Request (application/zip)
    + Body
        Zip file data with observation unit data


+ Response 200 (application/json)
    + Body
        {
            "metadata": {
                "status": [ {
                    "code":"1",
                    "message": "Upload Successful"
                } ]
            },
            "results": {
                "observationUnitDbIds" : [
                    "123abc", "456def"
                ]
            }
        }
+ Response 400 (application/json)

        {
            "metadata": {
                "status": [ {
                    "code":"42",
                    "message": "Could not update values for Observation Units"
                } ]
            }
        }
        