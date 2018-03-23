### Save Observation Unit Phenotypes [PUT /brapi/v1/studies/{studyDbId}/observationunits]

Use this call for uploading new Observations as JSON to a system. 

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds.

+ Parameters
    + studyDbId (required, string, `abc123`) ... The study these observation units are related to.
    
+ Request (application/json)

        [
            {
                "observationUnitDbId": "", // ignored if new
                "observationUnitName": "Test-2016-location-34-575",
                "observationLevel": "plot",
                "germplasmDbId": "1",
                "germplasmName": "IR-8",
                "pedigree": "IR-8-FP/IR-8-MP",
                "entryNumber": "1",
                "entryType": "Test entry",
                "plotNumber": "1",
                "plantNumber" : "0",
                "blockNumber" : "1",
                "X" : "1",
                "Y" : "1",
                "replicate": "1",
                "observationUnitXref":[
                    {"source": "biosampleEBI", "id": "SAMEA179865230"},
                    {"source": "gnpis.lot", "id": "INRA:CoeSt6 _SMH03"}, 
                    {"source": "kernelDB", "id": "239865"}
                ],
                "observations": [
                    {
                        "observationDbId": "", // ignored if new
                        "observationVariableDbId": "18020",
                        "observationVariableName": "Plant_height",
                        "collector" : "Mr. Technician",
                        "observationTimeStamp" : "2015-06-16T00:53:26Z",
                        "value": null
                    },
                    { 
                        "observationDbId": "", // ignored if new
                        "observationVariableDbId": "51496",
                        "observationVariableName": "GW100_g",
                        "collector" : "Mr. Technician",
                        "observationTimeStamp" : "2015-06-16T00:53:26Z",
                        "value": null
                    }
                ]
            },
            {
                "observationUnitDbId": "", // ignored if new
                "observationUnitName": "Test-2016-location-34-575",
                "observationLevel": "plot",
                "germplasmDbId": "1",
                "germplasmName": "IR-8",
                "pedigree": "IR-8-FP/IR-8-MP",
                "entryNumber": "1",
                "entryType": "Test entry",
                "plotNumber": "1",
                "plantNumber" : "0",
                "blockNumber" : "1",
                "X" : "1",
                "Y" : "1",
                "replicate": "1",
                "observationUnitXref":[
                    {"source": "biosampleEBI", "id": "SAMEA179865230"},
                    {"source": "gnpis.lot", "id": "INRA:CoeSt6 _SMH03"}, 
                    {"source": "kernelDB", "id": "239865"}
                ],
                "observations": [
                    {
                        "observationDbId": "", // ignored if new
                        "observationVariableDbId": "18020",
                        "observationVariableName": "Plant_height",
                        "collector" : "Mr. Technician",
                        "observationTimeStamp" : "2015-06-16T00:53:26Z",
                        "value": null
                    },
                    { 
                        "observationDbId": "", // ignored if new
                        "observationVariableDbId": "51496",
                        "observationVariableName": "GW100_g",
                        "collector" : "Mr. Technician",
                        "observationTimeStamp" : "2015-06-16T00:53:26Z",
                        "value": null
                    }
                ]
            }
        ]


+ Response 200 (application/json)
    + Body
    
            {
                "metadata": {
                    "status": [ {
                        "code":"1",
                        "message": "Upload Successful"
                    } ]
                },
                "result": {
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

+ Request (application/json)
    + Headers
    
            Content-Encoding: gzip
            
    + Body
    
            H4sIAAAAAAAA/+1VXW+bMBR976+w/BwaA4WmvKXrxyItUdSwtls1RUBuiVVjI0MyVVX/+wwdrDEEVdM0tRJ+Aa7POb5f5iKE0N0B+r2e6rdiYRFmILdBTgX/yml+Fk5W2EMYD9BwiGjMhYQVoveIw89O4ixIoCD6kOWGRUzXYCIqdw37yHCOHTzYy/8CW2AFOWUi13ExyCRlQZZUrpl7EZUPkytjpINSWNFYQr1vXMyH5XM616HAc/k42yQhyNbzyn3/Ma3jRaWlcaIKpkNFecyrfaQARAeEKoEPrwANhdt287d2s4SUUVURaPVGq+athHvs3e1givWEM7GRUakRUpEFKvFwfjpR7YJpWZ3FeHo+No9PRq5j2QQ/Dzo1Yp7S7LCseiUwmV2NvU8CFrmLlovpZ2IrEdSp8gCSAzs7/SNi2YUD+HmH9mN/zJkitUTbsOi8N1+XNvJ1IGkQMqgbe0QsvQu6eFW7z4tOWq6Bxmv99tT0SDAGUS5eWmkqD5EP0ZrTiAb8DUf6NFEFUdUu6ep6OwZxDdP1CfEc27Pc7/tEtgHbFF7yDWMNRFt3NEutO/NPk+6YRyfuXyT98sYkZBl/sHzv3of661Ud+vHQj4d+PKB+PLyH31U/HtpP+9/j4eDl+xeKyAPWSQwAAA==


+ Response 200 (application/json)
    + Body
    
            {
                "metadata": {
                    "status": [ {
                        "code":"1",
                        "message": "Upload Successful"
                    } ]
                },
                "result": {
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