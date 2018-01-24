## Get a Sample [/brapi/v1/samples/{sampleDbId}]

Used to retrieve the details of a single Sample from a Sample Tracking system.

### Get Sample [GET /brapi/v1/samples/{sampleDbId}]
+ Parameters
    + sampleDbId (required, string, `Unique-Plant-SampleID`) ... the internal DB id for a sample
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [],
                "datafiles": []
            },
            "result": {              
              "sampleDbId": "Unique-Plant-SampleID",
              "observationUnitDbId": "abc123",
              "germplasmDbId": "def456",
              "studyDbId": "StudyId-123",
              "plotDbId": "PlotId-123",
              "plantDbId" : "PlantID-123",
              "plateDbId": "PlateID-123",
              "plateIndex": 0,
              "takenBy": "Mr. Technician",
              "sampleTimestamp": "2016-07-27T14:43:22+0100",
              "sampleType" : "TypeOfSample",
              "tissueType" : "TypeOfTissue",
              "notes": "Cut from infected leaf",
            }
        }
        
