#!/bin/bash

# Be sure to install the apiary gem; https://github.com/apiaryio/apiary-client
# gem install apiaryio

# Param 1: compiled blueprint file (default "$HOME/brapi_blueprint.apib")
# Param 2: name of the apiary api (default "brapi")

if [ -f "$1" ]; then
	BRAPI_FILE=${1};
else
	BRAPI_FILE=${HOME}/brapi_blueprint.apib;
fi

if [ -z "$2" ]; then
	APINAME=brapidev
else
	APINAME=${2}
fi


# Publish to apiary
echo $BRAPI_FILE
echo $APINAME

#apiary publish --path $BRAPI_FILE --api-name $APINAME

BRAPI_FILE_CONTENTS=`cat $BRAPI_FILE`

curl -i \
  --request POST \
  --header "Authentication:Token $APIARY_TOKEN" \
  --header "content-type:application/json; charset=utf-8" \
  --data-binary @$BRAPI_FILE \
  https://api.apiary.io/blueprint/publish/$APINAME 

if [ $? -ne 0 ]; then
	echo "ERROR: Apiary rejected the file"
	exit 1
fi