
*NOTE* This might be redundant (incomplete as well) now. Replaced by similar call in study section.

## Germplasm Details List by studyDbId [/brapi/v1/studies/{studyDbId}/germplasm?pageSize=20&page=1]
Scope: CORE. 
Status: ACCEPTED. 
Implemented by: Cassavabase, Tripal Brapi Module, Germinate

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|trialDbId|string|The internal Id of the trial|Y|
|trialName|string|Name of the trial||
|data|array of objects|Each object is a germplasm record representing one of the entries in the trial|Y|
|germplasmDbId|string|Internal db identifier|Y|
|trialEntryNumberId|string|Entry number for this germplasm in the trial||
|defaultDisplayName|string|A string representing the germplasm that will be meaningful to the user|Y|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection||
|germplasmPUI|string|Permanent identifier (e.g. URI, DOI, LSID)||
|pedigree|string|Cross name with optional selection history.||
|seedSource|string|Seed source||
|synonyms|array of string|List of other germplasm name||

