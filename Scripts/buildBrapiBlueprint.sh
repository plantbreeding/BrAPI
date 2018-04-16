#!/usr/bin/env bash

if [ -d "$1" ]; then
	ROOT_DIRECTORY=${1};
else
	ROOT_DIRECTORY=${HOME};
fi

BRAPI_DIR=${ROOT_DIRECTORY}

BRAPI_FILE=${ROOT_DIRECTORY}/brapi_blueprint.apib

if [ -f $BRAPI_FILE ]; then
    rm $BRAPI_FILE
fi
touch $BRAPI_FILE

# Tedious to write out the names of all the directories and files but this let's us control the order of assembly
BRAPI_PREFIX=${BRAPI_DIR}/Specification/

sources=("README.md" 
	       "GeneralInfo/URL_Structure.md"
	       "GeneralInfo/Response_Structure.md"
	       "GeneralInfo/Error_Handling.md"
	       "GeneralInfo/Date_Time_Encoding.md"
	       "GeneralInfo/Location_Encoding.md"
	       "GeneralInfo/Search_Services.md"
	       "GeneralInfo/Asychronous_Processing.md"
	       "Authentication/README.md" 
	       "Authentication/Authentication.md"
	       "Calls/README.md" 
	       "Calls/Calls.md" 
	       "Germplasm/README.md"
	       "Germplasm/GermplasmSearch_GET.md" 
	       "Germplasm/GermplasmSearch_POST.md"
	       "Germplasm/Germplasm_GET.md"
	       "Germplasm/Germplasm_Pedigree_GET.md"
	       "Germplasm/Germplasm_Progeny_GET.md"
	       "Germplasm/Germplasm_Markerprofiles_GET.md"
	       "Germplasm/BreedingMethods_GET.md"
	       "Germplasm/BreedingMethods_BreedingMethodDbId_GET.md"
	       "GermplasmAttributes/README.md"
	       "GermplasmAttributes/Attributes_GET.md"
	       "GermplasmAttributes/Attributes_Categories_GET.md"
	       "GermplasmAttributes/Germplasm_Attributes_GET.md"
	       "Markers/README.md"
	       "Markers/MarkerSearch_GET.md"
	       "Markers/MarkerSearch_POST.md"
	       "Markers/MarkerDetailsByMarkerDbId.md"
	       "MarkerProfiles/README.md"
	       "MarkerProfiles/MarkerProfiles_GET.md"
	       "MarkerProfiles/MarkerProfiles_MarkerProfileDbId_GET.md"
	       "MarkerProfiles/AlleleMatrices_GET.md"
	       "MarkerProfiles/AlleleMatrixSearch_GET.md"
	       "MarkerProfiles/AlleleMatrixSearch_POST.md"
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
	       "Studies/Studies_ObservationVariables_GET_Deprecated.md"
	       "Studies/Studies_Germplasm_GET.md"
	       "Studies/ObservationLevels_GET.md"
	       "Studies/Studies_ObservationUnits_GET.md"
	       "Studies/Studies_ObservationUnits_POST_Deprecated.md"
	       "Studies/Studies_ObservationUnits_PUT.md"
	       "Studies/Studies_ObservationUnits_Zip_PUT.md"
	       "Studies/Studies_Table_GET.md"
	       "Studies/Studies_Table_POST.md"
	       "Studies/Studies_Layout_GET.md"
	       "Studies/Studies_Layout_PUT.md"
	       "Studies/Studies_Observations_GET.md"
	       "Studies/Studies_Observations_PUT.md"
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
	       "Samples/Sample_PUT.md"
	       "Samples/Samples_GET.md"
	       "Samples/SampleSearch_GET.md"
	       "Samples/SampleSearch_POST.md"
	       "ExternalVendorSamples/README.md"
	       "ExternalVendorSamples/Vendor_Plate_GET.md"
	       "ExternalVendorSamples/Vendor_Plates_POST.md"
	       "ExternalVendorSamples/Vendor_PlateSearch_GET.md"
	       "ExternalVendorSamples/Vendor_PlateSearch_POST.md"
	       "ExternalVendorSamples/Vendor_Specifications_GET.md"
) 

for i in ${sources[@]}; do
    echo $BRAPI_PREFIX$i;
    cat $BRAPI_PREFIX$i >> $BRAPI_FILE;
    echo "" >> $BRAPI_FILE;
done

echo $BRAPI_FILE