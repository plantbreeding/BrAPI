

## Study Germplasm Details [/brapi/v1/studies/{studyDbId}/germplasm?pageSize={pageSize}&page={page}]

Scope: PHENOTYPING

### Study Germplasm Details [GET]
+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize": 1000, 
                    "currentPage": 0, 
                    "totalCount": 2, 
                    "totalPages": 1 
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
