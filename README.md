# BrAPI
Repository for version control of the BrAPI specification

### Versions
Version | Status | Release Date | Apiary | Notes
--|--|--|--|--
[V1.2](https://github.com/plantbreeding/API/tree/master) | In Development | Planned: Apr 27, 2018 | [DEV](https://brapidev.docs.apiary.io/#) | [Project](https://github.com/plantbreeding/API/projects/2)
[V1.1](https://github.com/plantbreeding/API/tree/V1.1) | Latest Stable Release | Jan 26, 2018 | [PROD](https://brapi.docs.apiary.io/#) | [Release Notes](https://github.com/plantbreeding/API/releases/tag/V1.1) [Change File](https://github.com/plantbreeding/API/files/1668289/BrAPI_V1-1_Release_Notes.xlsx)
[V1.0](https://github.com/plantbreeding/API/tree/V1.0) | Archived | Nov 13, 2017 | [Archive-1.0](https://brapiarchive10.docs.apiary.io/#) | [Release Notes](https://github.com/plantbreeding/API/releases/tag/V1.0)

### INTRODUCTION


The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve their data to crop breeding applications. It is a shared, open API, to be used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is currently in an actively developing state, so now is the time for potential participants to help shape the specifications to ensure their needs are addressed. The listserve for discussions and announcements is [here](http://mail2.sgn.cornell.edu/cgi-bin/mailman/listinfo/plant-breeding-api). Additional documentation is in the [Github wiki](https://github.com/plantbreeding/API/wiki).
For demos and implementations examples checkout [apiary documentation](http://docs.brapi.apiary.io/).


Call | Description 
------------ | -------------
[Authentication](https://github.com/plantbreeding/API/blob/master/Specification/Authentication/) | This resource refers to the authentication mechanism for the API.
[Calls](https://github.com/plantbreeding/API/blob/master/Specification/Calls/) | N.A.
[Crops](https://github.com/plantbreeding/API/blob/master/Specification/Crops/) | For multi crop systems this is a useful call to list all the supported crops.
[GenomeMaps](https://github.com/plantbreeding/API/blob/master/Specification/GenomeMaps/) | Retrieving genetic or physical maps
[Germplasm](https://github.com/plantbreeding/API/blob/master/Specification/Germplasm/) |  N.A.
[GermplasmAttributes](https://github.com/plantbreeding/API/blob/master/Specification/GermplasmAttributes/) | N.A.
[Locations](https://github.com/plantbreeding/API/blob/master/Specification/Locations/) | Location calls.
[MarkerProfiles](https://github.com/plantbreeding/API/blob/master/Specification/MarkerProfiles/) | For the purposes of this API, the definition of markerprofile is *the allele calls for a specified germplasm line, for all markers, for a specified set of genotyping experiments or all experiments.*
[Markers](https://github.com/plantbreeding/API/blob/master/Specification/Markers/) |  N.A.
[ObservationVariables](https://github.com/plantbreeding/API/blob/master/Specification/ObservationVariables/) | Observation variable data response
[Phenotypes](https://github.com/plantbreeding/API/blob/master/Specification/Phenotypes/) | API to retrieve data (phenotype, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval.
[Programs](https://github.com/plantbreeding/API/blob/master/Specification/Programs/) | Call to retrieve a list of programs.
[Samples](https://github.com/plantbreeding/API/blob/master/Specification/Samples/) | API methods for traking/managing plant samples and realted metatdata. Sample in the context of these BrAPI calls, is defined as the actual bilogical plant material collected from the field.
[Studies](https://github.com/plantbreeding/API/blob/master/Specification/Studies/) | Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).
[Traits](https://github.com/plantbreeding/API/blob/master/Specification/Traits/) | Services related to trials. Trials comprise of multiple studies.
[Trials](https://github.com/plantbreeding/API/blob/master/Specification/Trials/) | Services related to trials. Trials comprise of multiple studies.
