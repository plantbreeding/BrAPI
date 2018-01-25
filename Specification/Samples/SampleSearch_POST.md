### Post Sample Search [POST /brapi/v1/samples-search] 
+ Request

        {
            "sampleDbId": ["Unique-Plant-SampleID-1", "Unique-Plant-SampleID-2"],
            "observationUnitDbId": ["abc123", "a1b2c3"],
            "plateDbId": ["PlateID-123"],
            "germplasmDbId": ["def456"]
        }

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":1000, 
                    "currentPage":0, 
                    "totalCount":2, 
                    "totalPages":1 
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data": [
                    {
                          "sampleDbId": "Unique-Plant-SampleID-1",
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
                          "notes": "Cut from infected leaf"
                      },{
                          "sampleDbId": "Unique-Plant-SampleID-2",
                          "observationUnitDbId": "a1b2c3",
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
                          "notes": "Cut from infected leaf"
                      }
                  ]
            }
        }
        
