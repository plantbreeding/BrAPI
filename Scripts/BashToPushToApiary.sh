#!/usr/bin/env bash
# Be sure to install the apiary gem; https://github.com/apiaryio/apiary-client
# gem install apiaryio
ROOT_DIRECTORY=/home/brapi
BRAPI_DIR=${ROOT_DIRECTORY}/API
if [ -d "$BRAPI_DIR" ]; then
    cd $BRAPI_DIR
    git pull
else
    cd $ROOT_DIRECTORY
    git clone https://github.com/plantbreeding/API.git -b master --single-branch
fi
## You'll need to get a token (https://login.apiary.io/tokens)
## Storing the key in $ROOT_DIRECTORY/.bash_rc
source ${ROOT_DIRECTORY}/.bash_rc
# echo $APIARY_API_KEY

# Your apiname here; docs.$APINAME.apiary.io
APINAME=brapi

BRAPI_FILE=${ROOT_DIRECTORY}/swagger.yaml

if [ -f $BRAPI_FILE ]; then
    rm $BRAPI_FILE
fi
touch $BRAPI_FILE

# Build your apib file from your nicely structured markdown directory
# Here is how mine looks, 
# tree ./blueprint
# .
# ├── EXAMPLE.json
# ├── blueprint
# │   ├── 0_Intro.md
# │   ├── 1_FeatureA
# │   │   ├── 0_Intro.md
# │   │   ├── 1_Accounts.md
# │   ├── 2_FeatureB
# │   │   ├── 0_Intro.md
# │   │   ├── 1_Status.md
# ├── preview.sh
# ├── synthetic-with-comments.apib
# └── synthetic.apib

# Tedious to write out the names of all the directories and files but this let's us control the order of assembly
BRAPI_PREFIX=${BRAPI_DIR}/Specification/
echo $BRAPI_PREFIX
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
	       "Markers/MarkerSearch.md"
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
	       "Studies/ListSeasons.md"
	       "Studies/ListStudyTypes.md"
	       "Studies/ListStudySummaries.md"
	       "Studies/SearchStudies.md"
	       "Studies/StudyDetails.md"
	       "Studies/StudyObservationVariables.md"
	       "Studies/StudyGermplasmDetails.md"
	       "Studies/ListObservationLevels.md"
	       "Studies/ObservationUnitDetails.md"
	       "Studies/SaveOrUpdateObservationUnits.md"
	       "Studies/StudyObservationUnitsAsTable.md"
	       "Studies/StudyObservationUnitsAsTableSave.md"
	       "Studies/PlotLayoutDetails.md"
	       "Studies/GetObservationUnitsByObservationVariableIds.md"
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
# for ((i=0; i<${sources[*]}; i++));
# do
#    echo $Prefix >> $FILE;
    cat $i >> $BRAPI_FILE
done
# Cleanup the temp files
#until 
#rm ./_synthetic.apib 2> /dev/null
#rm ./_synthetic-with-comments.apib 2> /dev/null

# Watch the sort on the find command
# This will dictate how the file is assembled
#for MARKDOWN in $(find ./blueprint -type f -iname *.md | sort -u); do

	# apiary rejects files with <!-- comments -->
	# make sure they are on one line and this will strip them out.
	# snowcrash is fine with comments oddly enoug
	#
#	cat "$MARKDOWN" | fgrep -v '<!--'  >> ./_synthetic.apib
#	echo "" >> ./_synthetic.apib

	# keep a copy with comments intact for debugging
	#
#	cat "$MARKDOWN"  >> ./_synthetic-with-comments.apib
#	echo "" >> ./_synthetic-with-comments.apib

#done

# Verify synthetic file
#snowcrash -v _synthetic-with-comments.apib

#if [ $? -ne 0 ]; then
#	echo "ERROR: snowcrash says the synthetic file is invalid"
#	exit 1
#fi

# Publish to apiary
echo $BRAPI_FILE
echo $APINAME

apiary publish --path $BRAPI_FILE --api-name $APINAME

if [ $? -ne 0 ]; then
	echo "ERROR: Apiary rejected the file"
	exit 1
fi

# If we've gotten this far, the files are good
# You should be using git and feature branches or you risk losing your work
# mv ./_synthetic.apib  ./synthetic.apib
# mv ./_synthetic-with-comments.apib  ./synthetic-with-comments.apib

# Generate schema json
#snowcrash synthetic.apib --output $APINAME.json 1> /dev/null 2> /dev/null

#if [ $? -ne 0 ]; then
#	echo "ERROR: snowcrash couldn't generate schema file"
#	exit 1
#fi

# Preview sexy 3 column documentation in your browser
#open http://docs.$APINAME.apiary.io/?3ColumnDocumentation=1
