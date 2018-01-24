### Request For Samples to be Generated [POST /brapi/v1/samples/collect-request]

Call to be implemented by a Sample Tracking system. Breeding management client systems should make this call to a Sample Tracking system to have new samples generated and sent to a Vendor.
The Breeding management system making this call should have "GET /studies/{studyDbId}/observationunits/{observationUnitDbId}" so the Sample Tracker can get the details of each Observation Unit.

+ Request (application/json)

    {
        "collectSamplesRequestDbId": "",
        "vendorDbId": "",
        "purpose": "genotyping",
        "observationUnits": [
            {
                "observationUnitDbId": "",
                "numberOfSamples": 2
            },
            {
                "observationUnitDbId": "",
                "numberOfSamples": 2
            }
        ]
    }


+ Response 200

    {
        "metadata": {
            "pagination": {
                "pageSize": 0,
                "currentPage": 0,
                "totalCount": 0,
                "totalPages": 0
            },
            "status": [],
            "datafiles": []
        },
        "result": {
            "sampleGroupDbId" : "Unique-Plant-SampleGroupID-From-SampleTracker"
        }
    }
