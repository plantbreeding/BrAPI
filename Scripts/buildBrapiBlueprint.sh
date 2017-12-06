#!/usr/bin/env bash

if [ -d "$1" ]; then
	ROOT_DIRECTORY=${1};
else
	ROOT_DIRECTORY=${HOME};
fi

BRAPI_DIR=${ROOT_DIRECTORY}/API

BRAPI_FILE=${ROOT_DIRECTORY}/brapi_blueprint.apib

if [ -f $BRAPI_FILE ]; then
    rm $BRAPI_FILE
fi
touch $BRAPI_FILE

# Tedious to write out the names of all the directories and files but this let's us control the order of assembly
BRAPI_PREFIX=${BRAPI_DIR}/Specification/
cd $BRAPI_PREFIX
sources=("README.md" 
	       "Authentication/README.md" 
	       "Authentication/Authentication.md"
	       "Calls/README.md" 
	       "Calls/Calls.md" 
	       "Germplasm/README.md"
	       "Germplasm/GermplasmSearchGET.md" 
	       "Germplasm/GermplasmSearchPOST.md"
	       "Germplasm/GermplasmDetailsByGermplasmDbId.md"
	       "Germplasm/GermplasmDetailsListByStudyDbId.md"
	       "Germplasm/GermplasmPedigree.md"
	       "Germplasm/GermplasmMarkerprofiles.md"
	       "Germplasm/GermplasmMarkerprofiles.md"
	       "GermplasmAttributes/README.md"
	       "GermplasmAttributes/ListAttributesByAttributeCategoryDbId.md"
	       "GermplasmAttributes/ListAttributeCategories.md"
	       "GermplasmAttributes/GermplasmAttributeValuesByGermplasmDbId.md"
	       "Markers/README.md"
	       "Markers/MarkerSearch_GET.md"
	       "Markers/MarkerSearch_POST.md"
	       "Markers/MarkerDetailsByMarkerDbId.md"
	       "MarkerProfiles/README.md"
	       "MarkerProfiles/MarkerProfileSearch.md"
	       "MarkerProfiles/MarkerProfileData.md"
	       "MarkerProfiles/MarkerProfileAlleleMatrix.md"
	       "MarkerProfiles/ScoresThroughPOST.md"
	       "Programs/README.md"
	       "Programs/ListPrograms.md"
	       "Programs/ProgramSearch.md"
	       "Crops/README.md"
	       "Crops/ListCrops.md"
	       "Trials/README.md"
	       "Trials/ListTrialSummaries.md"
	       "Trials/GetTrialById.md"
	       "Studies/README.md"
	       "Studies/Seasons_GET.md"
	       "Studies/StudyTypes_GET.md"
	       "Studies/StudiesSearch_GET.md"
	       "Studies/StudiesSearch_POST.md"
	       "Studies/Studies_GET.md"
	       "Studies/Studies_ObservationVariables_GET.md"
	       "Studies/Studies_Germplasm_GET.md"
	       "Studies/ObservationLevels_GET.md"
	       "Studies/Studies_ObservationUnits_GET.md"
	       "Studies/Studies_ObservationUnits_POST_Deprecated.md"
	       "Studies/Studies_ObservationUnits_PUT.md"
	       "Studies/Studies_ObservationUnits_Zip_PUT.md"
	       "Studies/Studies_Table_GET.md"
	       "Studies/Studies_Table_POST.md"
	       "Studies/Studies_Layout_GET.md"
	       "Studies/Studies_Observations_GET.md"
	       "Phenotypes/README.md"
	       "Phenotypes/PhenotypeSearch.md"
	       "Traits/README.md"
	       "Traits/ListAllTraits.md"
	       "Traits/TraitDetails.md"
	       "ObservationVariables/README.md"
	       "ObservationVariables/VariableDataTypeList.md"
	       "ObservationVariables/VariableList.md"
	       "ObservationVariables/VariableDetails.md"
	       "ObservationVariables/VariableSearch.md"
	       "ObservationVariables/VariableOntologyList.md"
	       "GenomeMaps/README.md"
	       "GenomeMaps/ListOfGenomeMaps.md"
	       "GenomeMaps/GenomeMapDetails.md"
	       "GenomeMaps/GenomeMapData.md"
	       "GenomeMaps/GenomeMapDataByRangeOnLinkageGroup.md"
	       "Locations/README.md"
	       "Locations/ListLocations.md"
	       "Locations/LocationDetails.md"
	       "Samples/README.md"
	       "Samples/TakeASample.md"
	       "Samples/RetrieveSampleMetadata.md"
) 

for i in ${sources[@]}; do
    cat $i >> $BRAPI_FILE
    echo "" >> $BRAPI_FILE
done

echo $BRAPI_FILE