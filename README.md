# BrAPI
Repository for version control of the BrAPI specification

### INTRODUCTION


The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve their data to crop breeding applications. It is a shared, open API, to be used by all data providers and data consumers who wish to participate. Initiated in May 2014, it is currently in an actively developing state, so now is the time for potential participants to help shape the specifications to ensure their needs are addressed. The listserve for discussions and announcements is at http://mail2.sgn.cornell.edu/cgi-bin/mailman/listinfo/plant-breeding-api . Additional documentation is in the Github wiki.


Call | Description 
------------ | -------------
Authentication | This resource refers to the authentication mechanism for the API.
Calls | N.A.
Crops | For multi crop systems this is a useful call to list all the supported crops.
GenomeMaps | Retrieving genetic or physical maps
Germplasm |  N.A.
GermplasmAttributes | N.A.
Locations | Location calls.
MarkerProfiles | For the purposes of this API, the definition of markerprofile is *the allele calls for a specified germplasm line, for all markers, for a specified set of genotyping experiments or all experiments.*
Markers |  N.A.
ObservationVariables | Observation variable data response
Phenotypes | API to retrieve data (phenotype, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval.
Programs | N.A.
Samples | API methods for traking/managing plant samples and realted metatdata. Sample in the context of these BrAPI calls, is defined as the actual bilogical plant material collected from the field.
Studies | Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).
Traits | Services related to trials. Trials comprise of multiple studies.
Trials | Services related to trials. Trials comprise of multiple studies.
