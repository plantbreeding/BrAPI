## Take a Sample [/brapi/v1/samples]

### Take a sample [PUT]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.

+ Request (application/json)

        {
          "plotId": "PlotId-123",
          "plantId" : "PlantID-123",
          "takenBy": "Mr. Technician",
          "sampleDate": "2016-07-27",
          "sampleType" : "TypeOfSample",
          "tissueType" : "TypeOfTissue",
          "notes": "Cut from infected leaf"
        }

+ Response 200

        {
            "metadata": null,
            "result": {
                "sampleId" : "Unique-Plant-SampleID"
            }
        }
