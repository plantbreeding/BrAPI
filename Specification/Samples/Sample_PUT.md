### Add a sample [PUT /brapi/v1/samples]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.

+ Request (application/json)

        {
            "sampleDbId": "",
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
        }

+ Response 200

        {
            "metadata": null,
            "result": {
                "sampleDbId" : "Unique-Plant-SampleID"
            }
        }
