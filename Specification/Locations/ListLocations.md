## List [/brapi/v1/locations?locationType={locationType}]

Implemented by: Germinate

Get a list of locations.

* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.

**Note**: Consider revising to describe polygon lat/lan points and check if adopting http://geojson.org/ is worth doing for v1.

### List locations [GET]

+ Parameters
    + locationType (optional, string, `Breeding Locations`) - Filter by location type specified.

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
                "data" : [
                    {
                        "locationDbId": 1,
                        "locationType" : "Breeding Location",
                        "name": "Ibadan",
                        "abbreviation": "IB",
                        "countryCode": "NGA",
                        "countryName": "Nigeria",
                        "latitude": -21.5,
                        "longitude": 165.5,
                        "altitude": 12,
                        "additionalInfo": 
                        {
                            "annualMeanRain" : "value", 
                            "soilDescription" :"23"
                        }
                    },
                    {
                        "locationDbId": 2,
                        "locationType" : "Storage Location",
                        "name": "Goa",
                        "abbreviation": "GO",
                        "countryCode": "IND",
                        "countryName": "India",
                        "latitude": 28.36,
                        "longitude": 77.12,
                        "altitude": 10,
                        "additionalInfo": {
                            "name1" : "value1",
                            "name2" : "value2"
                        }
                    }
                ]
            }
        }

