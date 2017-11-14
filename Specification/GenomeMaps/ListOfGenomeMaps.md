## Genome Map  [/brapi/v1/maps?species={species}&pageSize={pageSize}&page={page}&type={type}]

Status: ACCEPTED

Implemented by: Germinate, Cassavabase

Used by: Flapjack

Get list of maps

do we need list of parents and specify mapping population?

### Get list of maps [GET]
+ Parameters
   + species (optional, string, ``) ... Species
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination" : {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
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
