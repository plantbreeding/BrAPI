## List [/brapi/v1/locations/{locationDbId}]

Implemented by:  GnpIS

Get a list of locations.

* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.


### Retrieve locations details [GET]

| Variable                | Datatype        | Description                                             | Required |
| ----------------------- | --------------- | ------------------------------------------------------- | :------: |
| locationDbId            | string          | string identifier                                       |    Y     |
| locationType            | string          | string                                                  |    Y     |
| name                    | string          | string                                                  |    Y     |
| abreviation             | string          | string                                                  |          |
| countryCode             | string          | ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec  |          |
| countryName             | string          | string                                        |          |
| latitude                | string          | string                                        |          |
| longitude               | string          | string                                        |          |
| altitude                | string          | string                                        |          |
| instituteName           | string          | string   each institute/laboratory can have several experimental field    |          |
| instituteAdress         | string          | string                                        |          |
| additionalInfo          | object          | Additional arbitrary info on the study, like objectives or publications |          |


+ Response 200 (application/json)
        
        {
            "metadata": {
                "pagination": { 
                    "pageNumber": 1,
                    "pageSize": 2,
                    "totalCount": 100,
                    "totalPages": 50
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                {
                    "locationDbId": 1,
                    "locationType" : "Breeding Location",
                    "name": "Ibadan",
                    "abreviation": "IB",
                    "countryCode": "NGA",
                    "countryName": "Nigeria",
                    "latitude": -21.5,
                    "longitude": 165.5,
                    "altitude": 12,
                    "instituteName"; "INRA - GDEC",
                    "instituteAdress"; "road foo, nigeria",
                    "additionalInfo": 
                    {
                        "annualMeanRain" : "value", 
                        "soilDescription" :"23"
                    }
                }
            }
        }

