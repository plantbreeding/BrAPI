## Genome Map  [/brapi/v1/maps?species={speciesId}&pageSize={pageSize}&page={page}&type={type}]

Status: ACCEPTED

Implemented by: Germinate, Cassavabase

Used by: Flapjack

Get list of maps

do we need list of parents and specify mapping population?

### Get list of maps [GET]

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination" : {
                    "pageSize": 30,
                    "currentPage": 2,
                    "totalCount": 40,
                    "totalPages": 2
                }
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data" : [
                    {
                        "mapDbId": "1",
                        "name": "Some Map",
                        "species": "Some species",
                        "type": "Genetic",
                        "unit": "cM",
                        "publishedDate": "2008-04-16",
                        "markerCount": 1000,
                        "linkageGroupCount": 7,
                        "comments": "This map contains ..."
                    },
                    {
                        "mapDbId": "2",
                        "name": "Some Other map",
                        "species": "Some Species",
                        "type": "Genetic",
                        "unit": "cM",
                        "publishedDate": "2009-01-12",
                        "markerCount": 1501,
                        "linkageGroupCount": 7,
                        "comments": "this is blah blah"
                    }
                ]
            }
        }
