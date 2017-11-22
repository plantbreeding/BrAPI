### **Deprecated** Save Observation Unit Phenotypes [POST /brapi/v1/studies/{studyDbId}/observationunits?observationLevel={observationLevel}&pageSize={pageSize}&page={page}]

+ Parameters
    + format (default is JSON, but can be zip) ... In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    
+ Request (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [],
                "datafiles": [ "all_images.zip" ]
            },
            "result" : {
                "transactionDbId": "83748382938",
                "commit" : "true/false",
                "data" : [
                    {
                        "observatioUnitDbId": "abc-123",
                        "studyDbId": 2,
                        "observations": [
                            {
                                "observationVariableDbId": "18020",
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "11"
                            },
                            {   
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "111"
                            },
                            {   
                                "observationVariableDbId": "51497",
                                "observationVariableName": "image",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "myimage1.jpg"
                            }
                        ]
                    },
                    {
                        "observatioUnitDbId": "abc-456",
                        "studyDbId": 3,
                        "observations": [
                            {
                                "observationVariableDbId": "18020",
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "22"
                            },
                            {   
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "222"
                            },
                            {   
                                "observationVariableDbId": "51497",
                                "observationVariableName": "image",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "myimage2.jpg"
                            }
                        ]
                    }
                ]
            }
        }

+ Response 200 (application/json)

+ Response 500 (application/json)

        {
            "metadata": {
                "status": [ {
                    "code":"27",
                    "message": "Could not update observation values. Invalid data."
                } ]
            }
        }


### Save Observation Unit Phenotypes [PUT /brapi/v1/studies/{studyDbId}/observationunits]
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
            "results": {
                "observationUnitDbIds" : [
                    "123abc", "456def"
                ]
            }
        }
+ Response 500 (application/json)

        {
            "metadata": {
                "status": [ {
                    "code":"27",
                    "message": "Could not update observation values. Invalid data."
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
            "results": {
                "observationUnitDbIds" : [
                    "123abc", "456def"
                ]
            }
        }
+ Response 500 (application/json)

        {
            "metadata": {
                "status": [ {
                    "code":"27",
                    "message": "Could not update observation values. Invalid data."
                } ]
            }
        }

### Save Observation Unit Phenotypes (zip file) [POST /brapi/v1/studies/{studyDbId}/observationunits/zip]
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
+ Response 500 (application/json)

        {
            "metadata": {
                "status": [ {
                    "code":"27",
                    "message": "Could not update observation values. Invalid data."
                } ]
            }
        }
        