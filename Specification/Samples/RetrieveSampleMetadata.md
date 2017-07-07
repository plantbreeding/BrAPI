## Retrieve sample metadata [/brapi/v1/samples/{sampleId}]

### Retrieve sample metadata [GET]

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
              "studyDbId": "StudyId-123",
              "locationDbId": "LocationId-123",
              "plotId": "PlotId-123",
              "plantId" : "PlantID-123",
              "sampleId" : "Unique-Plant-SampleID",
              "takenBy": "Mr. Technician",
              "sampleTimestamp": "2016-07-27T14:43:22+0100",
              "sampleType" : "TypeOfSample",
              "tissueType" : "TypeOfTissue",
              "notes": "Cut from infected leaf",
              "studyName": "Yield Trial A",
              "season": "Summer",
              "locationName": "Kenya",
              "entryNumber": 11,
              "plotNumber": 1,
              "germplasmDbId": 15,
              "plantingTimestamp": "2016-01-01T23:22:21+0100",
              "harvestTimestamp": "2016-06-30T23:33:23+0100"
            }
        }
        
