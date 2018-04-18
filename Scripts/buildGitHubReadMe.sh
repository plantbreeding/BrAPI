#!/usr/bin/env bash

if [ -d "$1" ]; then
	ROOT_DIRECTORY=${1};
else
	ROOT_DIRECTORY=${HOME};
fi

BRAPI_DIR=${ROOT_DIRECTORY}

BRAPI_FILE=${ROOT_DIRECTORY}/Specification/README.md

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
) 

for i in ${sources[@]}; do
    echo $BRAPI_PREFIX$i;
    cat $BRAPI_PREFIX$i >> $BRAPI_FILE;
    echo "" >> $BRAPI_FILE;
done

echo $BRAPI_FILE