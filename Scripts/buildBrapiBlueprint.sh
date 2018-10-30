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

echo "Generating READMEs"
${BRAPI_DIR}/Scripts/buildOpenAPI.py $BRAPI_DIR
${BRAPI_DIR}/Scripts/buildReadMes.py $BRAPI_DIR
echo "READMEs Generated"

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
	       "GermplasmAttributes/README.md"
	       "Programs/README.md"
	       "Trials/README.md"
	       "Studies/README.md"
	       "Locations/README.md"
	       "Phenotypes/README.md"
	       "ObservationVariables/README.md"
	       "Images/README.md"
	       "GenomeMaps/README.md"
	       "Markers/README.md"
	       "MarkerProfiles/README.md"
	       "Samples/README.md"
	       "VendorSamples/README.md"
	       "Lists/README.md"
	       "People/README.md"
) 

for i in ${sources[@]}; do
    echo $BRAPI_PREFIX$i;
    cat $BRAPI_PREFIX$i >> $BRAPI_FILE;
    echo "" >> $BRAPI_FILE;
done

rm -rf $BRAPI_FILE.json;
echo "{&dquot;code&dquot;: &dquot;" >> $BRAPI_FILE.json;
cat $BRAPI_FILE >> $BRAPI_FILE.json;
echo " &dquot; }" >> $BRAPI_FILE.json;

sed -i 's|\\|\\\\|g' $BRAPI_FILE.json;
sed -i 's|\"|\\\"|g' $BRAPI_FILE.json;
sed -i 's|&dquot;|\"|g' $BRAPI_FILE.json;
sed -i ':a;N;$!ba;s|\n|\\n|g' $BRAPI_FILE.json;

echo $BRAPI_FILE