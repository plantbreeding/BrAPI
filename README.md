# BrAPI
Repository for version control of the BrAPI specification

### INTRODUCTION


The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve their data to crop breeding applications. It is a shared, open API, to be used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is currently in an actively developing state, so now is the time for potential participants to help shape the specifications to ensure their needs are addressed. The listserve for discussions and announcements is at http://mail2.sgn.cornell.edu/cgi-bin/mailman/listinfo/plant-breeding-api . Additional documentation is in the Github wiki.


Call | Description 
------------ | -------------
[Authentication](https://github.com/plantbreeding/API/blob/master/Specification/Authentication/Authentication.md) | This resource refers to the authentication mechanism for the API.
[Calls](https://github.com/plantbreeding/API/blob/master/Specification/Calls/Calls.md) | N.A.
[Crops](https://github.com/plantbreeding/API/blob/master/Specification/Crops/Crops.md) | For multi crop systems this is a useful call to list all the supported crops.
[GenomeMaps](https://github.com/plantbreeding/API/blob/master/Specification/GenomeMaps/GenomeMaps.md) | Retrieving genetic or physical maps
[Germplasm](https://github.com/plantbreeding/API/blob/master/Specification/Germplasm/Germplasm.md) |  N.A.
[GermplasmAttributes](https://github.com/plantbreeding/API/blob/master/Specification/GermplasmAttributes/GermplasmAttributes.md) | N.A.
[Locations](https://github.com/plantbreeding/API/blob/master/Specification/Locations/Locations.md) | Location calls.
[MarkerProfiles](https://github.com/plantbreeding/API/blob/master/Specification/MarkerProfiles/MarkerProfiles.md) | For the purposes of this API, the definition of markerprofile is *the allele calls for a specified germplasm line, for all markers, for a specified set of genotyping experiments or all experiments.*
[Markers](https://github.com/plantbreeding/API/blob/master/Specification/Markers/Markers.md) |  N.A.
[ObservationVariables](https://github.com/plantbreeding/API/blob/master/Specification/ObservationVariables/ObservationVariables.md) | Observation variable data response
[Phenotypes](https://github.com/plantbreeding/API/blob/master/Specification/Phenotypes/Phenotypes.md) | API to retrieve data (phenotype, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval.
[Programs](https://github.com/plantbreeding/API/blob/master/Specification/Programs/Programs.md) | N.A.
[Samples](https://github.com/plantbreeding/API/blob/master/Specification/Samples/Samples.md) | API methods for traking/managing plant samples and realted metatdata. Sample in the context of these BrAPI calls, is defined as the actual bilogical plant material collected from the field.
[Studies](https://github.com/plantbreeding/API/blob/master/Specification/Studies/Studies.md) | Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).
[Traits](https://github.com/plantbreeding/API/blob/master/Specification/Traits/Traits.md) | Services related to trials. Trials comprise of multiple studies.
[Trials](https://github.com/plantbreeding/API/blob/master/Specification/Trials/Trials.md) | Services related to trials. Trials comprise of multiple studies.
