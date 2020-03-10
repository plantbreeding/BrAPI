# BrAPI V2.0
The Breeding API (BrAPI) is a Standardized RESTful Web Service API Specification for communicating Plant Breeding Data. BrAPI allows for easy data sharing between databases and tools involved in plant breeding.

## Versions

### V2

BrAPI V2 is divided into four modules:

**BrAPI Core** - The BrAPI Core module contains high level entities used for organization and management. This includes Programs, Trials, Studies, Locations, People, and Lists

**BrAPI Phenotyping** - The BrAPI Phenotyping module contains entities related to phenotypic observations. This includes Observation Units, Observations, Observation Variables, Traits, Scales, Methods, and Images

**BrAPI Genotyping** - The BrAPI Genotyping module contains entities related to genotyping analysis. This includes Samples, Markers, Variant Sets, Variants, Call Sets, Calls, References, Reads, and Vendor Orders

**BrAPI Germplasm** - The BrAPI Germplasm module contains entities related to germplasm management. This includes Germplasm, Germplasm Attributes, Seed Lots, Crosses, Pedigree, and Progeny

| Version | Status | Release Date | SwaggerHub | Apiary | Notes |
|---------|--------|--------------|------------|--------|-------|
|[V2.0](https://github.com/plantbreeding/API/tree/V2.0) |Released |Mar 11, 2020 | | | [Release Notes / Change File](https://github.com/plantbreeding/API/releases/tag/V2.0)|
|                                                       |                      |             |[BrAPI Core](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Core)               |[BrAPI Core](https://brapicore.docs.apiary.io) | |
|                                                       |                      |             |[BrAPI Phenotyping](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Phenotyping) |[BrAPI Phenotyping](https://brapiphenotyping.docs.apiary.io) | |
|                                                       |                      |             |[BrAPI Genotyping](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Genotyping)   |[BrAPI Genotyping](https://brapigenotyping.docs.apiary.io) | |
|                                                       |                      |             |[BrAPI Germplasm](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Germplasm)     |[BrAPI Germplasm](https://brapigermplasm.docs.apiary.io) | |

### V1

Version | Status | Release Date | SwaggerHub | Apiary | Notes
--|--|--|--|--|--
[V1.3](https://github.com/plantbreeding/API/tree/V1.3) | Archived | Nov 01, 2018 |[Archive-1.3](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI)     | [Archive-1.3](https://brapi.docs.apiary.io/#)          | [Release Notes](https://github.com/plantbreeding/API/releases/tag/V1.3) / [Change File]()
[V1.2](https://github.com/plantbreeding/API/tree/V1.2) | Archived | Apr 27, 2018 |[Archive-1.2](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI/1.2) | [Archive-1.2](https://brapiarchive12.docs.apiary.io/#) | [Release Notes](https://github.com/plantbreeding/API/releases/tag/V1.2) / [Change File](https://github.com/plantbreeding/API/files/1964628/BrAPI_V1-2_Release_Notes.xlsx)
[V1.1](https://github.com/plantbreeding/API/tree/V1.1) | Archived | Jan 26, 2018 |                                                                          | [Archive-1.1](https://brapiarchive11.docs.apiary.io/#) | [Release Notes](https://github.com/plantbreeding/API/releases/tag/V1.1) / [Change File](https://github.com/plantbreeding/API/files/1668289/BrAPI_V1-1_Release_Notes.xlsx)
[V1.0](https://github.com/plantbreeding/API/tree/V1.0) | Archived | Nov 13, 2017 |                                                                          | [Archive-1.0](https://brapiarchive10.docs.apiary.io/#) | [Release Notes](https://github.com/plantbreeding/API/releases/tag/V1.0)

## General Reference Documentation
- [URL Structure](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/URL_Structure.md)
- [Response Structure](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Response_Structure.md)
- [Date/Time Encoding](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Date_Time_Encoding.md)
- [Location Encoding](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Location_Encoding.md)
- [Error Handling](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Error_Handling.md)
- [Search Services](https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Search_Services.md)



## Resources
[Brapi.org](https://brapi.org) - The home of all things BrAPI

[BrAPI On Apiary](https://brapi.docs.apiary.io/#) - Apiary documentation of BrAPI

[BrAPI On SwaggerHub](https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI) - SwaggerHub documentation of BrAPI

[BrAPI Community Forum](https://forum.brapi.org) - Consult with BrAPI experts from all over the world

[BRAVA](http://webapps.ipk-gatersleben.de/brapivalidator/) - Test your BrAPI Server with this robust test client

[BrAPI Test Server](https://test-server.brapi.org) - Test your BrAPI Client against sample data

