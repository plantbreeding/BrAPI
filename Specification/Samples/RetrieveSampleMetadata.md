## Retrieve sample metadata [/brapi/v1/samples/{sampleId}]

### Retrieve sample metadata [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : null,
                "status" : null,
                "datafiles": []
            },
            "result": {
              "studyDbId": "StudyId-123",
              "locationDbId": "LocationId-123",
              "plotId": "PlotId-123",
              "plantId" : "PlantID-123",
              "sampleId" : "Unique-Plant-SampleID",
              "takenBy": "Mr. Technician",
              "sampleDate": "2016-07-27",
              "sampleType" : "TypeOfSample",
              "tissueType" : "TypeOfTissue",
              "notes": "Cut from infected leaf",
              "studyName": "Yield Trial A",
              "season": "Summer",
              "locationName": "Kenya",
              "entryNumber": 11,
              "plotNumber": 1,
              "germplasmDbId": 15,
              "plantingDate": "20160101",
              "harvestDate": "20160630"
            }
        }
        
