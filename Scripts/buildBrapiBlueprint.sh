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

sources=(  "GeneralInfo/Intro.md"
	       "GeneralInfo/URL_Structure.md"
	       "GeneralInfo/Response_Structure.md"
	       "GeneralInfo/Error_Handling.md"
	       "GeneralInfo/Date_Time_Encoding.md"
	       "GeneralInfo/Location_Encoding.md"
	       "GeneralInfo/Search_Services.md"
	       "GeneralInfo/Asychronous_Processing.md"
	       "Authentication/README.md" 
	       "Calls/README.md" 
	       "Crops/README.md"
	       "Germplasm/README.md"
	       "Markers/README.md"
	       "MarkerProfiles/README.md"
	       "Programs/README.md"
	       "Trials/README.md"
	       "Studies/README.md"
	       "Phenotypes/README.md"
	       "Traits/README.md"
	       "ObservationVariables/README.md"
	       "GenomeMaps/README.md"
	       "Locations/README.md"
	       "Samples/README.md"
	       "ExternalVendorSamples/README.md"
) 

echo "{&dquot;code&dquot;: &dquot;" >> $BRAPI_FILE;
for i in ${sources[@]}; do
    echo $BRAPI_PREFIX$i;
    cat $BRAPI_PREFIX$i >> $BRAPI_FILE;
    echo "" >> $BRAPI_FILE;
done
echo "&dquot;}" >> $BRAPI_FILE;

sed -i 's|\\|\\\\|g' $BRAPI_FILE;
sed -i 's|\"|\\\"|g' $BRAPI_FILE;
sed -i 's|&dquot;|\"|g' $BRAPI_FILE;
sed -i ':a;N;$!ba;s|\n|\\n|g' $BRAPI_FILE;

echo $BRAPI_FILE