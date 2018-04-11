## Markerprofile search [/brapi/v1/markerprofiles]
Scope: GENOTYPING.
Status: ACCEPTED.

Implemented by: Germinate

Used by: Flapjack

For the requested Germplasm Id and/or Extract Id, returns the Markerprofile Id and number of non-missing allele calls 
(marker/allele pairs).

### Retrieve Markerprofile Ids [GET /brapi/v1/markerprofiles{?germplasmDbId}{?studyDbId}{?sampleDbId}{?extractDbId}{?methodDbId}{?pageSize}{?page}]
+ Parameters
    + germplasmDbId (optional, string, `993`) ... The server's internal ids for the Germplasm IDs, as returned by the **Find markerprofile by Germplasm** service.
    + studyDbId (optional, string, `111`) ... The server's internal id for the StudyDbId
    + sampleDbId (optional, string, `184`) ... The server's internal id for the SampleDbId
    + extractDbId (optional, string, `84`) ... The server's internal id for the ExtractDbId
    + pageSize (optional, integer, `10000`) ... The number of allele call results (marker/allele pairs) to be returned in the response. If multiple experiments are requested, some responses will contain the last results from one experiment followed by the first results from the next.
    + page (optional, integer, `1`) ... Required if `pageSize` is given; and requires that `pageSize` be given. The page indexing starts at 0 (the first page is 'page'=0)
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
                "data" : [
                    {   
                        "markerprofileDbId": "993",
                        "germplasmDbId" : "2374",
                        "uniqueDisplayName": "MyFancyGermplasm",
                        "sampleDbId" : "3937",
                        "extractDbId" : "3939",
                        "analysisMethod": "GoldenGate",
                        "resultCount": 1470
                    },
                    {
                        "markerprofileDbId": "994",
                        "germplasmDbId" : "2374",
                        "uniqueDisplayName" : "Germplasm2",
                        "sampleDbId" : "1234",
                        "extractDbId" : "3939",
                        "analysisMethod": "GBS",
                        "resultCount": 1470
                    }
                ]
            }
        }
        
