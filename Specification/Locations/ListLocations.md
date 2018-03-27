## List Locations [/brapi/v1/locations]

Implemented by: Germinate

Get a list of locations.

* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.

**Note**: Consider revising to describe polygon lat/lan points and check if adopting http://geojson.org/ is worth doing for v1.

| Variable                | Datatype        | Description                                             | Required |
| ----------------------- | --------------- | ------------------------------------------------------- | :------: |
| locationDbId            | string          | string identifier                                       |    Y     |
| locationType            | string          | string                                                  |    Y     |
| name                    | string          | string                                                  |    Y     |
| **Deprecated** abreviation| string        | **Use abbreviation**                                    |          |
| abbreviation            | string          | string                                                  |          |
| countryCode             | string          | ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec  |          |
| countryName             | string          | string                                        |          |
| latitude                | string          | string                                        |          |
| longitude               | string          | string                                        |          |
| altitude                | string          | string                                        |          |
| instituteName           | string          | string   each institute/laboratory can have several experimental field    |          |
| **Deprecated** instituteAdress| string    | **Use instituteAddress**                           |          |
| instituteAddress        | string          | string                                        |          |
| additionalInfo          | object          | Additional arbitrary info on the study, like objectives or publications |          |


### List locations [GET /brapi/v1/locations{?locationType}{?pageSize}{?page}]
+ Parameters
    + locationType (optional, string, `Breeding Location`) ... Filter by location type specified.
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
        
        {
            "metadata": {
                "pagination": { 
                    "currentPage": 0,
                    "pageSize": 1000,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data" : [
                    {
                        "locationDbId": "abc123",
                        "locationType" : "Breeding Location",
                        "name": "Ibadan",
                        "abbreviation": "IB",
                        "countryCode": "NGA",
                        "countryName": "Nigeria",
                        "latitude": -21.5,
                        "longitude": 165.5,
                        "altitude": 12,
                        "instituteName": "INRA - GDEC",
                        "instituteAddress": "route foo, Clermont Ferrand, France",
                        "additionalInfo": 
                        {
                            "annualMeanRain" : "value", 
                            "soilDescription" :"23"
                        }
                    },
                    {
                        "locationDbId": "def456",
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

