## Study Germplasm Details [/brapi/v1/studies/{studyDbId}/germplasm?pageSize={pageSize}&page={page}]

Scope: PHENOTYPING

### Study Germplasm Details [GET]
+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (optional, integer, `1000`) ... the number of germplasm entries to be returned in the response
    + page (optional, integer, `10`) ... the desired response page

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status": [],
                "datafiles": [],
            },
            "result": {
                "studyDbId": 123,
                "trialName": "myBestTrial",
                "data": [
                   { 
                        "germplasmDbId": "382",
                        "entryNumber": "1",
                        "germplasmName": "Pahang",
                        "pedigree": "TOBA97/SW90.1057",
                        "seedSource": "SS1",
                        "accessionNumber": "ITC0609",
                        "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                        "synonyms": ["01BEL084609"]
                    },
                    {
                        "germplasmDbId": "394",
                        "entryNumber": "2",
                        "germplasmName": "Pahang",
                        "pedigree": "TOBA97/SW90.1057",
                        "seedSource": "SS2",
                        "accessionNumber": "ITC0727",
                        "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084727",
                        "synonyms": [ "01BEL084727"]
                    }
                ]
            }
        }
