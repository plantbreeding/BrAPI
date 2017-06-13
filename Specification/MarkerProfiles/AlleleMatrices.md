## Allele Matrices [/brapi/v1/allelematrices?studyDbId=307
Status: PROPOSED.

Implemented by: GOBII

Used by: Flapjack

This resource is used for reading and writing genomic matrices:
+ GET provides a list of available matrices, optionally filtered by study;
+ POST will provide a means for adding new matrices (content TBD).

### Scores through GET [GET]


+ Parameters: studyDbId restricts the list of matrices to a specific study. 


+ Response 200 (application/json)

        {
            "metadata": {   
                "pagination": {
                    "pageSize": 100,
                    "currentPage": 0,
                    "totalCount": 1,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : { 
                "data": [
                    ["1", "1", "A/B"],
                    ["1", "2", "B"],
                    ["2", "1", "A"],
                    ["2", "2", "A/B"]
                ]
            }
        }
